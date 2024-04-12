import json

import sys
from pathlib import Path

import pytest
from pytest_cookies.plugin import Cookies, Result

current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent
repo_basedir =current_dir.parent
cookiecutter_json = repo_basedir / "cookiecutter.json"

@pytest.fixture(
    params=json.loads(cookiecutter_json.read_text())["docker_base"]
)
def baked_project(cookies: Cookies, request) -> Result:
    result = cookies.bake(
        extra_context={
            "project_slug": "DummyProject",
            "project_name": "dummy-project",
            "default_docker_registry": "test.test.com",
            "docker_base": request.param,
        }
    )

    assert result.exception is None
    assert result.exit_code == 0
    return result