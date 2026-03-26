"""AI Services - Explainability and Transparency"""

from typing import Dict, List


class Explainability:
    """Generate human-readable explanations for AI decisions"""

    def __init__(self):
        pass

    def explain_classification(self, classification: Dict, text: str) -> str:
        """Explain why text was classified as specific abuse type"""
        # Find top classification
        top_class = max(classification.items(), key=lambda x: x[1])[0]
        top_score = classification[top_class]
        
        explanation = (
            f"The AI model classified this report as '{top_class}' with {top_score:.0%} confidence. "
            f"This classification is based on Natural Language Processing analysis of the incident description. "
            f"The model identifies key phrases and contextual patterns that indicate the type of abuse. "
            f"Keywords and linguistic markers such as repeated language, urgency indicators, and threat terminology "
            f"all contribute to this determination.\n\n"
            f"The system uses semantic analysis to compare the reported text against known patterns of harassment, "
            f"discrimination, bullying, threats, and assault."
        )
        
        return explanation

    def explain_severity(self, severity_score: float, factors: List[str]) -> str:
        """Explain severity score calculation"""
        explanation = f"The severity score of {severity_score}/10 indicates a "
        
        if severity_score >= 8:
            explanation += "CRITICAL level incident that requires immediate attention."
        elif severity_score >= 6:
            explanation += "HIGH priority case that should be reviewed urgently."
        elif severity_score >= 4:
            explanation += "MEDIUM priority case that needs appropriate follow-up."
        else:
            explanation += "LOW priority case, though still requiring documentation."
        
        explanation += "\n\nContributing factors to this score:\n"
        for i, factor in enumerate(factors, 1):
            explanation += f"{i}. {factor}\n"
        
        return explanation

    def explain_priority(self, priority_score: float, reasons: List[str]) -> str:
        """Explain report prioritization"""
        explanation = f"This report is ranked at {priority_score:.0f}% priority in the review queue because:\n\n"
        
        for i, reason in enumerate(reasons, 1):
            explanation += f"{i}. {reason}\n"
        
        explanation += (
            "\nReports are automatically prioritized based on AI analysis of severity, "
            "pattern detection, and contextual factors to ensure that the most urgent cases "
            "receive attention first while maintaining comprehensive case management."
        )
        
        return explanation

    def get_confidence_statement(self, confidence: float) -> str:
        """Generate confidence statement for the AI analysis"""
        if confidence > 0.9:
            return "Very High Confidence - AI is highly certain about this analysis"
        elif confidence > 0.8:
            return "High Confidence - AI is confident about this determination"
        elif confidence > 0.7:
            return "Moderate-High Confidence - AI assessment is reliable"
        elif confidence > 0.6:
            return "Moderate Confidence - AI assessment should be considered with review"
        elif confidence > 0.5:
            return "Lower Confidence - Manual review is strongly recommended"
        else:
            return "Low Confidence - Human moderator review is essential"

    def explain_ai_limitations(self) -> str:
        """Provide transparency about AI system limitations"""
        return (
            "Important: This AI system is designed to assist human moderators, not replace them.\n\n"
            "Limitations to be aware of:\n"
            "• Context nuances: Sarcasm, idioms, and cultural references may be misinterpreted\n"
            "• Language diversity: Non-English text or slang may not be accurately classified\n"
            "• False positives: The system may flag legitimate content due to keyword overlap\n"
            "• Evolving tactics: New forms of abuse may not be immediately recognized\n"
            "• Edge cases: Ambiguous reports require human judgment\n\n"
            "All AI determinations should be reviewed by qualified human moderators before taking action. "
            "The system provides evidence-based recommendations to guide decision-making, "
            "but final determinations rest with human reviewers to ensure fairness and accuracy."
        )

    def explain_pattern_detection(self, patterns: List[Dict]) -> str:
        """Explain how patterns were detected"""
        if not patterns:
            return "No significant patterns detected in current reports."
        
        explanation = f"The system detected {len(patterns)} pattern(s) in the report database:\n\n"
        
        for i, pattern in enumerate(patterns, 1):
            explanation += (
                f"{i}. Pattern involving {pattern.get('incident_count', 0)} incidents\n"
                f"   - Reports: {', '.join(str(rid) for rid in pattern.get('report_ids', [])[:3])}\n"
                f"   - Average severity: {pattern.get('severity_average', 0):.1f}/10\n"
            )
        
        explanation += (
            "\nPattern detection uses text similarity analysis and semantic matching "
            "to identify recurring incidents from the same source or location, "
            "helping identify potential offenders for appropriate intervention."
        )
        
        return explanation
