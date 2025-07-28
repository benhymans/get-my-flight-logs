import argparse
import os
from typing import Optional

DEFAULT_SOURCE = "/sdcard/DJI/dji.go.v4/FlightRecord"
DEFAULT_DESTINATION = "./flightlogs"


def copy_logs(source: str, destination: str) -> None:
    import pymtp

    device = pymtp.MTP()
    device.connect()
    try:
        os.makedirs(destination, exist_ok=True)
        for obj in device.get_ObjectHandles():
            info = device.get_ObjectInfo(obj)
            if info.filename.startswith(source):
                data = device.get_file_to_buffer(obj)
                dest_path = os.path.join(destination, os.path.basename(info.filename))
                with open(dest_path, "wb") as f:
                    f.write(data)
    finally:
        device.disconnect()


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy DJI flight logs via MTP")
    parser.add_argument(
        "-s", "--source", default=DEFAULT_SOURCE, help="Source path on the device"
    )
    parser.add_argument(
        "-d",
        "--destination",
        default=DEFAULT_DESTINATION,
        help="Destination directory",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    args = parse_args(argv)
    copy_logs(args.source, args.destination)


if __name__ == "__main__":
    main()
