# Cookiecutter For o²S²PARC Jupyter Services

Status: ![Build Status](https://github.com/ITISFoundation/cookiecutter-osparc-jupyterlab-service/workflows/Github-CI%20Push/PR/badge.svg)

Template library to generate an [o²S²PARC compatible interactive service with the JupyterLab environment](https://docs.osparc.io/#/docs/study_setup/JupyterLabs?id=jupyterlab). 
In addition to the different JupyterLab "flavours" offered on o²S²PARC, you can use this library to create one with your favourite software and tools. 
As a basis, we recommend to start from the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/). 


## Requirements
- GNU Make
- Python3
- Python3-venv (recommended to work in a virtual environment)
- [``cookiecutter``](https://python-package-generator.readthedocs.io/en/master/)

```console
sudo apt-get update
sudo apt-get install -y make python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install cookiecutter
```

## Usage

Generate a new Cookiecutter template layout:
```console
python3 -m venv .venv
source .venv/bin/activate
cookiecutter gh:ITISFoundation/cookiecutter-osparc-jupyterlab-service
```

## Information for the developers of this cookiecutter

### Get the code and run the cookiecutter
```console
git clone https://github.com/ITISFoundation/cookiecutter-osparc-jupyterlab-service.git
cd cookiecutter-osparc-jupyterlab-service
make devenv
source .venv/bin/activate
make play
```

### Run the tests
This will create different projects based on different docker image bases, specified in [cookiecutter.json](/cookiecutter.json), and will build the images (this can take some time)
```console
make tests
```

### Extend the tests
Right now, tests only checks that cookiecutter can be run and the Docker images built. Manual testing is still required to check that the build images run as expected.

## License

This project is licensed under the terms of the [MIT License](/LICENSE)

## More Details

This cookiecutter allows users to choose a Kernel, among Python, R and Julia, where they can install packages with from a requirement-like file (see [env-config]({{cookiecutter.project_slug}}/env-config/)) for details. 

In case these options are not enough, they can build their custom image. We recommend to use one of the [Jupyter Docker Stacks]({{cookiecutter.project_slug}}/Dockerfile#L4-L5) as base (so JupyterLab is already installed and configured) and the [start-up scripts](./{{cookiecutter.project_slug}}/boot_scripts/) can be re-used.

By default, with this cookiecutter, users install their libraries in the main kernel (i.e. we don't add an additional kernel to the ones already shipped with the base JupyterLab).
---

<p align="center">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" width="150">
</p>
