import logging

def setup_logger():
    logging.basicConfig(
        filename="activity.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_action(message):
    logging.info(message)
