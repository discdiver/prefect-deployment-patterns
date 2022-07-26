import prefect
from prefect import task, flow
from prefect import get_run_logger


@task
def say_hi():
    logger = get_run_logger()
    logger.info("Hello from the Health Check Flow! 👋")


@task
def log_platform_info():
    import platform
    import sys
    from prefect.orion.api.server import ORION_API_VERSION

    logger = get_run_logger()
    logger.info("Host's network name = %s", platform.node())
    logger.info("Python version = %s", platform.python_version())
    logger.info("Platform information (instance type) = %s ", platform.platform())
    logger.info("OS/Arch = %s/%s", sys.platform, platform.machine())
    logger.info("Prefect Version = %s 🚀", prefect.__version__)
    logger.info("Prefect API Version = %s", ORION_API_VERSION)


@flow(name="healthcheck")
def run_healthcheck():
    hi = say_hi()
    log_platform_info(wait_for=[hi])


if __name__ == "__main__":
    run_healthcheck()
