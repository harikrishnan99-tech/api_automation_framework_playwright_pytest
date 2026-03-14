import logging
import os
from logging.handlers import TimedRotatingFileHandler
import coloredlogs


# Create logs directory if not exists
log_dir = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_dir, exist_ok=True)

# Use fixed log file name (IMPORTANT for rotation)
log_file = os.path.join(log_dir, "application.log")

# Create Logger
logger = logging.getLogger("api_framework_logger")
logger.setLevel(logging.DEBUG)
logger.propagate = False  # Prevent duplicate logs

# Log Format
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
formatter = logging.Formatter(log_format)

# Timed Rotating File Handler
# - Rotate daily at midnight
# - Keep last 7 log files
# --------------------------------------------------
file_handler = TimedRotatingFileHandler(
    filename=log_file,
    when="midnight",      # rotate daily
    interval=1,
    backupCount=7,        # keep last 7 days
    encoding="utf-8"
)

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


# Avoid adding duplicate handlers
if not logger.handlers:
    logger.addHandler(file_handler)


# --------------------------------------------------
# Colored Console Logs
# (Only affects terminal, not file)
# --------------------------------------------------
coloredlogs.install(
    level="INFO",
    logger=logger,
    fmt=log_format,
    level_styles={
        "debug": {"color": "white"},
        "info": {"color": "green"},
        "warning": {"color": "yellow"},
        "error": {"color": "red", "bold": True},
        "critical": {"color": "red", "bold": True},
    }
)