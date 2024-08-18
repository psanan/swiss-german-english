#!/usr/bin/env python

import yaml


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def load_yaml(path):
    entries_by_id = {}
    entries_by_ch = {}
    with open(path, "r") as yaml_file:
        for document in yaml.safe_load_all(yaml_file):
            if document is None:
                print("Warning: skipping empty document (trailing --- ?)")
                continue
            entry = dotdict(document)
            if "id" in entry:
                if entry.id in entries_by_id:
                    print("ERROR duplicate id ", entry.id)
                else:
                    entries_by_id[entry.id] = entry
            if "ch" in entry:
                if not isinstance(entry.ch, list):
                  entries_ch = [entry.ch]
                else:
                  entries_ch = entry.ch
                for entry_ch in entries_ch:
                    if entry_ch in entries_by_ch:
                        print("ERROR duplicate ch ", entry.ch)
                    else:
                        entries_by_ch[entry_ch] = entry
    return entries_by_id, entries_by_ch




if __name__ == "__main__":
    print(load_yaml("translations.yaml"))
