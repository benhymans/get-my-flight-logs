import argparse
import os
import sys
from typing import Optional

try:
    import tomllib
except ModuleNotFoundError:  # fallback for Python < 3.11
    import tomli as tomllib


class Config:
    def __init__(self, source: str, destination: str) -> None:
        self.source = source
        self.destination = destination


def load_config(path: str) -> Config:
    with open(path, "rb") as f:
        data = tomllib.load(f)
    paths = data.get("paths", {})
    source = paths.get("source")
    destination = paths.get("destination")
    if not source or not destination:
        raise ValueError("Config must define paths.source and paths.destination")
    return Config(source, destination)


def copy_logs(config: Config) -> None:
    import pymtp

    device = pymtp.MTP()
    device.connect()
    try:
        os.makedirs(config.destination, exist_ok=True)
        for obj in device.get_ObjectHandles():
            info = device.get_ObjectInfo(obj)
            if info.filename.startswith(config.source):
                data = device.get_file_to_buffer(obj)
                dest_path = os.path.join(
                    config.destination, os.path.basename(info.filename)
                )
                with open(dest_path, "wb") as f:
                    f.write(data)
    finally:
        device.disconnect()


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy DJI flight logs via MTP")
    parser.add_argument(
        "-c",
        "--config",
        default="config.toml",
        help="Path to configuration file",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    args = parse_args(argv)
    config = load_config(args.config)
    copy_logs(config)


if __name__ == "__main__":
    main()
