# 🛠️ Auto Git Updater

This script automatically updates your local Git repositories, runs optional commands, and saves daily logs for each project.

````yaml
projects:
  - name: "project1"
    path: "/path/to/project1"
    branch: "recette"
    commands:
      - "echo 'Project1 updated'"
      - "systemctl restart myservice1"

  - name: "project2"
    path: "/path/to/project2"
    branch: "develop"
    commands:
      - "echo 'Deploying project2'"
      - "/path/to/project2/scripts/deploy.sh"
````
Fields:

- name → Project name (used for log folders)
- path → Local repository path
- branch → Branch to update
- commands → Optional commands after update

# 🚀 How to use
### Install dependencies
````shell
pip install pyyaml
````

### Run manually
````shell
python3 update_repos.py
````

### Or override branch for all projects:
````shell
python3 update_repos.py --branch develop
````

# ⏲️ Automate with Cron
````shell
crontab -e
````

````shell
0 * * * * /usr/bin/python3 /path/to/update_repos/update_repos.py
````