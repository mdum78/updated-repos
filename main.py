import yaml
import argparse
from utils.updater import update_project


def main():
    parser = argparse.ArgumentParser(description="Update local git repositories")
    parser.add_argument("--branch", help="Override branch for all projects")
    args = parser.parse_args()

    with open("projects.yml", "r") as file:
        config = yaml.safe_load(file)

    for project in config.get("projects", []):
        update_project(project, override_branch=args.branch)


if __name__ == "__main__":
    main()
