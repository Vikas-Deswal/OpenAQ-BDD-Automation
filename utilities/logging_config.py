import inspect
import logging
from pathlib import Path
from datetime import datetime

def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Create a file handler (you can customize file path and format)
    if not logger.handlers:  # Only add handler if it doesn't exist
        current_file = Path(__file__)
        project_root = current_file.parent.parent
        log_dir = project_root / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"testLogs_{datetime.now():%Y%m%d_%H%M%S}.log"

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

logger = get_logger()