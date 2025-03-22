#!/usr/bin/env python3

import file_io

STYLES = [["<b>", "</b>"], ["<i>", "</i>"], ["", ""]]


def _entry_to_html(entry):
    style = 0
    html_to_join = ["<li>"]
    for key in file_io.KEYS:
        sub_html_to_join = []
        for string in entry[key]:
            sub_html_to_join.append(
                f"{STYLES[style][0]}{string}{STYLES[style][1]}")
        html_to_join.append(
            " <font color='grey'>|</font> ".join(sub_html_to_join))
        html_to_join.append("&nbsp;&nbsp;")
        style += 1
    html_to_join.append("</li>")
    return "".join(html_to_join)


def process_template(path, entries_by_primary_key):
    found_entries_by_primary_key = {}
    lines_out = ["<!-- DO NOT EDIT. This file is generated from a template -->\n"]
    with open(path, "r") as template_file:
        for line in template_file:
            line_stripped = line.strip()
            if line_stripped.startswith("<li>"):
                primary_key_potential = line_stripped.removeprefix(
                    "<li>").strip()
                if primary_key_potential in entries_by_primary_key:
                    primary_key = primary_key_potential
                    entry = entries_by_primary_key[primary_key]
                    found_entries_by_primary_key[primary_key] = entry
                    lines_out.append(_entry_to_html(entry))
                else:
                    print("WARNING: didn't find entry for primary key:",
                          primary_key_potential)
                    lines_out.append(f'<font color="red">{line}</font>')
            else:
                lines_out.append(line)
    out_path = path + ".out.html"
    with open(out_path, "w") as out_file:
        for line in lines_out:
            out_file.write(line)
    return found_entries_by_primary_key


if __name__ == "__main__":
    entries = file_io.entries_from_tsv("translations.tsv")
    entries_by_primary_key = file_io.entries_by_primary_key(entries)
    found_entries_by_primary_key = process_template("guide.template.html",
                                                    entries_by_primary_key)
    print(f"Found {len(entries_by_primary_key)} entries.")

    output_filename = "guide_vocabulary.tsv"
    file_io.tsv_from_entries(found_entries_by_primary_key.values(),
                             output_filename)
    print(f"Output to {output_filename}")
