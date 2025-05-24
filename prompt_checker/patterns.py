"""
Pattern matching functionality for detecting jailbreaking attempts
"""

import re
from typing import Dict, List, Optional

class PatternMatcher:
    def __init__(self, config: Dict):
        """
        Initialize pattern matcher with configuration
        
        Args:
            config: Configuration dictionary containing patterns
        """
        self.config = config
        self.patterns = self._compile_patterns()
        
    def _compile_patterns(self) -> List[Dict]:
        """
        Compile regex patterns from configuration
        
        Returns:
            List of compiled pattern dictionaries
        """
        compiled_patterns = []
        
        for pattern in self.config["patterns"]:
            compiled_patterns.append({
                "pattern": re.compile(pattern["regex"], re.IGNORECASE),
                "description": pattern["description"],
                "weight": pattern["weight"]
            })
            
        return compiled_patterns
    
    def find_matches(self, text: str) -> List[Dict]:
        """
        Find all pattern matches in the given text
        
        Args:
            text: Text to search for patterns
            
        Returns:
            List of dictionaries containing match information
        """
        matches = []
        
        for pattern in self.patterns:
            if pattern["pattern"].search(text):
                matches.append({
                    "description": pattern["description"],
                    "weight": pattern["weight"]
                })
                
        return matches 