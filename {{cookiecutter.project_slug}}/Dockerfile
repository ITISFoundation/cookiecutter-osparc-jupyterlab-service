
{% if cookiecutter.docker_base != "custom:special-image" %}
# {{ cookiecutter.docker_base }} is one possible base image, you can find information about others here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html
# Check the Jupyter/docker-stacks repo for more information about other versions: https://github.com/jupyter/docker-stacks
FROM {{ cookiecutter.docker_base }} as base
{% endif %}

{% if cookiecutter.docker_base == "custom:special-image" %}
# Choose your custom docker image, for example some jupyter-based ones are documented  here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html
# If you need older versions, you can find more information here: https://github.com/jupyter/docker-stacks?tab=readme-ov-file#using-old-images
# Or check the available images in the registry: https://quay.io/organization/jupyter
FROM {{ cookiecutter.docker_base }} as base
{% endif %}

LABEL maintainer={{ cookiecutter.git_username }}

ENV JUPYTER_ENABLE_LAB="yes"
# autentication is disabled for now
ENV NOTEBOOK_TOKEN=""
ENV NOTEBOOK_BASE_DIR="$HOME/work"

USER root

ENV HOME="/home/$NB_USER"

# --------------- Add additional system libraries -------------------
# TODO: do you need additional system libraries (e.g. zip, bc, etc...)?
# If yes, uncomment the following and adapt
# If not, remove the following (or leave commented)

# RUN apt-get update && \
#   apt-get install -y --no-install-recommends \
#   bc \
#   zip \
#   && \
#   apt-get clean && rm -rf /var/lib/apt/lists/* 

{% if cookiecutter.docker_base == "quay.io/jupyter/minimal-notebook:python-3.11" %}
ENV REQ_FILE="requirements.txt"
# ------------------------------  Python packages   --------------
# This will install the additional packages that you specified in requirements.txt in the pre-existing Python kernel
# Like in: https://github.com/jupyter/docker-stacks/blob/main/images/scipy-notebook/Dockerfile

COPY --chown=$NB_UID:$NB_GID env-config/python/${REQ_FILE} ${NOTEBOOK_BASE_DIR}/${REQ_FILE}
RUN mamba install --yes --file ${NOTEBOOK_BASE_DIR}/${REQ_FILE}

## ----------------------------------------------------------------------
{% endif %}

{% if cookiecutter.docker_base == "quay.io/jupyter/r-notebook:r-4.3.3" %} 
# ------------------------- Other kernel -------------------------------------------
# This will install the additional packages that you specified in requirements.txt in the pre-existing R kernel
# Like in: https://github.com/jupyter/docker-stacks/blob/main/images/r-notebook/Dockerfile
ENV REQ_FILE="requirements.txt"
COPY --chown=$NB_UID:$NB_GID env-config/r/${REQ_FILE} ${NOTEBOOK_BASE_DIR}/${REQ_FILE}
RUN mamba install --yes --file ${NOTEBOOK_BASE_DIR}/${REQ_FILE}
## ------------------------------------------------------------------------
{% endif %}


{% if cookiecutter.docker_base == "quay.io/jupyter/julia-notebook:julia-1.10.2" %} 
ENV REQ_FILE="Project.toml"
# ------------------------- Other kernel -------------------------------------------
# This will install the additional packages that you specified in Project.toml in the pre-existing Julia kernel.
COPY --chown=$NB_UID:$NB_GID env-config/julia/${REQ_FILE} ${NOTEBOOK_BASE_DIR}/${REQ_FILE}
RUN julia --project=${REQ_FILE} -e 'using Pkg; Pkg.instantiate()'
## ------------------------------------------------------------------------
{% endif %}

# ---------------- Final setup  --------------------------------------------------------

USER root

RUN apt-get update && \
   apt-get install -y --no-install-recommends \
   gosu \
   && \
   apt-get clean && rm -rf /var/lib/apt/lists/* 

# Run a script from the base image to fix files permission
#RUN fix-permissions /home/$NB_USER

# copy README and CHANGELOG
COPY --chown=$NB_UID:$NB_GID README.ipynb ${NOTEBOOK_BASE_DIR}/README.ipynb
COPY --chown=$NB_UID:$NB_GID CHANGELOG.md ${NOTEBOOK_BASE_DIR}/CHANGELOG.md

# remove write permissions from files which are not supposed to be edited
RUN chmod gu-w ${NOTEBOOK_BASE_DIR}/CHANGELOG.md && \
  chmod gu-w ${NOTEBOOK_BASE_DIR}/${REQ_FILE}

RUN mkdir --parents "/home/${NB_USER}/.virtual_documents" && \
  chown --recursive "$NB_USER" "/home/${NB_USER}/.virtual_documents"
ENV JP_LSP_VIRTUAL_DIR="/home/${NB_USER}/.virtual_documents"

# Copying boot scripts
COPY --chown=$NB_UID:$NB_GID boot_scripts/ /docker
