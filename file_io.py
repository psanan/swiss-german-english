#!/usr/bin/env python

import yaml


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def load_yaml(path):
    entries_by_ch = {}
    with open(path, "r") as yaml_file:
        for document in yaml.safe_load_all(yaml_file):
            if document is None:
                print("Warning: skipping empty document (trailing --- ?)")
                continue
            entry = dotdict(document)
            if "ch" not in entry:
                print("Warning: entry missing required ch field")
                continue
            if not isinstance(entry.ch, list):
              chs = [entry.ch]
            else:
              chs = entry.ch
            for ch in chs:
                if ch in entries_by_ch:
                    print("ERROR duplicate ch ", ch)
                else:
                    entries_by_ch[ch] = entry
    return entries_by_ch




if __name__ == "__main__":
    print(load_yaml("translations.yaml"))
