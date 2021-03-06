import os
import uuid
import tempfile

import delegator
import docker
import logme

from .env import SUBDOCKER_STORAGE_DIR, HEROKUISH_IMAGE

# from .env import HEROKUISH_IMAGE

# docker run --rm -v $(pwd):/tmp/app gliderlabs/herokuish /bin/herokuish buildpack build
@logme.log
def build(*, repo_url, environ=None, logger):
    if environ is None:
        environ = {}

    # Ensure Docker is running.
    delegator.run("service docker start")

    # Temporary location for application.
    tmp_dir = tempfile.mkdtemp()
    build_id = uuid.uuid4().hex

    logger.info(f"Starting build {build_id!r}.")

    # Clone a git repo.
    cmd = f"git clone {repo_url} {tmp_dir}"
    logger.info(f"Running $ {cmd}.")
    c = delegator.run(cmd)

    # b'APP_PATH=/app                    # Application path during runtime'
    # b'ENV_PATH=/tmp/env                # Path to files for defining base environment'
    # b'BUILD_PATH=/tmp/build            # Working directory during builds'
    # b'CACHE_PATH=/tmp/cache            # Buildpack cache location'
    # b'IMPORT_PATH=/tmp/app             # Mounted path to copy to app path'
    # b'BUILDPACK_PATH=/tmp/buildpacks   # Path to installed buildpacks'

    # Create the Docker client.
    c = docker.from_env()

    # Pull the image.
    logger.info("Pulling Herokuish Docker image...")
    c.api.pull(HEROKUISH_IMAGE)
    logger.info("Done pulling Herokuish Docker image!")

    # docker run gliderlabs/herokuish /bin/herokuish buildpack build
    logger.info(f"Running build {build_id!r}...")

    # TODO: store image.

    container_id = c.api.create_container(
        HEROKUISH_IMAGE,
        f"/bin/herokuish buildpack build {build_id}; /bin/herokuish slug generate; /bin/herokuish slug export",
        volumes=["/tmp/app"],
        host_config=docker.types.HostConfig(
            version=8,
            binds=[f"{tmp_dir}:/tmp/app", f"{SUBDOCKER_STORAGE_DIR}:/var/lib/docker"],
        ),
    )

    container = c.containers.get(container_id)
    container.start()

    for line in container.logs(stream=True):
        print(line.strip())
