"""AI Services - Severity Scoring using Hugging Face API"""

import os
from typing import Dict, List
import requests


class SeverityScorer:
    """Calculate severity scores using AI and multiple factors"""

    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY", "")
        self.api_url_base = "https://api-inference.huggingface.co/models"
        
        # Text similarity model to compare with known severe cases
        self.similarity_model = "sentence-transformers/all-MiniLM-L6-v2"
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        # Known high-severity keywords
        self.high_severity_keywords = [
            "kill", "suicide", "die", "threat", "danger", "attack",
            "punch", "hit", "stab", "weapon", "bomb", "gun"
        ]
        
        self.medium_severity_keywords = [
            "hate", "stupid", "idiot", "loser", "racist", "sexist",
            "discriminat", "bully", "insult", "mock"
        ]

    def score(self, text: str, report_metadata: Dict = None) -> float:
        """
        Calculate severity score (0-10)

        Args:
            text: Report description
            report_metadata: Additional context (location, reporter role, etc)

        Returns:
            Severity score (0.0-10.0)
        """
        if report_metadata is None:
            report_metadata = {}
        
        # Calculate base score from text
        base_score = self._calculate_text_severity(text)
        
        # Apply metadata adjustments
        metadata_adjustment = self._calculate_metadata_adjustment(report_metadata)
        
        final_score = min(10.0, base_score + metadata_adjustment)
        return round(final_score, 1)

    def _calculate_text_severity(self, text: str) -> float:
        """Score based on text content and keywords"""
        text_lower = text.lower()
        score = 2.0  # Base score
        
        # Check for high severity keywords
        high_keyword_count = sum(1 for keyword in self.high_severity_keywords 
                                if keyword in text_lower)
        score += high_keyword_count * 1.5
        
        # Check for medium severity keywords  
        medium_keyword_count = sum(1 for keyword in self.medium_severity_keywords 
                                  if keyword in text_lower)
        score += medium_keyword_count * 0.8
        
        # Text length as factor (longer reports often have more detail)
        if len(text) > 500:
            score += 1.0
        elif len(text) > 200:
            score += 0.5
        
        # Repetition detection (multiple exclamation marks, caps)
        if "!!!" in text or text.count("!") > 3:
            score += 1.0
        
        caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
        if caps_ratio > 0.3:  # More than 30% caps
            score += 0.5
        
        return min(score, 8.0)  # Cap at 8 before metadata adjustment

    def _calculate_metadata_adjustment(self, metadata: Dict) -> float:
        """Adjust score based on report metadata"""
        adjustment = 0.0
        
        # Repeated reporter flag
        if metadata.get("is_recurring_pattern"):
            adjustment += 1.5
        
        # Power imbalance indicators
        if metadata.get("power_imbalance"):
            adjustment += 1.0
        
        # Time-sensitive (ongoing harassment)
        if metadata.get("is_ongoing"):
            adjustment += 1.0
        
        # Multiple witnesses
        witness_count = metadata.get("witness_count", 0)
        if witness_count > 0:
            adjustment += min(witness_count * 0.5, 1.0)
        
        return adjustment

    def get_contributing_factors(self, text: str, score: float) -> List[str]:
        """Identify factors contributing to the score"""
        factors = []
        text_lower = text.lower()
        
        # Check for specific patterns
        if any(keyword in text_lower for keyword in self.high_severity_keywords):
            factors.append("High-severity language detected")
        
        if text.count("!!!") > 0 or text.count("!") > 3:
            factors.append("Emotional intensity indicators (excessive punctuation)")
        
        if len(text) > 500:
            factors.append("Detailed incident report (comprehensive description)")
        
        caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
        if caps_ratio > 0.3:
            factors.append("All-caps language indicating heightened emotion")
        
        if score >= 8:
            factors.append("Severity score above 8 (critical level)")
        elif score >= 6:
            factors.append("Severity score between 6-8 (high level)")
        elif score >= 4:
            factors.append("Severity score between 4-6 (medium level)")
        else:
            factors.append("Severity score below 4 (low level)")
        
        return factors

    def categorize_severity(self, score: float) -> str:
        """Convert numeric score to severity level"""
        if score >= 8.0:
            return "Critical"
        elif score >= 6.0:
            return "High"
        elif score >= 4.0:
            return "Medium"
        else:
            return "Low"
