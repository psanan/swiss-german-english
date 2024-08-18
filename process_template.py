#!/usr/bin/env python

import file_io

def process_template(path, entries_by_id, entries_by_ch):
    found_entries_by_id = {}
    with open(path, "r") as template_file:
        for line in template_file:
            line_stripped = line.strip()
            if line_stripped.startswith("<li>"):
                potential = line_stripped.removeprefix("<li>").strip()
                if potential.isdigit():
                    id = int(potential)
                    if id in entries_by_id:
                        entry = entries_by_id[id]
                        print("Found entry by id: ", id, entry)
                        found_entries_by_id[id] = entry
                        continue
                elif potential in entries_by_ch:
                    entry = entries_by_ch[potential]
                    print("Found entry by ch: ", potential, entry)
                    found_entries_by_id[entry.id] = entry
                    continue
                print("WARNING: didn't find entry for ", potential)
    return found_entries_by_id

if __name__ == "__main__":
    entries_by_id, entries_by_ch = file_io.load_yaml("translations.yaml")
    print(entries_by_id)
    print()
    print(entries_by_ch)
    found_entries_by_id = process_template("guide.template.html", entries_by_id, entries_by_ch)
    print("FOUND:")
    print(found_entries_by_id)
