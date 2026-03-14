import asyncio
from functools import wraps


class RetryException(Exception):
    """Custom retry trigger exception."""
    pass


def async_retry(
    retries: int = 3,
    delay: float = 1,
    allowed_exceptions: tuple = (Exception,)
):
    """
    Enterprise async retry decorator.
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, retries + 1):
                try:
                    return await func(*args, **kwargs)

                except allowed_exceptions as e:
                    last_exception = e

                    if attempt == retries:
                        raise

                    await asyncio.sleep(delay)

            raise last_exception

        return wrapper

    return decorator