from pathlib import Path
import subprocess

from utils.logger import setup_logger
from utils.git_utils import fetch_updates, get_commit, update_branch
from utils.commands import run_commands


def update_project(project: dict, override_branch: str = None):
    name = project.get("name", "project")
    repo_path = Path(project["path"])
    branch = override_branch or project.get("branch", "recette")
    commands = project.get("commands", [])

    setup_logger(name)

    if not repo_path.exists():
        print(f"[ERROR] Path does not exist: {repo_path}\n")
        return

    print(f"[INFO] Updating {repo_path} on branch {branch}")

    try:
        fetch_updates(repo_path)
        local_commit = get_commit(repo_path, branch)
        remote_commit = get_commit(repo_path, f"origin/{branch}")

        if local_commit != remote_commit:
            print(f"[INFO] Branch {branch} is outdated, pulling changes...")
            update_branch(repo_path, branch)
            print(f"[INFO] {repo_path} updated successfully.\n")
            run_commands(commands)
        else:
            print(f"[INFO] Branch {branch} is up to date.\n")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Operation failed for {repo_path}: {e}\n")
