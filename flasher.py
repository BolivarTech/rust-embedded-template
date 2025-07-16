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
    path_hex = os.path.join(".", args.path_elf + ".hex")
    path_bin = os.path.join(".", args.path_elf + ".bin")
    path_elf = os.path.join(".", args.path_elf if args.path_elf.endswith(".elf") else args.path_elf + ".elf")
    #os.rename(args.path_elf, path_elf)
    chip = args.chip
    print(f"Flashing {path_elf} to {chip}")
    commands = [
        ["cargo", "clean"],
        ["probe-rs", "erase", "--chip", chip],
        ["cargo", "build", "--profile", "gdb"],
        ["arm-none-eabi-objcopy", "-O", "ihex", path_elf, path_hex],
        ["arm-none-eabi-objcopy", "-O", "binary", path_elf, path_bin],
        ["probe-rs", "download", "--chip", chip, path_elf]
    ]
    probe_test = ["probe-rs", "list"]
    result = subprocess.run(probe_test, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    probe_detected = True
    if result.returncode != 0 or "No debug probes were found" in result.stdout.decode():
        print("No debug probes were found")
        probe_detected = False
    for cmd in commands:
        if not probe_detected and cmd[0] == "probe-rs":
            print(f"Skipping command: {' '.join(cmd)} as no debug probe was detected.")
            continue
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f"Error executing command: {' '.join(cmd)}")
            sys.exit(result.returncode)
        else:
            if cmd[0] == "cargo" and cmd[1] == "build":
                os.rename(path, path_elf)
    print(f"Flashing was successfully to {chip}")


if __name__ == "__main__":

    args_parser = build_argparser()
    run_command(args_parser)
    sys.exit(0)
