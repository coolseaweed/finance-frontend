import os
from dataclasses import make_dataclass
from source.core.parsers import parse_origins_list


default_stable_diffusion_bucket = "goarcade"
default_stable_diffusion_key = "kakao/tmp"


def get_config():
    """load environment variables and return a config object"""

    # for development, try to load .env
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass

    _config = dict()

    # cors origins
    # _config["cors_allow_origins"] = parse_origins_list(str(os.environ.get("CORS_ALLOW_ORIGINS", "")))
    _config["cors_allow_origins"] = ["*"]
    _config["cors_allow_credentials"] = bool(int(os.environ.get("CORS_ALLOW_CREDENTIALS", 0)))

    # dart info.
    _config["dart_key"] = os.environ.get("DART_KEY", None)

    # aws info
    _config["aws_access_key_id"] = os.environ.get("AWS_ACCESS_KEY_ID", None)
    _config["aws_secret_access_key"] = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    _config["default_region"] = os.environ.get("DEFAULT_REGION", None)
    _config["expires_in"] = int(os.environ.get("AWS_URL_EXPIRES_IN", 3600))

    # following is for accessing swagger from eks
    _config["root_path"] = str(os.environ.get("ROOT_PATH", ""))
    _config["server_path"] = str(os.environ.get("SERVER_PATH", ""))
    _config["openapi_url"] = str(os.environ.get("OPENAPI_URL", "/openapi.json"))
    _config["swagger_url"] = str(os.environ.get("SWAGGER_URL", "/documentation"))

    # make dataclass to access these variables
    Config = make_dataclass("Config", fields=[(k, type(v)) for k, v in _config.items()])
    config = Config(**_config)

    return config


config = get_config()
