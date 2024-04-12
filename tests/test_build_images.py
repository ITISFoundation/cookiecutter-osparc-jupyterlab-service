import subprocess
import pytest
import os
from pytest_cookies.plugin import Result

# @pytest.mark.parametrize(
#     "commands_on_baked_project",
#     (
#         "make build",
#     ),
# )
def test_build_image(baked_project: Result):
    working_dir = baked_project.project_path
    # subprocess.run(
    #     ["/bin/bash", "-c", commands_on_baked_project], cwd=working_dir, check=True
    # )
    os.chdir(str(working_dir))
    
    build_command = subprocess.run(["/bin/bash", "-c", "make build"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, cwd=working_dir)
    print(build_command.stderr)
    print(build_command.stdout)

