# Cookiecutter For o²S²PARC Jupyter Services

Template library to generate an [o²S²PARC compatible interactive service with the JupyterLab environment](https://docs.osparc.io/#/docs/study_setup/JupyterLabs?id=jupyterlab). 
In addition to the different JupyterLab "flavours" offered on o²S²PARC, you can use this library to create one with your favourite software and tools. 

This library is pre-configured to easily build JupyterLabs with Python, R or Julia and additional dependencies. Just choose the appropriate `base_image` when running the cookiecutter and follow the instructions in the `README.md`.

If you need to install other custom software, you can do so my selecting the custom image as `base_image`.

## Requirements
- GNU Make
- Python3
- Python3-venv (recommended to work in a virtual environment)
- [``cookiecutter``](https://python-package-generator.readthedocs.io/en/master/)
- [``Docker``](https://docs.docker.com/get-docker/) (if you wish to build and test the service locally)

To install the cookiecutter:
```console
sudo apt-get update
sudo apt-get install -y make python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install cookiecutter jinja2_time
```

## Usage

Generate a new Cookiecutter template layout:
```console
python3 -m venv .venv
source .venv/bin/activate
cookiecutter git+ssh://git@github.com/ITISFoundation/cookiecutter-osparc-jupyterlab-service
```

## Information for the developers of this cookiecutter

### Get the code and run the cookiecutter
```console
git clone git+ssh://git@github.com/ITISFoundation/cookiecutter-osparc-jupyterlab-service
cd cookiecutter-osparc-jupyterlab-service
make devenv
source .venv/bin/activate
make play
```

### Run the tests
This will create different projects on the docker image bases, specified in [cookiecutter.json](/cookiecutter.json), and will build the images (this can take some time)
```console
make tests
```

### Extend the tests
In the latest version, tests only checks that cookiecutter can be run and the Docker images built. Manual testing is still required to check that the built images run as expected.

## License

This project is licensed under the terms of the [MIT License](/LICENSE)

## More Details

This cookiecutter allows users to choose a Kernel, among Python, R and Julia, where they can install packages from a requirement-like file (see [env-config]({{cookiecutter.project_slug}}/env-config/) for details). By default the latest versions (as of April 2024) provided by the Jupyter team are used (e.g. Python 3.11). Users find in their Dockerfiles instructions on how to use older versions. 

In case these options are not enough, they can build their custom image. We recommend to use one of the [Jupyter Docker Stacks]({{cookiecutter.project_slug}}/Dockerfile#L4-L5) as base (so JupyterLab is already installed and configured) and the [start-up scripts](./{{cookiecutter.project_slug}}/boot_scripts/) can be re-used.

By default, with this cookiecutter, users install their libraries in the main kernel (i.e. we don't add an additional kernel and environment to the ones already shipped with the base JupyterLab).

---

<p align="center">
<a href="https://www.z43.swiss" target="_blank">
<image src="https://raw.githubusercontent.com/ITISFoundation/osparc-simcore-clients/4e8b18494f3191d55f6692a6a605818aeeb83f95/docs/_media/mwl.png" alt="Made with love (and lots of hard work) at www.z43.swiss" width="20%" />
</a>
</p>