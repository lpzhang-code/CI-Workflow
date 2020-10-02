## CI Workflow

### Overview

This simple project involves a GitHub Actions workflow being triggered by push to develop/master branch.

The workflow builds a container image from the Dockerfile, runs unit tests inside of the container, and if those tests pass, logs into DockerHub and pushes up the container image we built.

### Docker

Containerisation can be a difficult concept, but is easier to grasp when considering the following points:

- the Dockerfile contains instructions for building the container image. It usually involves installing dependencies, and copying the source code into the root directory of the container (which we can name).
- once the source code is copied into the container, and mounted with docker compose, changes made inside of the container are persisted outside of it (and vice versa).
- we run a container using an image we built ourselves or by downloading a prebuilt image. We can share images on DockerHub, in theory allowing anyone to run the application in a standardised environment.

### GitHub Actions

This is a very useful tool for running workflows on the code in our repository:

- Workflows are triggered by some event such as push/PR to a branch in the repository.
- Workflows consist of jobs which run on their own machine, one job can be dependent on the successful completion of another job.
- Jobs consist of precise operations known as actions, these can be defined by ourselves or prebuilt by the community.
- All this is written in YAML configuration file, which allows for logical expressions, artifacts (which are outputs of some job), and caching.
