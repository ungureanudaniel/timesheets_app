import psycopg2
import logging
import os
from time import sleep, time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

TIMEOUT = 30
INTERVAL = 2

def get_db_config():
     """Retrieve database configuration from environment variables."""
     return {
         "dbname": os.environ.get("POSTGRES_DB"),
        "user": os.environ.get("POSTGRES_USER"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "host": os.environ.get("POSTGRES_HOST", "localhost"),  # Default to localhost
        "port": int(os.environ.get("POSTGRES_PORT", 5432)),     # Default to 5432
        "sslmode": os.environ.get("POSTGRES_SSLMODE", "disable"),  # Default to 'disable'
        }
def wait_for_postgres():
    logger.info("Waiting for postgres...")
    config = get_db_config()
    start_time = time()
    while time() - start_time < TIMEOUT:
        try:
            with psycopg2.connect(**config) as conn:
                logger.info("PostgreSQL is ready!")
                return True
        except psycopg2.OperationalError as error:
            logger.info(
                f"PostgreSQL isn't ready.\npsycopg2 {type(error).__name__}\n{error}\nWaiting for {INTERVAL} second(s)..."
            )
            sleep(INTERVAL)

    logger.error(f"Could not connect to PostgreSQL within {TIMEOUT} seconds.")
    return False


wait_for_postgres()