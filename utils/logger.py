import sys
from pathlib import Path
from datetime import datetime


class Logger:
    def __init__(self, file):
        self.terminal = sys.stdout
        self.log = open(file, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


def setup_logger(project_name: str) -> None:
    """Create a logger per project and per day."""
    logs_root = Path("../logs") / project_name
    logs_root.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = logs_root / f"{today}.log"
    sys.stdout = Logger(log_file)
