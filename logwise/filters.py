from datetime import datetime
from logwise.parser import LogEntry

def filter_by_level(entries: list[LogEntry], level: str) -> list[LogEntry]:
    return [
        entry for entry in entries
        if entry.level and entry.level.upper() == level.upper() 
    ]

def filter_by_keyword(entries: list[LogEntry], keyword: str) -> list[LogEntry]:
    return [
        entry for entry in entries
        if entry.message and keyword.lower() in entry.message.lower()
    ]
    
def filter_by_date(
    entries: list[LogEntry], since: str | None = None, until: str | None = None
) -> list[LogEntry]:
    since_dt = datetime.strptime(since, "%Y-%m-%d") if since else None
    until_dt = datetime.strptime(until, "%Y-%m-%d").replace(
        hour=23, minute=59, second=59
    ) if until else None

    return [
        entry for entry in entries
        if entry.timestamp and
        (since_dt is None or entry.timestamp >= since_dt) and
        (until_dt is None or entry.timestamp <= until_dt)
    ]