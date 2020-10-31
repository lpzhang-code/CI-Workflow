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

**First Example**

- create YAML file in `.github/workflows`, beginning with optional workflow name appearing in the actions tab

```
name: example-workflow
```

- specify event which triggers workflow

```
on: [push]
```

- specify the workflow's jobs, by default multiple jobs run in parallel; name the only job for this workflow

```
jobs:
  check-bats-version:
```

- that job will be executed by Linux runner hosted by GitHub

```
    runs-on: ubuntu-latest
```

- now specify the job's actions, which can be run directly on machine or in container; actions in the same job can share data; we begin with prebuilt community action which downloads our commit to the runner

```
    steps:
      - uses: actions/checkout@v2
```

- second action is also prebuilt by the community, it downloads node package to runner, giving access to npm command

```
      - uses: actions/setup-node@v1
```

- third actions runs command where npm installs package

```
      - run: npm install -g bats
```

- final action runs command outputting package version

```
      - run: bats -v
```

**Second Example**

- following example shows making env vars available to client.js script

```
jobs:
  example-job:
      steps:
        - name: Connect to Postgres
          run: node client.js
          env:
            POSTGRES_HOST: postgres
            POSTGRES_PORT: 5432
```

**Third Example**

- store script inside repository, then run using action by specifying path and shell type

```
jobs:
  example-job:
      steps:
        - name: Run build script
          run: ./.github/scripts/build.sh
          shell: bash
```

**Fourth Example**

- we can share files between jobs in the same workflow, or save them for later reference, by storing them as artifacts; create and upload file as artifact

```
jobs:
  example-job:
      steps:
        - run: |
            expr 1 + 1 > output.log
          shell: bash
        - name: Upload output file
          uses: actions/upload-artifact@v1
          with:
            name: output-log-file
            path: output.log
```

- now download the artifact in separate workflow

```
jobs:
  example-job:
      steps:
        - name: Download single artifact
          uses: actions/download-artifact@v2
          with:
            name: output-log-file
```

**Fifth Example**

- although jobs in the same workflow normally run in parallel, we can run jobs in sequence by creating dependency between second and first job where second won't run if first fails

```
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: ./setup_server.sh
  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - run: ./build_server.sh
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: ./test_server.sh
```

**Sixth Example**

- use build matrix to run job across multiple combinations; the below build matrix runs job across different versions of node.js

```
jobs:
  example-job:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [6, 8, 10]
    steps:
      - uses: actions/setup-node@v1
      with:
        node-version: $
```

**Seventh Example**

- expressions can be used to set variables

```
env:
  env_var: ${{ <expression> }}
```

- expressions are commonly used with `if` keyword to determine if action should be run

```
if: ${{ <expression> }}
```

- use context objects inside expressions to retrieve information about workflows, runners, jobs, and steps (actions); github object contains information about workflow, env object contains env vars that have been set, etc

```
github.ref = 'ref/heads/develop'
```
