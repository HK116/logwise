# logwise

A fast, lightweight command-line log analysis tool for engineers.
No dependencies. Just Python.

![logwise demo](https://github.com/HK116/logwise/raw/main/docs/demo.png)

---

## The Problem

When something breaks in production, you're staring at thousands of log lines
trying to find the ones that matter. Grepping works, but it's clunky, colourless,
and gives you no summary of what you're looking at.

logwise lets you filter by level, keyword, and date range — and shows you exactly
what you need, cleanly formatted, with colour.

---

## Who Is This For

Anyone who works with log files — developers, DevOps engineers, sysadmins.
If you've ever run `cat app.log | grep ERROR` and wished it did more, this is for you.

---

## Installation

Requires Python 3.10+. No external packages needed.

```bash
git clone git@github.com:HK116/logwise.git
cd logwise
# python3 -m venv .venv
# source .venv/bin/activate
```

---

## Usage

```bash
python3 -m logwise <path-to-log-file> [options]
```

### Filter by log level

```bash
python3 -m logwise app.log --level ERROR
```

### Filter by keyword

```bash
python3 -m logwise app.log --keyword "connection refused"
```

### Filter by date range

```bash
python3 -m logwise app.log --since 2024-01-01 --until 2024-01-31
```

### Chain multiple filters

```bash
python3 -m logwise app.log --level ERROR --keyword "connection" --since 2024-01-15
```

### All options

![logwise help](https://github.com/HK116/logwise/raw/main/docs/help.png)

---

## How It Works

logwise is built in four focused layers — each with a single responsibility:

cli.py       →  reads and validates terminal arguments
parser.py    →  reads the log file, extracts timestamp, level and message
filters.py   →  applies level, keyword and date filters sequentially
output.py    →  colourises and formats results to the terminal

Log lines that don't match the expected format are handled gracefully —
they're never silently dropped, and they never crash the tool.

---

## Supported Log Format

YYYY-MM-DD HH:MM:SS LEVEL message

Example:
2024-01-15 09:02:33 ERROR Connection refused: could not reach auth service

---

## Roadmap

- [ ] Support multiple log formats (JSON, Apache, syslog)
- [ ] Export filtered results to a file (`--output results.txt`)
- [ ] Summary statistics — error frequency, busiest time windows
- [ ] Live log tailing (`--follow`)
- [ ] Pattern detection — spike alerts over a time window

---

## Author

Henok Urufa — [github.com/HK116](https://github.com/HK116)