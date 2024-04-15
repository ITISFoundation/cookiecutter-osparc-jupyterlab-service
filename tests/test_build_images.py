import os
import subprocess
from pathlib import Path
from pytest_cookies.plugin import Result


def test_build_image(baked_project: Result):
    working_dir = baked_project.project_path
    assert working_dir is not None
    os.chdir(str(working_dir))

    # Build baked images, except custom (doesn't produce a valid Dockerfile by design)
    dockerfile = Path.joinpath(working_dir, "Dockerfile")
    with open(dockerfile, "r") as fp:
        content = fp.read()
        if "custom:special-image" not in content:
            subprocess.run(
                ["/bin/bash", "-c", "make build"],
                shell=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                cwd=working_dir,
            )
