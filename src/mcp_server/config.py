from pathlib import Path


DEFAULT_CONFIG = Path("config.yaml")


def load_config(path=DEFAULT_CONFIG):
    try:
        import yaml
    except ImportError:
        return {}

    if not Path(path).exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
