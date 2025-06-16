import logging

def setup_logger():
    logging.basicConfig(
        filename="activity.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def setup_logger_grenoble():
    logging.basicConfig(
        filename="activity_grenoble.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def setup_logger_marseille():
    logging.basicConfig(
        filename="activity_marseille.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def setup_logger_rennes():
    logging.basicConfig(
        filename="activity_rennes.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_action(message):
    logging.info(message)
