from loguru import logger

logger.add('./logs/run_{time:YYYY-MM-DD}.log', serialize=True, enqueue=True, rotation='50 MB', compression='zip', backtrace=True, catch=True)