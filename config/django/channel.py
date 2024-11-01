from typing import Any
from loguru import logger
from pydantic import Field
from pydantic_settings import BaseSettings
from config.django.database import db_config


class ChannelSettings(BaseSettings):
    """
    This class defines the setting configuration for the channel layer.
    """

    logger.info("--->> Start executing the channel layer configuration")
    CHANNEL_LAYERS: dict[str, Any] = Field(
        default={
            "default": {
                "BACKEND": "channels_redis.core.RedisChannelLayer",
                "CONFIG": {
                    "hosts": [
                        (db_config.REDIS_HOST.get_secret_value(), db_config.REDIS_PORT),
                    ],
                },
            },
        },
        frozen=True,
    )
    logger.success("--->> Channel layer configuration executed successfully")


channel_config = ChannelSettings()
