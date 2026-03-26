"""AI Services - NLP Classification using Hugging Face API"""

import os
from typing import Dict
import requests


class NLPClassifier:
    """Natural Language Processing classifier using Hugging Face Inference API"""

    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY", "")
        self.api_url_base = "https://api-inference.huggingface.co/models"
        
        # Models to use
        self.classification_model = "facebook/bart-large-mnli"  # Zero-shot classification
        self.toxicity_model = "michellejieli/NSFW_text_classifier"
        
        self.labels = [
            "harassment",
            "discrimination", 
            "bullying",
            "threat",
            "assault",
            "other"
        ]
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def classify(self, text: str) -> Dict[str, float]:
        """
        Classify text into abuse categories using zero-shot classification

        Returns:
            Dictionary with {abuse_type: confidence_score}
        """
        if not self.api_key:
            # Return mock data for demo without API key
            return {
                "harassment": 0.92,
                "discrimination": 0.67,
                "bullying": 0.54,
                "threat": 0.23,
                "assault": 0.15,
                "other": 0.05,
            }
        
        try:
            # Use zero-shot classification
            payload = {
                "inputs": text,
                "parameters": {
                    "candidate_labels": self.labels,
                    "multi_class": True
                }
            }
            
            response = requests.post(
                f"{self.api_url_base}/{self.classification_model}",
                headers=self.headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                # Map scores to labels
                classifications = {}
                for label, score in zip(result.get("labels", self.labels), 
                                       result.get("scores", [0] * len(self.labels))):
                    classifications[label] = score
                return classifications
            else:
                # Fallback to mock data on API error
                return self._get_mock_classification(text)
                
        except Exception as e:
            print(f"Classification API error: {e}")
            return self._get_mock_classification(text)

    def _get_mock_classification(self, text: str) -> Dict[str, float]:
        """Return mock classification for demo purposes"""
        # Simple keyword-based mock classification for demo
        text_lower = text.lower()
        scores = {}
        
        if any(word in text_lower for word in ["hate", "stupid", "idiot", "harassment"]):
            scores["harassment"] = 0.85
        if any(word in text_lower for word in ["because of", "discrimination", "racist"]):
            scores["discrimination"] = 0.80
        if any(word in text_lower for word in ["bully", "loser", "weak"]):
            scores["bullying"] = 0.75
        if any(word in text_lower for word in ["kill", "hurt", "danger", "threat"]):
            scores["threat"] = 0.90
        if any(word in text_lower for word in ["hit", "punch", "attack"]):
            scores["assault"] = 0.88
        
        # Fill in remaining labels
        for label in self.labels:
            if label not in scores:
                scores[label] = max(0.0, 0.5 - len(scores) * 0.1)
        
        return scores

    def get_keywords(self, text: str) -> list:
        """Extract relevant keywords from text using NER or simple extraction"""
        # Simple keyword extraction for demo
        abuse_keywords = [
            "harassment", "discriminat", "bully", "threat", "hate", "abuse",
            "assault", "attack", "insult", "racist", "sexist", "homophob"
        ]
        
        found_keywords = []
        text_lower = text.lower()
        
        for keyword in abuse_keywords:
            if keyword in text_lower:
                found_keywords.append(keyword)
        
        return found_keywords[:5]  # Return top 5 keywords
