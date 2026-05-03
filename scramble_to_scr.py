#!/usr/bin/env python3
"""
Convert a 5x5 scramble into a twsearch .scr file for first-center solving.

Uses twsearch's --showpositions flag to get the CENTER2/CENTER3 state
after applying a scramble, then formats it into a .scr file.

Usage:
    python3 scramble_to_scr.py "F' R D' Bw B' ..."
    python3 scramble_to_scr.py "F' R D' Bw B' ..." -o output.scr
    python3 scramble_to_scr.py   (interactive mode, prompts for scramble)
"""

import subprocess
import argparse
import sys
import os

# ---- CONFIG: adjust these paths to match your setup ----
TWSEARCH_BIN = os.path.expanduser("~/twips/build/bin/twsearch")
TWS_FILE = os.path.expanduser("~/twips/samples/main/5x5FirstCenter.tws")
# ---------------------------------------------------------

ZEROS_LINE = "0 " * 24
ZEROS_LINE = ZEROS_LINE.strip()


def get_center_state(scramble: str) -> dict[str, str]:
    """Run twsearch --showpositions and parse CENTER2/CENTER3 lines."""
    result = subprocess.run(
        [TWSEARCH_BIN, "--showpositions", TWS_FILE],
        input=scramble,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("twsearch error:", result.stderr, file=sys.stderr)
        sys.exit(1)

    output = result.stdout
    centers = {}
    lines = output.splitlines()

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped in ("CENTER2", "CENTER3"):
            # The next line has the piece values
            values = lines[i + 1].strip()
            centers[stripped] = values

    if "CENTER2" not in centers or "CENTER3" not in centers:
        print("Could not find CENTER2/CENTER3 in twsearch output.", file=sys.stderr)
        print("Full output:", file=sys.stderr)
        print(output, file=sys.stderr)
        sys.exit(1)

    return centers


def format_scr(centers: dict[str, str], name: str = "FirstCenterScramble") -> str:
    """Format the parsed center state into a .scr file."""
    lines = [
        f"Scramble {name}",
        "CENTER2",
        centers["CENTER2"],
        ZEROS_LINE,
        "CENTER3",
        centers["CENTER3"],
        ZEROS_LINE,
        "End",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Convert a 5x5 scramble to a twsearch .scr file."
    )
    parser.add_argument("scramble", nargs="?", help="The scramble algorithm string")
    parser.add_argument("-o", "--output", help="Output .scr file path (default: stdout)")
    parser.add_argument(
        "-n", "--name", default="FirstCenterScramble",
        help="Scramble name in the .scr file (default: FirstCenterScramble)",
    )
    args = parser.parse_args()

    scramble = args.scramble
    if not scramble:
        scramble = input("Enter scramble: ").strip()

    if not scramble:
        print("No scramble provided.", file=sys.stderr)
        sys.exit(1)

    centers = get_center_state(scramble)
    scr_content = format_scr(centers, args.name)

    if args.output:
        with open(args.output, "w") as f:
            f.write(scr_content)
        print(f"Written to {args.output}")
    else:
        print(scr_content)


if __name__ == "__main__":
    main()
