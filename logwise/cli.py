import argparse

from logwise.parser import parse_file
from logwise.filters import filter_by_date, filter_by_keyword, filter_by_level
from logwise.output import print_results, print_summary

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="logwise",
        description="A command-line log analysis tool for engineers",
        epilog="Example: logwise app.log --level ERROR --keyword 'connection refused'"
    )

    parser.add_argument(
        'filepath',
        help="Path to the log file"
    )

    parser.add_argument(
        "--level",
        help="Filter by log level e.g. ERROR, WARN, INFO, DEBUG",
        type=str
    )

    parser.add_argument(
        "--keyword",
        help="Filter by keyword in the message",
        type=str
    )

    parser.add_argument(
        "--since",
        help="Show entries from this date (YYYY-MM-DD)",
        type=str
    )

    parser.add_argument(
        "--until",
        help="Show entries until this date (YYYY-MM-DD)",
        type=str
    )

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    entries = parse_file(args.filepath)
    total = len(entries)

    if args.level:
        entries = filter_by_level(entries, args.level)
    if args.keyword:
        entries = filter_by_keyword(entries, args.keyword)
    if args.since or args.until:
        entries = filter_by_date(entries, args.since, args.until)

    print_results(entries)
    print_summary(total, len(entries))


if __name__ == "__main__":
    main()