"""
Utility functions for the prompt checker
"""

import os
import yaml
from typing import Dict, Optional

def load_config(config_path: Optional[str] = None) -> Dict:
    """
    Load configuration from file or use default configuration
    
    Args:
        config_path: Optional path to configuration file
        
    Returns:
        Configuration dictionary
    """
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
            
    # Default configuration
    return {
        "risk_threshold": 0.7,
        "patterns": [
            {
                "regex": r"ignore.*previous.*instructions",
                "description": "Attempt to ignore previous instructions",
                "weight": 0.8
            },
            {
                "regex": r"you.*are.*now.*(?:dan|dyn|d4n)",
                "description": "DAN-like jailbreak attempt",
                "weight": 0.9
            },
            {
                "regex": r"bypass.*(?:safety|restrictions|filters)",
                "description": "Attempt to bypass safety measures",
                "weight": 0.85
            },
            {
                "regex": r"act.*as.*(?:hack|exploit|jailbreak)",
                "description": "Attempt to act as a hacker or exploiter",
                "weight": 0.75
            },
            {
                "regex": r"generate.*(?:malware|virus|exploit)",
                "description": "Attempt to generate harmful code",
                "weight": 0.95
            },
            {
                "regex": r"pretend.*to.*be.*(?:hack|exploit|jailbreak)",
                "description": "Attempt to pretend to be a hacker",
                "weight": 0.7
            },
            {
                "regex": r"ignore.*(?:ethics|morals|safety)",
                "description": "Attempt to ignore ethical guidelines",
                "weight": 0.8
            }
        ]
    } 