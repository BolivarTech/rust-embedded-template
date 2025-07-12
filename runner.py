#!/usr/bin/env python3
import os
import subprocess
import sys

chip = "STM32G431R8"

def run_command(path=None):
    commands = [
        ["cargo", "clean"],
        ["probe-rs", "erase", "--chip", chip],
        ["cargo", "build", "--profile", "gdb"],
        ["probe-rs", "download", "--chip", chip, path]
    ]

    for cmd in commands:
        result = subprocess.run(cmd)
        if result.returncode != 0:
            sys.exit(result.returncode)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = "." + os.path.sep + sys.argv[1]
        run_command(path)
        #print("Running commands with path:", path)
    else:
        print("Usage: runner.py <path_to_elf>")
    sys.exit(0)