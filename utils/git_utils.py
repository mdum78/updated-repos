import subprocess
from pathlib import Path


def fetch_updates(repo_path: Path):
    subprocess.run(["git", "-C", str(repo_path), "fetch"], check=True)


def get_commit(repo_path: Path, ref: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo_path), "rev-parse", ref]
    ).decode().strip()


def update_branch(repo_path: Path, branch: str):
    subprocess.run(["git", "-C", str(repo_path), "checkout", branch], check=True)
    subprocess.run(["git", "-C", str(repo_path), "pull", "origin", branch], check=True)
