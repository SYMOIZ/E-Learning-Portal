class ConfigurationError(RuntimeError):
    pass

def require_setting(settings: dict, key: str) -> str:
    try:
        return settings[key]
    except KeyError as error:
        raise ConfigurationError(f"Missing required setting: {key}") from error
