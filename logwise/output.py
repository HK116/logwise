from logwise.parser import LogEntry

COLOURS = {
    "ERROR":    "\033[31m",
    "INFO":     "\033[32m",
    "WARN":     "\033[33m",
    "WARINING": "\033[33m",
    "DEBUG":    "\033[34m",
    "FRAMING":  "\033[36m",
    "RESET":    "\033[0m",
    "BOLD":     "\033[1m",
}

def colourise(level: str | None) -> str:
    if level is None:
        return COLOURS["RESET"]
    return COLOURS.get(level.upper(), COLOURS["RESET"])

def format_entry(entry: LogEntry) -> str:
    colour = colourise(entry.level)
    reset = COLOURS["RESET"]
    bold = COLOURS["BOLD"]

    if entry.timestamp is None:
        return f"{colour}??:??:?? {'UNKNOWN':<8}{reset} {entry.message}"
    
    time_str = entry.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    level_str = (entry.level or "UNKNOWN").ljust(8)

    return f"{colour}{bold}{time_str} {level_str}{reset} {entry.message}"

def print_results(entries: list[LogEntry]) -> None:
    if not entries:
        print(f"{COLOURS['WARN']}No matching log entries found.{COLOURS['RESET']}")
        return
    
    print()
    for entry in entries:
        print(format_entry(entry))
    print()


def print_summary(total: int, filtered: int) -> None:
    bold = COLOURS['BOLD']
    reset = COLOURS['RESET']

    print(f"{bold}-- Summary -------------------------------{reset}")
    print(f"   Total lines parsed : {total}")
    print(f"   Matching entries   : {filtered}")
    print(f"{bold}------------------------------------------{reset}")
