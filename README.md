# sync-guardian 🛡️

A reliable Python-based directory synchronization tool designed as a robust alternative to cloud-based sync solutions. Perfect for keeping local directories in sync with automated scheduling support across Windows, macOS, and Linux.

## Features

- Reliable file synchronization with MD5 hash verification
- Detailed logging of all operations
- Cross-platform scheduling support
- Preservation of file metadata
- Nested directory support
- Comprehensive error handling
- Unit tested codebase

## Installation

```bash
git clone https://github.com/moijafcor/sync-guardian.git
cd sync-guardian
pip install -r requirements.txt
```

## Quick Start

Basic usage (all platforms):
```bash
python sync_guardian.py "/path/to/source" "/path/to/target"
```

With custom log file:
```bash
python sync_guardian.py "/path/to/source" "/path/to/target" --log "/path/to/logs/sync.log"
```

## Automated Scheduling Setup

### Windows (Task Scheduler)

1. Save the following as `run_sync.bat`:
```batch
@echo off
python C:\Path\To\sync_guardian.py "C:\Path\To\Source" "C:\Path\To\Target" --log "C:\Logs\sync.log"
```

2. Open Task Scheduler:
   - Create Basic Task
   - Set trigger (Daily/On startup)
   - Action: Start a program
   - Program: Path to your batch file
   - Finish

### macOS (Launchd)

1. Create a plist file `~/Library/LaunchAgents/com.sync-guardian.sync.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.sync-guardian.sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/sync_guardian.py</string>
        <string>/path/to/source</string>
        <string>/path/to/target</string>
        <string>--log</string>
        <string>/path/to/sync.log</string>
    </array>
    <key>StartInterval</key>
    <integer>3600</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

2. Load the job:
```bash
launchctl load ~/Library/LaunchAgents/com.sync-guardian.sync.plist
```

### Linux (Cron)

1. Open your crontab:
```bash
crontab -e
```

2. Add a line for hourly sync (adjust timing as needed):
```
0 * * * * /usr/bin/python3 /path/to/sync_guardian.py "/path/to/source" "/path/to/target" --log "/path/to/sync.log"
```

## Project Structure

```
sync-guardian/
├── src/
│   ├── __init__.py
│   └── sync_guardian.py
├── tests/
│   ├── __init__.py
│   └── test_sync_guardian.py
├── logs/
├── requirements.txt
├── README.md
└── LICENSE
```

## Development

### Running Tests

```bash
python -m unittest tests/test_sync_guardian.py -v
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for reliable local directory synchronization
- Built as an alternative to less reliable cloud-based solutions
- Designed for R programming workflows but suitable for any directory sync needs
- Initially developed with assistance from Claude (Anthropic)
