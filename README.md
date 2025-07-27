# get-my-flight-logs

This is a command line Python application that copies flight log files from a DJI Remote Control using the MTP protocol.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `config.toml` file specifying the source path on the device and the local destination directory:
   ```toml
   [paths]
   source = "/sdcard/DJI/dji.go.v4/FlightRecord"
   destination = "./flightlogs"
   ```
3. Run the script:
   ```bash
   python getmyflightlogs.py --help
   python getmyflightlogs.py
   ```

The script connects to the first available MTP device and copies all files from the configured source path into the destination directory.
