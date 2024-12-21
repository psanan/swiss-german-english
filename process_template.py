#!/usr/bin/env python3

import file_io

def _entry_to_html(entry):
    # TODO make prettier, remove hard-coding, and include multiples
    entry_ch = entry['ch'][0]
    entry_en = entry["en"][0] if "en" in entry else ""
    entry_de = entry['de'][0] if "de" in entry else ""
    return f"<li> <b>{entry_ch}</b> <i>{entry_de}</i> {entry_en}"

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
