# get-my-flight-logs

This is a command line Python application that copies flight log files from a DJI Remote Control using the MTP protocol.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python getmyflightlogs.py --help
   python getmyflightlogs.py
   ```
   Use `--source` to set the path on the device and `--destination` for the local
   folder. The defaults are `/sdcard/DJI/dji.go.v4/FlightRecord` and `./flightlogs`.

The script connects to the first available MTP device and copies all files from
the source path into the destination directory.
