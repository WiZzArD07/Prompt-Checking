# AI Jailbreaking Prompt Checker

This project provides a robust system for detecting and analyzing potentially harmful or jailbreaking attempts in prompts sent to AI models.

## Features

- Pattern-based detection of common jailbreaking attempts
- Semantic analysis of prompt content
- Scoring system for potential risks
- Configurable detection rules
- Easy integration with existing AI systems
- Interactive web interface using Streamlit

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Python API

```python
from prompt_checker import PromptChecker

checker = PromptChecker()
result = checker.analyze_prompt("Your prompt here")
print(result)
```

### Web Interface

To run the Streamlit web interface:

```bash
streamlit run app.py
```

This will start a local web server and open the interface in your default browser. The interface provides:
- Interactive prompt input
- Real-time analysis
- Visual risk score gauge
- Detailed pattern detection results
- Warning messages

## Project Structure

- `prompt_checker/` - Main package directory
  - `__init__.py` - Package initialization
  - `checker.py` - Core prompt checking logic
  - `patterns.py` - Pattern definitions
  - `utils.py` - Utility functions
- `tests/` - Test suite
- `config/` - Configuration files
- `app.py` - Streamlit web interface
- `requirements.txt` - Project dependencies

## Configuration

The system can be configured through the `config/config.yaml` file to adjust detection rules and thresholds.

## Testing

Run tests using pytest:
```bash
pytest tests/
```

## License

MIT License 