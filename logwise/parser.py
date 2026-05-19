from dataclasses import dataclass
from datetime import datetime
import re


LOG_PATTERN = re.compile(
    r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)$'
)

@dataclass
class LogEntry:
    timestamp: datetime | None
    level: str | None
    message: str
    raw: str # actual log line 

def parse_line(line: str) -> LogEntry:
    line = line.strip()
    match = LOG_PATTERN.match(line)

    if match:
        raw_timestamp, level, message = match.groups()
        timestamp = datetime.strptime(raw_timestamp, "%Y-%m-%d %H:%M:%S")

        return LogEntry(
            timestamp=timestamp,
            level=level,
            message=message,
            raw=line
        )
    return LogEntry(
        timestamp=None,
        level=None,
        message=line,
        raw=line
    )

def parse_file(filepath: str) -> list[LogEntry]:
    entries = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                if line.strip():
                    entries.append(parse_line(line))
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file not found - {filepath}")
    except PermissionError:
        raise PermissionError(f"Error: permission denied: {filepath}")

    return entries