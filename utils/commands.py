import subprocess


def run_commands(commands: list):
    """Run a list of shell commands after project update."""
    for cmd in commands:
        print(f"[INFO] Executing: {cmd}")
        subprocess.run(cmd, shell=True, check=True)
