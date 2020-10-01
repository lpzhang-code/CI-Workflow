## CI Workflow

### Overview

This simple project involves a GitHub Actions workflow being triggered by push to develop/master branch.

The workflow builds a container image from the Dockerfile, runs unit tests inside of the container, and if those tests pass, logs into DockerHub and pushes up the container image we built.

### Docker

Containerisation can be a difficult concept, but is easier to grasp when considering the following points:

- the Dockerfile contains instructions for building the container image. It usually involves installing dependencies, and copying the source code into the root directory of the container (which we can name).
- once the source code is copied into the container, and mounted with docker compose, changes made inside of the container are persisted outside of it (and vice versa).
- we run a container using an image we built ourselves or by downloading a prebuilt image. We can share images on DockerHub, in theory allowing anyone to run the application in a standardised environment.