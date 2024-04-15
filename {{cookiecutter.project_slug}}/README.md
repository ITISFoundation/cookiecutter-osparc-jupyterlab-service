# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}

## Requirements
- GNU Make
- Python3
- [``Docker``](https://docs.docker.com/get-docker/) (if you wish to build and test the service locally)

## Workflow
1. Add your additional libraries to the appropriate in file [`env-config`](./env-config/)
2. The [Dockerfile]({{ cookiecutter.project_slug }}/src/Dockerfile) shall be modified to install additional packages, software and/or Jupyter kernels
3. The [.osparc](.osparc) is the configuration folder and source of truth for metadata: describes service info and expected inputs/outputs of the service. If you need to change the inputs/outputs of the service, description, thumbnail, etc... check the [`metadata.yml`](./.osparc/metadata.yml) file
4. Optional: if you need to change the default the start-up behavior of the service, modify the [`boot_notebook.bash`](./boot_scripts/boot_notebook.bash) file
5. The service docker image may be built with ``make build`` (see "Useful Commands" below)
6. The service docker image may be run locally with ``make run-local`` (see "Useful Commands" below)
7. Once you are happy with your code, an automated pipeline will build the Docker image for you (as in step 5)
8. If you wish to publish you your Service on the o²S²PARC platform, get in touch with [o²S²PARC Support](mailto:support@osparc.io)

After the initial version, you can update your Service and publish a new version, with ``make version-patch``, or ``make version-minor``, or  ``make version-major``

### Useful commands
```console
$ make help
$ make build # This will build an o²S²PARC-compatible image (similar to `Docker build` command)
$ make run-local # This will run the JupyterLab interface on your computer. Follow the instructions in your console to open it in your browser (useful e.g. to test that your code runs as expected)
```

