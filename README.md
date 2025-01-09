# sync-guardian 🛡️

A reliable Python-based directory synchronization tool designed as a robust alternative to cloud-based sync solutions. Perfect for keeping local directories in sync with automated scheduling support for Windows.

## Features

- Reliable file synchronization with MD5 hash verification
- Detailed logging of all operations
- Windows Task Scheduler integration
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

1. Basic usage:
```bash
python sync_guardian.py "C:\Path\To\Source" "C:\Path\To\Target"
```

2. With custom log file:
```bash
python sync_guardian.py "C:\Path\To\Source" "C:\Path\To\Target" --log "C:\Logs\sync.log"
```

## Windows Task Scheduler Setup

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
