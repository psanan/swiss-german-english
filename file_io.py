#!/usr/bin/env python

import yaml


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def load_yaml(path):
    raw_data = []
    with open(path, "r") as yaml_file:
        for document in yaml.safe_load_all(yaml_file):
            if document is None:
                print("Warning: skipping empty document (trailing --- ?)")
                continue
            raw_data.append(dotdict(document))

    print(raw_data)
    print(raw_data[0].id)


if __name__ == "__main__":
    load_yaml("translations.yaml")
