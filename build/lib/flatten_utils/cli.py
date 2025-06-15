"""
cli.py

Command-line interface for flatten_utils

Allows users to flattem deeply nested Python data structures (like lists, dicts, sets, etc.)
from the command line using JSON input.

Supports:
- Unlimited or depth-limitd flattening
- Stopping flatten at specific types
- Input via file, direct string, or named
-- json falg

"""


import argparse
import json
import sys
try:
    from .core import flatten_list, flatten_limited, deep_flatten
except ImportError:
    from flatten_utils.core import flatten_list, flatten_limited, deep_flatten

def main():
    """
    
    Entry point for the flatten_utils CLI.

    Parsed command_line arguments, reads input (JSON string or file),
    optionally applies depth-limited flattening, and prints the flattened result.

    """

    parser = argparse.ArgumentParser(
        description="Flatten nested structures (lists, sets, dicts, etc.)"
    )

    parser.add_argument(
        "pos_input",
        nargs="?",
        help="JSON string input (positional or use --json)"
    )
    parser.add_argument(
        "--json",
        dest="json_input",
        help="JSON string input (optional named flag)"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Path to a JSON file (takes priority over --json or positional input)"
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=None,
        help="Limit flatten depth (optional)"
    )
    parser.add_argument(
        "--stop_at",
        nargs='*',
        help="Types to stop flattening at (e.g. str bytes)"
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the output JSON"
    )

    args = parser.parse_args()

    input_str = None
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                input_str = f.read()
        except Exception as e:
            print(f"Failed to read the '{args.file}': {e}")
            sys.exit(1)
        if args.json_input or args.pos_input:
            print("Warning: --file overrides --json and positional input.")
        
    else:
        input_str = args.json_input or args.pos_input
    
    if not input_str:
        print("Invalid input! Provide JSON via file, --json or positional argument.")
        sys.exit(1)
    
    try:
        data = json.loads(input_str)
    except json.JSONDecodeError:
        print("Invalid JSON input!")
        sys.exit(1)

    try:
        stop_at_types = tuple(eval(t) for t in args.stop_at) if args.stop_at else (str, bytes)
    except Exception as e:
        print(f"Invalid types(s) in --stop_at: {e}")
        sys.exit(1)

    try:
        if args.depth is not None:
            result = list(flatten_limited(data, depth=args.depth, stop_at=stop_at_types))
        else:
            result = list(deep_flatten(data, stop_at=stop_at_types))
        
        output = json.dumps(result, indent=2 if args.pretty else None)
        print(output)

    except Exception as e:
        print(f"Unexpected error during flattening: {e}")
        sys.exit(1)

if __name__=="__main__":
    main()
