#!/usr/bin/env python

import yaml

# For now an entry is not a proper class, just a dict expected to have entries for
# each language, either a single string or a list of strings.

def _entry_field_as_list(entry, field):
    if not isinstance(entry, dict):
        print(type(entry))
        raise RuntimeError()
    field = entry[field]
    return field if isinstance(field, list) else [field]

def validate_entry(entry):
    if entry is None:
        return False, "entry is None (trailing ---?)"
    if "ch" not in entry:
        return False, "All entries require ch"
    return True, None

def validate_entries(entries):
    chs = set()
    for entry in entries:
        valid, status = validate_entry(entry)
        if not valid:
            # It might be more convenient to print out all invalid entries first.
            return False, f"Invalid entry: {entry}: {status}"
        for entry_ch in _entry_field_as_list(entry, "ch"):
            if entry_ch in chs:
                return False, f"Duplicate ch: {ch}"
            chs.add(entry_ch)

def entries_from_yaml(path):
    entries = []
    with open(path, "r") as yaml_file:
        for entry in yaml.safe_load_all(yaml_file):
            entries.append(entry)
    return entries


def entries_by_ch(entries):
    """Requires validated entries list (no duplicates)"""
    entries_by_ch = {}
    for entry in entries:
        for entry_ch in _entry_field_as_list(entry, "ch"):
            entries_by_ch[entry_ch] = entry
    return entries_by_ch


if __name__ == "__main__":
    entries = entries_from_yaml("translations.yaml")
    validate_entries(entries)
    print(entries_by_ch(entries))
