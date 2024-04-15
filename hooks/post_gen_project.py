#
# When the hook scripts script are run, their current working directory is the root of the generated project
#
# SEE https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html

import shutil
import sys
from pathlib import Path
import os
from contextlib import contextmanager


SELECTED_DOCKER_BASE = "{{ cookiecutter.docker_base }}"
SELECTED_GIT_REPO = "{{ cookiecutter.git_repo }}"


def create_ignore_listings():
    # .gitignore
    common_gitignore = Path("Common.gitignore")
    python_gitignore = Path("Python.gitignore")

    gitignore_file = Path(".gitignore")
    gitignore_file.unlink(missing_ok=True)
    shutil.copyfile(common_gitignore, gitignore_file)

    if "python" in SELECTED_DOCKER_BASE:
        with gitignore_file.open("at") as fh:
            fh.write("\n")
            fh.write(python_gitignore.read_text())

    common_gitignore.unlink()
    python_gitignore.unlink()


def remove_repo_folder():
    if SELECTED_GIT_REPO != "github":
        shutil.rmtree(".github")
    if SELECTED_GIT_REPO != "gitlab":
        shutil.rmtree(".gitlab")


def remove_requirements_folders():
    if "python" not in SELECTED_DOCKER_BASE:
        shutil.rmtree("env-config/python")
    if "r-notebook" not in SELECTED_DOCKER_BASE:
        shutil.rmtree("env-config/r")
    if "julia" not in SELECTED_DOCKER_BASE:
        shutil.rmtree("env-config/julia")


@contextmanager
def context_print(
    msg,
):
    print("-", msg, end="...", flush=True)
    yield
    print("DONE")


def main():
    print("Starting post-gen-project hook:", flush=True)
    try:
        with context_print("Updating .gitignore and .dockerignore configs"):
            create_ignore_listings()

        with context_print("Adding config for selected external repository"):
            remove_repo_folder()

        with context_print("Creating dependencies files based on selection"):
            remove_requirements_folders()

    except Exception as exc:  # pylint: disable=broad-except
        print("ERROR", exc)
        return os.EX_SOFTWARE
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
