"""
Core prompt checking functionality
"""

import re
from typing import Dict, List, Tuple, Optional
from .patterns import PatternMatcher
from .utils import load_config

class PromptChecker:
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the prompt checker with optional custom configuration
        
        Args:
            config_path: Path to custom configuration file
        """
        self.config = load_config(config_path)
        self.pattern_matcher = PatternMatcher(self.config)
        
    def analyze_prompt(self, prompt: str) -> Dict:
        """
        Analyze a prompt for potential jailbreaking attempts
        
        Args:
            prompt: The prompt to analyze
            
        Returns:
            Dict containing analysis results including:
            - risk_score: Float between 0 and 1
            - detected_patterns: List of detected patterns
            - warnings: List of warning messages
            - is_safe: Boolean indicating if prompt is safe
        """
        # Convert prompt to lowercase for case-insensitive matching
        prompt_lower = prompt.lower()
        
        # Initialize results
        results = {
            "risk_score": 0.0,
            "detected_patterns": [],
            "warnings": [],
            "is_safe": True
        }
        
        # Check for pattern matches
        pattern_matches = self.pattern_matcher.find_matches(prompt_lower)
        results["detected_patterns"] = pattern_matches
        
        # Calculate risk score
        risk_score = self._calculate_risk_score(pattern_matches)
        results["risk_score"] = risk_score
        
        # Generate warnings
        warnings = self._generate_warnings(pattern_matches, risk_score)
        results["warnings"] = warnings
        
        # Determine if prompt is safe
        results["is_safe"] = risk_score < self.config["risk_threshold"]
        
        return results
    
    def _calculate_risk_score(self, pattern_matches: List[Dict]) -> float:
        """
        Calculate risk score based on detected patterns
        
        Args:
            pattern_matches: List of detected pattern matches
            
        Returns:
            Float between 0 and 1 representing risk level
        """
        if not pattern_matches:
            return 0.0
            
        total_weight = sum(match["weight"] for match in pattern_matches)
        max_possible_weight = sum(
            pattern["weight"] 
            for pattern in self.config["patterns"]
        )
        
        return min(total_weight / max_possible_weight, 1.0)
    
    def _generate_warnings(self, pattern_matches: List[Dict], risk_score: float) -> List[str]:
        """
        Generate warning messages based on detected patterns and risk score
        
        Args:
            pattern_matches: List of detected pattern matches
            risk_score: Calculated risk score
            
        Returns:
            List of warning messages
        """
        warnings = []
        
        for match in pattern_matches:
            warnings.append(f"Detected pattern: {match['description']}")
            
        if risk_score >= self.config["risk_threshold"]:
            warnings.append(
                f"High risk score detected ({risk_score:.2f}). "
                "This prompt may contain jailbreaking attempts."
            )
            
        return warnings 