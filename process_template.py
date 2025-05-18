#!/usr/bin/env python3

import file_io

STYLES = [["<b>", "</b>"], ["<i>", "</i>"], ["", ""]]

HEADER= """
<!DOCTYPE html>
<!-- DO NOT EDIT. This file is generated from a template -->
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <meta name="author" content="Patrick Sanan" />
    <title>Swiss German in N Flashcards</title>
    <link rel="stylesheet" href="styles/styles.css" />
  </head>
<body>
"""

FOOTER="</body></html>"

def _entry_to_html(entry):
    style = 0
    html_to_join = ["<tr>\n"]
    for key in file_io.KEYS:
        html_to_join.append("<td>\n")
        sub_html_to_join = []
        for string in entry[key]:
            sub_html_to_join.append(
                f"{STYLES[style][0]}{string}{STYLES[style][1]}")
        html_to_join.append(
            " <font color='grey'>/</font> ".join(sub_html_to_join))
        html_to_join.append("\n</td>\n")
        style += 1
    html_to_join.append("</tr>\n")
    return "".join(html_to_join)


def process_template(path, entries_by_primary_key):
    found_entries_by_primary_key = {}
    lines_out = [HEADER]
    with open(path, "r") as template_file:
        for line in template_file:
            line_stripped = line.strip()
            if line_stripped.startswith("<li>"):
                primary_key_potential = line_stripped.removeprefix(
                    r"<li>").removesuffix(r"<\li>").strip()
                if primary_key_potential in entries_by_primary_key:
                    primary_key = primary_key_potential
                    entry = entries_by_primary_key[primary_key]
                    found_entries_by_primary_key[primary_key] = entry
                    lines_out.append(_entry_to_html(entry))
                else:
                    print("WARNING: didn't find entry for primary key:",
                          primary_key_potential)
                    lines_out.append(f'<tr><font color="red">{line}</font></tr>')
            elif line_stripped.startswith("<ul>"):
                lines_out.append("<p><table>\n")
            elif line_stripped.startswith("</ul>"):
                lines_out.append("</p></table>\n")
            else:
                lines_out.append(line)
    lines_out.append(FOOTER)
    if path.endswith(".template.html"):
        out_path = path.replace(".template.html", ".html")
    else:
        out_path = path + ".out.html"
    with open(out_path, "w") as out_file:
        for line in lines_out:
            out_file.write(line)
    return out_path, found_entries_by_primary_key


if __name__ == "__main__":
    entries = file_io.entries_from_tsv("translations.tsv")
    entries_by_primary_key = file_io.entries_by_primary_key(entries)
    html_output_path, found_entries_by_primary_key = process_template("guide.template.html",
                                                    entries_by_primary_key)
    print(f"Found {len(found_entries_by_primary_key)} entries.")
    print(f"Output to {html_output_path}")

    vocabulary_output_filename = "guide_vocabulary.tsv"
    file_io.tsv_from_entries(found_entries_by_primary_key.values(),
                             vocabulary_output_filename)
    print(f"Output to {vocabulary_output_filename}")
