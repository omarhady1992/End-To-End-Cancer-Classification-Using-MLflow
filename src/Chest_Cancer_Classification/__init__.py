import os
import sys
import logging

logging_format = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"

log_dir = "logs"
log_fp = os.path.join(log_dir, "running_logs.log")

logging.basicConfig(
    level= logging.INFO,
    format = logging_format,
    handlers= [ 
        logging.FileHandler(log_fp),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("ClassifierLogger")