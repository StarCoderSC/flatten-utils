import argparse
import json
import sys
from .core import flatten_list, flatten_limited, deep_flatten

def main():
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

    args = parser.parse_args()

    # Determine which input to use
    input_str = args.json_input or args.pos_input
    if not input_str:
        print("❌ Invalid input! Provide JSON string as argument or --json flag.")
        sys.exit(1)

    # Try to load JSON input
    try:
        data = json.loads(input_str)
    except json.JSONDecodeError:
        print("❌ Invalid JSON input!")
        sys.exit(1)

    # Stop flattening at these types
    stop_at_types = tuple(eval(t) for t in args.stop_at) if args.stop_at else (str, bytes)

    # Choose flatten strategy
    if args.depth is not None:
        result = list(flatten_limited(data, depth=args.depth, stop_at=stop_at_types))
    else:
        result = list(deep_flatten(data, stop_at=stop_at_types))

    # Output result
    print(json.dumps(result, indent=2))




