"""Demo data provider for SupportHub demonstrations"""

from datetime import datetime, timedelta


class DemoDataProvider:
    """Provides realistic mock data for demo purposes"""

    @staticmethod
    def get_mock_reports() -> list:
        """Get mock reports for demonstration"""
        return [
            {
                "id": 1,
                "report_id": "RPT-001A",
                "title": "Severe Harassment in Workplace",
                "description": (
                    "I have been consistently harassed by my manager over the past 3 months. "
                    "He makes degrading comments about my work, excludes me from meetings, "
                    "and has threatened to fire me if I don't comply with unreasonable demands. "
                    "This is affecting my mental health. I have evidence via emails and witnessed incidents."
                ),
                "severity_score": 8.7,
                "severity_level": "Critical",
                "status": "pending",
                "time": "2 hours ago",
                "location": "Building A, 3rd Floor",
                "incident_date": "2026-01-31",
            },
            {
                "id": 2,
                "report_id": "RPT-001B",
                "title": "Recurring Pattern Detected",
                "description": (
                    "Another incident with the same individual targeting different employees. "
                    "This appears to be a pattern of abuse of power and intimidation tactics. "
                    "Multiple victims have come forward with similar experiences."
                ),
                "severity_score": 8.2,
                "severity_level": "High",
                "status": "under_review",
                "time": "4 hours ago",
                "location": "Building A, 3rd Floor",
                "incident_date": "2026-01-31",
            },
            {
                "id": 3,
                "report_id": "RPT-001C",
                "title": "Cyberbullying in Group Chat",
                "description": (
                    "I am being targeted in a workplace group chat. Colleagues are making "
                    "insulting comments, spreading rumors, and excluding me from conversations. "
                    "This has been going on for 2 weeks and is affecting my work performance."
                ),
                "severity_score": 6.5,
                "severity_level": "High",
                "status": "pending",
                "time": "6 hours ago",
                "location": "Online",
                "incident_date": "2026-01-31",
            },
            {
                "id": 4,
                "report_id": "RPT-001D",
                "title": "Discrimination Based on Gender",
                "description": (
                    "I have been passed over for promotions multiple times despite strong performance. "
                    "Male colleagues with less experience have been promoted. I overheard comments "
                    "suggesting gender bias in promotion decisions."
                ),
                "severity_score": 7.1,
                "severity_level": "High",
                "status": "pending",
                "time": "1 day ago",
                "location": "HR Department",
                "incident_date": "2026-01-30",
            },
            {
                "id": 5,
                "report_id": "RPT-001E",
                "title": "Physical Threat Incident",
                "description": (
                    "A coworker threatened physical violence against me. He said he would 'beat me up' "
                    "if I reported him to management. This happened in front of other witnesses. "
                    "I am afraid to come to work now."
                ),
                "severity_score": 9.0,
                "severity_level": "Critical",
                "status": "under_review",
                "time": "3 days ago",
                "location": "Parking Lot",
                "incident_date": "2026-01-28",
            },
        ]

    @staticmethod
    def get_mock_patterns() -> list:
        """Get mock pattern detection results"""
        return [
            {
                "pattern_id": "PAT-001",
                "pattern_name": "Manager Harassment Pattern",
                "incident_count": 5,
                "report_ids": [1, 2, 8, 12, 15],
                "severity_average": 8.1,
                "location": "Building A, 3rd Floor",
                "confidence": 0.94,
                "description": "Multiple reports from different employees against same manager"
            },
            {
                "pattern_id": "PAT-002",
                "pattern_name": "Group Chat Cyberbullying",
                "incident_count": 3,
                "report_ids": [3, 7, 11],
                "severity_average": 6.2,
                "location": "Online",
                "confidence": 0.87,
                "description": "Coordinated harassment in workplace group chat"
            },
            {
                "pattern_id": "PAT-003",
                "pattern_name": "Gender Discrimination",
                "incident_count": 2,
                "report_ids": [4, 9],
                "severity_average": 6.8,
                "location": "Multiple Locations",
                "confidence": 0.78,
                "description": "Systemic gender bias in promotion and hiring decisions"
            },
        ]

    @staticmethod
    def get_mock_analytics() -> dict:
        """Get mock analytics data"""
        return {
            "total_reports": 127,
            "reports_this_month": 42,
            "high_severity": 12,
            "pending_review": 34,
            "resolved": 81,
            "patterns_detected": 8,
            "resolution_rate": 0.78,
            "average_resolution_time": "4.2 days",
            "abuse_types": {
                "Harassment": 42,
                "Discrimination": 28,
                "Bullying": 32,
                "Threat": 12,
                "Assault": 8,
                "Other": 5,
            },
            "severity_distribution": {
                "Critical": 12,
                "High": 45,
                "Medium": 48,
                "Low": 22,
            },
            "monthly_trend": [
                {"month": "Nov", "count": 18},
                {"month": "Dec", "count": 24},
                {"month": "Jan", "count": 42},
            ],
            "top_locations": [
                {"location": "Building A", "incidents": 32},
                {"location": "Online", "incidents": 28},
                {"location": "Meeting Room", "incidents": 15},
                {"location": "HR Department", "incidents": 12},
                {"location": "Parking Lot", "incidents": 8},
            ],
        }

    @staticmethod
    def get_mock_ai_analysis(report_id: int) -> dict:
        """Get mock AI analysis for a report"""
        analyses = {
            1: {
                "classification": {
                    "harassment": 0.94,
                    "discrimination": 0.45,
                    "bullying": 0.38,
                    "threat": 0.52,
                    "assault": 0.15,
                },
                "severity_score": 8.7,
                "severity_level": "Critical",
                "confidence": 0.96,
                "contributing_factors": [
                    "Repeated harassment pattern (3+ incidents documented)",
                    "Threat language identified ('fire you')",
                    "Power imbalance indicators (manager-employee)",
                    "Extended time period (3 months)",
                    "Mental health impact mentioned",
                    "Evidence availability (emails, witnesses)"
                ],
                "matched_patterns": [
                    {"pattern_id": "PAT-001", "similarity": 0.92, "incident_count": 5}
                ],
                "explanation": (
                    "This report shows clear indicators of workplace harassment with severe consequences. "
                    "The combination of repeated negative comments, exclusion from meetings, and threats "
                    "creates a hostile work environment. The extended duration (3 months) and documented "
                    "evidence strengthen the classification. Pattern matching identifies similar incidents "
                    "from other employees reporting the same manager, suggesting systemic behavior."
                ),
            },
            2: {
                "classification": {
                    "harassment": 0.91,
                    "discrimination": 0.38,
                    "bullying": 0.35,
                    "threat": 0.48,
                    "assault": 0.12,
                },
                "severity_score": 8.2,
                "severity_level": "High",
                "confidence": 0.93,
                "contributing_factors": [
                    "Pattern of abuse detected",
                    "Multiple victims identified",
                    "Abuse of power indicators",
                    "Intimidation tactics documented",
                ],
                "matched_patterns": [
                    {"pattern_id": "PAT-001", "similarity": 0.88, "incident_count": 5}
                ],
                "explanation": (
                    "This report corroborates the pattern of harassment detected in other incidents. "
                    "The consistency of complaints against the same individual strengthens the case for "
                    "systemic harassment. The AI model identifies this as part of a larger pattern requiring "
                    "escalated investigation and potential disciplinary action."
                ),
            },
            3: {
                "classification": {
                    "harassment": 0.78,
                    "discrimination": 0.25,
                    "bullying": 0.85,
                    "threat": 0.22,
                    "assault": 0.08,
                },
                "severity_score": 6.5,
                "severity_level": "High",
                "confidence": 0.88,
                "contributing_factors": [
                    "Coordinated group behavior",
                    "Extended duration (2 weeks)",
                    "Work performance impact",
                    "Online/remote nature",
                ],
                "matched_patterns": [
                    {"pattern_id": "PAT-002", "similarity": 0.84, "incident_count": 3}
                ],
                "explanation": (
                    "This is classified as cyberbullying due to the group chat dynamics and coordinated "
                    "negative behavior. The two-week duration and documented performance impact indicate "
                    "a serious workplace issue. Pattern analysis shows similar incidents in other group chats, "
                    "suggesting a broader cultural issue requiring intervention."
                ),
            },
        }
        return analyses.get(report_id, analyses[1])  # Default to first analysis

    @staticmethod
    def get_mock_ai_classifications(text: str) -> dict:
        """Get mock AI classification based on text keywords"""
        text_lower = text.lower()
        scores = {
            "harassment": 0.5,
            "discrimination": 0.3,
            "bullying": 0.4,
            "threat": 0.25,
            "assault": 0.2,
        }

        # Adjust scores based on keywords
        if any(word in text_lower for word in ["harass", "degrad", "exclude"]):
            scores["harassment"] = min(1.0, scores["harassment"] + 0.35)

        if any(word in text_lower for word in ["fire", "threat", "beat", "hurt"]):
            scores["threat"] = min(1.0, scores["threat"] + 0.40)

        if any(word in text_lower for word in ["bully", "insult", "mock"]):
            scores["bullying"] = min(1.0, scores["bullying"] + 0.30)

        if any(word in text_lower for word in ["bias", "discrimination", "because of"]):
            scores["discrimination"] = min(1.0, scores["discrimination"] + 0.35)

        if any(word in text_lower for word in ["punch", "hit", "attack"]):
            scores["assault"] = min(1.0, scores["assault"] + 0.40)

        return scores

    @staticmethod
    def get_dashboard_stats() -> dict:
        """Get dashboard statistics"""
        return {
            "total_reports": 127,
            "high_severity": 12,
            "pending_review": 34,
            "resolved": 81,
            "this_month": 42,
            "resolution_rate": "78%",
            "avg_response_time": "2.1 hours",
        }

    @staticmethod
    def get_recent_activity() -> list:
        """Get recent activity for dashboard"""
        return [
            {
                "id": 1045,
                "title": "Report #1042 - Harassment Case",
                "category": "High Priority",
                "time": "2 hours ago",
            },
            {
                "id": 1044,
                "title": "Pattern Detected - Recurring Offender",
                "category": "Pattern Alert",
                "time": "4 hours ago",
            },
            {
                "id": 1043,
                "title": "Report #1038 - Resolved",
                "category": "Completed",
                "time": "1 day ago",
            },
            {
                "id": 1042,
                "title": "New Report Submitted",
                "category": "Incoming",
                "time": "2 days ago",
            },
        ]
