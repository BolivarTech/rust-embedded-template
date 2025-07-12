#!/usr/bin/env python3

"""
flasher.py

Automates building, erasing, and flashing firmware to a microcontroller using Cargo and probe-rs.

Usage:
    python flasher.py [-c CHIP] <path_to_elf>

Arguments:
    -c, --chip      Specify the chip type (default: STM32G431R8)
    path_to_elf     Path to the ELF binary to be flashed

This script:
    - Cleans the Cargo project
    - Erases the microcontroller flash
    - Builds the firmware with the 'gdb' profile
    - Downloads the firmware to the microcontroller

Dependencies:
    - Python 3.x
    - cargo
    - probe-rs

Author: Julian Bolivar
Date: 2025-07-12
Version: 1.0.0
"""

import os
import subprocess
import sys
from argparse import ArgumentParser

def build_argparser():
    """
    Parse command line arguments.

    :return: command line arguments
    """
    parser = ArgumentParser(
        description="Automate building, erasing, and flashing firmware to an microcontroller using Cargo and probe-rs."
    )
    parser.add_argument("-c", "--chip", required=False, type=str, default="STM32G431R8",
                        help="Specify the chip type. (default: STM32G431R8)")
    parser.add_argument("path_elf", nargs='?', type=str, default=None,
                        help="Path to the ELF binary to be flashed. If not provided, usage instructions will be displayed.")
    return parser


def run_command(args_parser):
    """
    Executes the build, erase, and flash commands using the provided argument parser.

    Args:
        args_parser (ArgumentParser): The argument parser containing user-supplied arguments.

    Exits:
        The script exits with a non-zero code if any command fails or if required arguments are missing.
    """
    args = args_parser.parse_args()
    if args.path_elf is None:
        print("Error: <path_elf> argument is required.\n")
        args_parser.print_help()
        sys.exit(1)
    path = os.path.join(".", args.path_elf)
    chip = args.chip
    print(f"Flashing {path} to {chip}")
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

    args_parser = build_argparser()
    run_command(args_parser)
    sys.exit(0)