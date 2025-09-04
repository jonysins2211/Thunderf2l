# Thunder/__main__.py

import os

from dotenv import load_dotenv
from typing import Set, Optional, List, Dict
from Thunder.utils.logger import logger

load_dotenv("config.env")

def str_to_bool(val: str) -> bool:
    return val.lower() in ("true", "1", "t", "y", "yes")

def str_to_int_list(val: str) -> List[int]:
    return [int(x) for x in val.split() if x.isdigit()] if val else []

def str_to_int_set(val: str) -> Set[int]:
    return {int(x) for x in val.split() if x.isdigit()} if val else set()

class Var:
    API_ID: int = int(os.getenv("API_ID", ""))
    API_HASH: str = os.getenv("API_HASH", "")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

    if not all([API_ID, API_HASH, BOT_TOKEN]):
        logger.critical("Missing required Telegram API configuration")
        raise ValueError("Missing required Telegram API configuration")

    NAME: str = os.getenv("NAME", "Mlfiletolinkbot")
    SLEEP_THRESHOLD: int = int(os.getenv("SLEEP_THRESHOLD", "600"))
    WORKERS: int = int(os.getenv("WORKERS", "8"))
    TIMEOUT: int = int(os.getenv("TIMEOUT", "90"))

    BIN_CHANNEL: int = int(os.getenv("BIN_CHANNEL", "-1002710313786"))

    if not BIN_CHANNEL:
        logger.critical("BIN_CHANNEL is required")
        raise ValueError("BIN_CHANNEL is required")

    PORT: int = int(os.getenv("PORT", "8080"))
    BIND_ADDRESS: str = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PING_INTERVAL: int = int(os.getenv("PING_INTERVAL", "840"))
    NO_PORT: bool = str_to_bool(os.getenv("NO_PORT", "True"))
    CACHE_SIZE: int = int(os.getenv("CACHE_SIZE", "100"))

    OWNER_ID: int = int(os.getenv("OWNER_ID", "949657126"))

    if not OWNER_ID:
        logger.warning("WARNING: OWNER_ID is not set. No user will be granted owner access.")

    OWNER_USERNAME: str = os.getenv("OWNER_USERNAME", "Mladminbot")

    FQDN: str = os.getenv("FQDN", "shared-danni-ravana-04161957.koyeb.app") or BIND_ADDRESS
    HAS_SSL: bool = str_to_bool(os.getenv("HAS_SSL", "True"))
    PROTOCOL: str = "https" if HAS_SSL else "http"
    PORT_SEGMENT: str = "" if NO_PORT else f":{PORT}"
    URL: str = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"

    SET_COMMANDS: bool = str_to_bool(os.getenv("SET_COMMANDS", "True"))

    DATABASE_URL: str = os.getenv("DATABASE_URL", "mongodb+srv://primebaby11220:TuGa0I5ZsiC8mp5A@cluster0.df4rivj.mongodb.net/?retryWrites=true&w=majority")

    if not DATABASE_URL:
        logger.critical("DATABASE_URL is required")
        raise ValueError("DATABASE_URL is required")

    MAX_BATCH_FILES: int = int(os.getenv("MAX_BATCH_FILES", "50"))

    BANNED_CHANNELS: Set[int] = str_to_int_set(os.getenv("BANNED_CHANNELS", ""))

    MULTI_CLIENT: bool = False

    FORCE_CHANNEL_ID: Optional[int] = None

    force_channel_env = os.getenv("FORCE_CHANNEL_ID", "").strip()

    if force_channel_env:
        try:
            FORCE_CHANNEL_ID = int(force_channel_env)
        except ValueError:
            logger.warning(f"Invalid FORCE_CHANNEL_ID '{force_channel_env}' in environment; must be an integer.")

    TOKEN_ENABLED: bool = str_to_bool(os.getenv("TOKEN_ENABLED", "False"))
    TOKEN_TTL_HOURS: int = int(os.getenv("TOKEN_TTL_HOURS", "24"))

    SHORTEN_ENABLED: bool = str_to_bool(os.getenv("SHORTEN_ENABLED", "False"))
    SHORTEN_MEDIA_LINKS: bool = str_to_bool(os.getenv("SHORTEN_MEDIA_LINKS", "False"))
    URL_SHORTENER_API_KEY: str = os.getenv("URL_SHORTENER_API_KEY", "")
    URL_SHORTENER_SITE: str = os.getenv("URL_SHORTENER_SITE", "")

    RATE_LIMIT_ENABLED: bool = str_to_bool(os.getenv("RATE_LIMIT_ENABLED", "True"))
    MAX_FILES_PER_PERIOD: int = int(os.getenv("MAX_FILES_PER_PERIOD", "4"))
    RATE_LIMIT_PERIOD_MINUTES: int = int(os.getenv("RATE_LIMIT_PERIOD_MINUTES", "1"))
    MAX_QUEUE_SIZE: int = int(os.getenv("MAX_QUEUE_SIZE", "100"))
    GLOBAL_RATE_LIMIT: bool = str_to_bool(os.getenv("GLOBAL_RATE_LIMIT", "True"))
    MAX_GLOBAL_REQUESTS_PER_MINUTE: int = int(os.getenv("MAX_GLOBAL_REQUESTS_PER_MINUTE", "4"))

