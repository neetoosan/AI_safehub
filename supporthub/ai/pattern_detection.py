"""AI Services - Pattern Detection using Similarity Analysis"""

import os
from typing import List, Dict
import requests


class PatternDetector:
    """Detect recurring patterns in reports using similarity analysis"""

    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY", "")
        self.api_url_base = "https://api-inference.huggingface.co/models"
        
        # Semantic similarity model
        self.similarity_model = "sentence-transformers/all-MiniLM-L6-v2"
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        # Similarity threshold for pattern matching
        self.similarity_threshold = 0.7

    def detect_patterns(self, report_text: str, reports_db: List[Dict]) -> List[Dict]:
        """
        Find similar/related reports

        Args:
            report_text: Current report text
            reports_db: List of existing reports

        Returns:
            List of related report IDs with similarity scores
        """
        if not reports_db:
            return []
        
        similar_reports = []
        
        # Simple string similarity for demo (Levenshtein-like)
        for report in reports_db:
            similarity = self._calculate_text_similarity(
                report_text,
                report.get("description", "")
            )
            
            if similarity > self.similarity_threshold:
                similar_reports.append({
                    "report_id": report.get("id"),
                    "report_number": report.get("report_id"),
                    "similarity_score": round(similarity, 2),
                    "description": report.get("description", "")[:100]
                })
        
        # Sort by similarity score
        similar_reports.sort(key=lambda x: x["similarity_score"], reverse=True)
        return similar_reports[:5]  # Return top 5 matches

    def find_recurring_offenders(self, reports_db: List[Dict]) -> List[Dict]:
        """Identify potential recurring offenders based on pattern similarity"""
        offender_patterns = {}
        
        # Group reports by similarity
        for i, report1 in enumerate(reports_db):
            if "patterns" not in offender_patterns:
                offender_patterns[f"pattern_{i}"] = [report1]
            
            for j, report2 in enumerate(reports_db[i+1:], start=i+1):
                similarity = self._calculate_text_similarity(
                    report1.get("description", ""),
                    report2.get("description", "")
                )
                
                if similarity > self.similarity_threshold:
                    if f"pattern_{i}" not in offender_patterns:
                        offender_patterns[f"pattern_{i}"] = []
                    offender_patterns[f"pattern_{i}"].append(report2)
        
        # Filter patterns with 2+ reports
        recurring = []
        for pattern_id, reports in offender_patterns.items():
            if len(reports) >= 2:
                recurring.append({
                    "pattern_id": pattern_id,
                    "incident_count": len(reports),
                    "report_ids": [r.get("id") for r in reports],
                    "severity_average": sum(r.get("severity_score", 5) for r in reports) / len(reports)
                })
        
        return sorted(recurring, key=lambda x: x["incident_count"], reverse=True)

    def identify_hotspots(self, reports_db: List[Dict]) -> List[Dict]:
        """Identify locations with high incident rates"""
        location_stats = {}
        
        for report in reports_db:
            location = report.get("location", "Unknown")
            if location not in location_stats:
                location_stats[location] = {
                    "location": location,
                    "incident_count": 0,
                    "average_severity": 0,
                    "reports": []
                }
            
            location_stats[location]["incident_count"] += 1
            location_stats[location]["reports"].append(report.get("id"))
        
        # Calculate averages
        for location in location_stats:
            if location_stats[location]["incident_count"] > 0:
                total_severity = sum(
                    r.get("severity_score", 5) 
                    for r in [rep for rep in reports_db 
                             if rep.get("location") == location]
                )
                location_stats[location]["average_severity"] = (
                    total_severity / location_stats[location]["incident_count"]
                )
        
        # Return hotspots with 3+ incidents
        hotspots = [
            loc for loc in location_stats.values() 
            if loc["incident_count"] >= 3
        ]
        
        return sorted(hotspots, key=lambda x: x["incident_count"], reverse=True)

    def temporal_analysis(self, reports_db: List[Dict]) -> Dict:
        """Analyze temporal patterns in reports"""
        temporal_data = {
            "total_reports": len(reports_db),
            "by_hour": {},
            "by_day": {},
            "trends": "increasing" if len(reports_db) > 5 else "stable"
        }
        
        # Simple temporal analysis
        for report in reports_db:
            # Mock temporal data for demo
            day = report.get("day", "unknown")
            hour = report.get("hour", "unknown")
            
            if day not in temporal_data["by_day"]:
                temporal_data["by_day"][day] = 0
            temporal_data["by_day"][day] += 1
            
            if hour not in temporal_data["by_hour"]:
                temporal_data["by_hour"][hour] = 0
            temporal_data["by_hour"][hour] += 1
        
        return temporal_data

    def _calculate_text_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts using simple method"""
        # Simple word-based similarity for demo
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
