# Copilot Instructions for Captura_Python_PI

## Project Overview
This project is a Python-based data capture and monitoring tool, primarily using scripts such as `Captura_Python.py`, `Leitura_Python.py`, and related CSV files for data storage. It is designed for periodic system resource monitoring and logging, with optional alerting (e.g., via Slack) and MySQL integration.

## Key Components
- **Captura_Python.py**: Main script for capturing system metrics (CPU, RAM, Disk), logging to CSV, and sending alerts.
- **Leitura_Python.py**: Reads and processes captured data.
- **ScriptLeitura1.py**: Additional data processing or reporting logic.
- **captura_dados.csv / dados_gerais.csv**: Main data storage files for captured and processed data.
- **script_especificação.py**: (Purpose to be determined; likely for configuration or specification extraction.)

## Patterns & Conventions
- **Resource Monitoring**: Uses `psutil` for CPU, RAM, and disk stats. Data is timestamped and appended to CSV.
- **Alerting**: Alerts (e.g., high CPU/RAM/Disk usage) are sent via a function like `enviar_mensagem_slack`. Thresholds are hardcoded in the main script.
- **Database Integration**: MySQL connection is present but credentials are placeholders. Update with real credentials for production.
- **CSV Logging**: Data is appended using Python's `csv` module with `|` as delimiter.
- **Error Handling**: Uses `try/except KeyboardInterrupt` for graceful shutdown.
- **Scheduling**: Uses `time.sleep(10)` for periodic execution; no external scheduler.

## Developer Workflows
- **Run Main Script**: Execute `Captura_Python.py` directly with Python 3.12+.
- **Dependencies**: Install with `pip install psutil mysql-connector-python` (and any others found in import statements).
- **Virtual Environment**: Use the `venv/` directory for isolation. Activate before running scripts.
- **Debugging**: Print statements are used for runtime feedback. Adjust thresholds or add logging as needed.

## Project-Specific Notes
- **No tests or build system**: There are no automated tests or build scripts. Manual execution and inspection are standard.
- **No config files**: All configuration (thresholds, DB credentials) is hardcoded in scripts.
- **No web or API components**: All logic is local and script-based.
- **No `.env` or secrets management**: Credentials are in plain text; do not commit real secrets.

## Example: Adding a New Metric
To add a new system metric (e.g., network usage):
1. Import the relevant `psutil` function in `Captura_Python.py`.
2. Capture the metric in the main loop.
3. Append the value to the CSV and update print/logging statements.

## Key Files
- `Captura_Python.py`: Main logic, metrics, alerting, and logging.
- `Leitura_Python.py`: Data reading/processing.
- `captura_dados.csv`, `dados_gerais.csv`: Data storage.

---

For questions or improvements, review the main scripts and follow the patterns above. If unclear, ask for clarification or check recent code changes.