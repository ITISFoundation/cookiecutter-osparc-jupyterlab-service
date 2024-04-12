import subprocess

from pytest_cookies.plugin import Result
import pytest

from test_bake_project import baked_project

@pytest.mark.parametrize(
    "commands_on_baked_project",
    (
        "make build",
    ),
)
def test_make_workflows(baked_project: Result, commands_on_baked_project: str):
    working_dir = baked_project.project_path
    subprocess.run(
        ["/bin/bash", "-c", commands_on_baked_project], cwd=working_dir, check=True
    )