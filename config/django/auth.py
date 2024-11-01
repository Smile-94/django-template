from pydantic_settings import BaseSettings
from loguru import logger


class AuthSettings(BaseSettings):

    try:
        FIRST_RUN: bool = True  # Custom flag to check first run
        AUTH_USER_MODEL: str = "user.User"

        AUTHENTICATION_BACKENDS: list[str] = [
            "django.contrib.auth.backends.ModelBackend"
        ]

        AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
            {
                "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
            },
        ]

    except Exception as e:
        logger.error(f"--->> Error loading AuthSettings: {str(e)}")


auth_config = AuthSettings()