#!/usr/bin/env python

import file_io

def process_template(path, entries_by_ch):
    # TODO: add a printer for entries and build the filled-in version of the template
    found_entries_by_ch = {}
    with open(path, "r") as template_file:
        for line in template_file:
            line_stripped = line.strip()
            if line_stripped.startswith("<li>"):
                ch_potential = line_stripped.removeprefix("<li>").strip()
                if ch_potential in entries_by_ch:
                    ch = ch_potential
                    entry = entries_by_ch[ch]
                    print("Found entry by ch: ", ch, entry)
                    found_entries_by_ch[ch] = entry
                else:
                    print("WARNING: didn't find entry for ", ch_potential)
    return found_entries_by_ch

if __name__ == "__main__":
    entries = file_io.entries_from_yaml("translations.yaml")
    entries_by_ch = file_io.entries_by_ch(entries)
    print(entries_by_ch)
    found_entries_by_ch = process_template("guide.template.html", entries_by_ch)
    print("FOUND:")
    print(found_entries_by_ch)
