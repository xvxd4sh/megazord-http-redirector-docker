#!/usr/bin/env pytest
"""Tests for example container."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest

# import time


ENV_VAR = "ECHO_MESSAGE"
ENV_VAR_VAL = "Docker compose is up and running!"
READY_MESSAGE = "Debug message"
RELEASE_TAG = os.getenv("RELEASE_TAG")
VERSION_FILE = "src/version.txt"


# TODO: Implement this test.
# def test_container_count(dockerc):
#    """Verify the test composition and container."""
#    # stopped parameter allows non-running containers in results
#    assert (
#        len(dockerc.containers(stopped=True)) == 1
#    ), "Wrong number of containers were started."


# TODO: Implement this test.
# def test_wait_for_ready(main_container):
#    """Wait for container to be ready."""
#    TIMEOUT = 10
#    for i in range(TIMEOUT):
#        if READY_MESSAGE in main_container.logs().decode("utf-8"):
#            break
#        time.sleep(1)
#    else:
#        raise Exception(
#            f"Container does not seem ready.  "
#            f'Expected "{READY_MESSAGE}" in the log within {TIMEOUT} seconds.'
#        )


# def test_wait_for_exits(main_container, version_container):
#    """Wait for containers to exit."""
#    assert main_container.wait() == 0, "Container service (main) did not exit cleanly"
#    assert (
#        version_container.wait() == 0
#    ), "Container service (version) did not exit cleanly"


# TODO: Implement this test.
# def test_output(main_container):
#    """Verify the container had the correct output."""
#    main_container.wait()  # make sure container exited if running test isolated
#    log_output = main_container.logs().decode("utf-8")
#    assert SECRET_QUOTE in log_output, "Secret not found in log output."
#


@pytest.mark.skipif(
    RELEASE_TAG in [None, ""], reason="this is not a release (RELEASE_TAG not set)"
)
def test_release_version():
    """Verify that release tag version agrees with the module version."""
    pkg_vars = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), pkg_vars)  # nosec
    project_version = pkg_vars["__version__"]
    assert (
        RELEASE_TAG == f"v{project_version}"
    ), "RELEASE_TAG does not match the project version"


# def test_log_version(version_container):
#    """Verify the container outputs the correct version to the logs."""
#    version_container.wait()  # make sure container exited if running test isolated
#    log_output = version_container.logs().decode("utf-8").strip()
#    pkg_vars = {}
#    with open(VERSION_FILE) as f:
#        exec(f.read(), pkg_vars)  # nosec
#    project_version = pkg_vars["__version__"]
#    assert (
#        log_output == project_version
#    ), f"Container version output to log does not match project version file {VERSION_FILE}"


# def test_container_version_label_matches(version_container):
#    """Verify the container version label is the correct version."""
#    pkg_vars = {}
#    with open(VERSION_FILE) as f:
#        exec(f.read(), pkg_vars)  # nosec
#    project_version = pkg_vars["__version__"]
#    assert (
#        version_container.labels["org.opencontainers.image.version"] == project_version
#    ), "Dockerfile version label does not match project version"
