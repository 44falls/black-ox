#!/usr/bin/env python3

import yaml
import os
from objs import main

file_path = os.path.realpath(__file__)
cur_dir = os.path.dirname(file_path)

target_dir = os.path.join(cur_dir, "target")

config_file = os.path.join(cur_dir, "config", "config.yml")

with open(config_file, "r") as config:
    cfg = yaml.safe_load(config)


def main():
    pass


if __name__ == "__main__":
    main()
