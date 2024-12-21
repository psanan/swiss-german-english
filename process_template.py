#!/usr/bin/env python3

import file_io

STYLES=[["<b>", "</b>"],["<i>","</i>"], ["",""]]

def _entry_to_html(entry):
    style = 0
    html_to_join = ["<li>"]
    for key in file_io.KEYS:
        sub_html_to_join = []
        for string in entry[key]:
            sub_html_to_join.append(f"{STYLES[style][0]}{string}{STYLES[style][1]}")
        html_to_join.append(" | ".join(sub_html_to_join))
        html_to_join.append("&nbsp;&nbsp;")
        style += 1
    html_to_join.append("</li>")
    return "".join(html_to_join)

def process_template(path, entries_by_primary_key):
    found_entries_by_primary_key = {}
    lines_out = []
    with open(path, "r") as template_file:
        for line in template_file:
            line_stripped = line.strip()
            if line_stripped.startswith("<li>"):
                ch_potential = line_stripped.removeprefix("<li>").strip()
                if ch_potential in entries_by_primary_key:
                    ch = ch_potential
                    entry = entries_by_primary_key[ch]
                    print("Found entry by ch: ", ch, entry)
                    found_entries_by_primary_key[ch] = entry
                    lines_out.append(_entry_to_html(entry))
                else:
                    print("WARNING: didn't find entry for ", ch_potential)
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
    print(entries_by_primary_key)
    found_entries_by_primary_key = process_template("guide.template.html", entries_by_primary_key)
    print("entries by ch")
    entries_by_primary_key
    print("FOUND:")
    print(found_entries_by_primary_key)

    output_filename = "guide_vocabulary.tsv"
    file_io.tsv_from_entries(found_entries_by_primary_key.values(), output_filename)
