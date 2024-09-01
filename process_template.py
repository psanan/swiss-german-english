#!/usr/bin/env python

import file_io

# FIXME duplicated helper
def _entry_field_as_list(entry, field):
    if not isinstance(entry, dict):
        print(type(entry))
        raise RuntimeError()
    field = entry[field]
    return field if isinstance(field, list) else [field]

def _entry_to_html(entry):
    # TODO make prettier
    entry_ch = _entry_field_as_list(entry, "ch")[0]
    if "en" in entry:
        entry_en = _entry_field_as_list(entry, "en")[0]
    else:
        entry_en = ""
    return f"<li> <b>{entry_ch}</b> : {entry_en}"

def process_template(path, entries_by_ch):
    found_entries_by_ch = {}
    lines_out = []
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
                    lines_out.append(_entry_to_html(entry))
                else:
                    print("WARNING: didn't find entry for ", ch_potential)
                    lines_out.append(line)
            else:
                    lines_out.append(line)
    out_path = path + ".out.html"
    with open(out_path, "w") as out_file:
        for line in lines_out:
            out_file.write(line)
    return found_entries_by_ch


if __name__ == "__main__":
    entries = file_io.entries_from_yaml("translations.yaml")
    entries_by_ch = file_io.entries_by_ch(entries)
    print(entries_by_ch)
    found_entries_by_ch = process_template("guide.template.html", entries_by_ch)
    print("FOUND:")
    print(found_entries_by_ch)

    output_filename = "guide_vocabulary.yaml"
    file_io.yaml_from_entries(found_entries_by_ch.values(), output_filename)
