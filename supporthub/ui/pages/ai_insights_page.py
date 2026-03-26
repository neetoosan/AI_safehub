"""AI Insights and Explainability Page"""

import flet as ft
from config.settings import COLORS


def create_ai_insights_page(report_id: str = "1045"):
    """Display AI analysis results and explainability features"""
    
    def build_classification_item(label: str, confidence: str, color: str):
        """Build a classification item with confidence bar"""
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(label, size=12),
                        width=100,
                    ),
                    ft.Container(
                        content=ft.ProgressBar(
                            value=float(confidence.rstrip("%")) / 100,
                            color=color,
                            bgcolor=f"{color}20",
                        ),
                        expand=True,
                        margin=ft.margin.only(right=10),
                    ),
                    ft.Text(confidence, size=12, weight="bold", color=color),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(bottom=8),
        )
    
    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            f"AI Analysis - Report #{report_id}",
                            size=32,
                            weight="bold",
                            color=COLORS["primary"],
                        ),
                        padding=20,
                    ),
                    ft.Divider(),
                    # Classification Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Abuse Classification", weight="bold", size=18),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            build_classification_item(
                                                "Harassment", "92%", COLORS["critical"]
                                            ),
                                            build_classification_item(
                                                "Discrimination", "67%", COLORS["warning"]
                                            ),
                                            build_classification_item(
                                                "Bullying", "54%", COLORS["warning"]
                                            ),
                                            build_classification_item(
                                                "Threat", "23%", COLORS["secondary"]
                                            ),
                                        ]
                                    ),
                                    padding=15,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ],
                        ),
                        padding=20,
                    ),
                    # Severity Scoring
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Severity Assessment", weight="bold", size=18),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text("Overall Severity Score:"),
                                                    ft.Container(
                                                        content=ft.Text(
                                                            "8.7/10",
                                                            weight="bold",
                                                            color=COLORS["critical"],
                                                        ),
                                                        bgcolor=COLORS["critical"],
                                                        opacity=0.2,
                                                        padding=10,
                                                        border_radius=8,
                                                    ),
                                                ],
                                                wrap=True,
                                            ),
                                            ft.Divider(),
                                            ft.Column(
                                                controls=[
                                                    ft.Text("Contributing Factors:", weight="bold"),
                                                    ft.Text("• Repeated pattern detected (3+ incidents)"),
                                                    ft.Text("• Threat language identified"),
                                                    ft.Text("• Power imbalance indicators"),
                                                    ft.Text("• Time-sensitive nature"),
                                                ],
                                                spacing=5,
                                            ),
                                        ]
                                    ),
                                    padding=15,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ],
                        ),
                        padding=20,
                    ),
                    # Pattern Detection
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Pattern Detection", weight="bold", size=18),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text("Potential Recurring Offender (High Confidence)"),
                                            ft.Text(
                                                "Similar incidents linked: #1042, #1038",
                                                size=12,
                                                color=COLORS["secondary"],
                                            ),
                                            ft.ElevatedButton(
                                                content=ft.Text("View Pattern Details"),
                                                icon=ft.Icons.LINK,
                                            ),
                                        ]
                                    ),
                                    padding=15,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ],
                        ),
                        padding=20,
                    ),
                    # Explainability
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Why This Analysis?", weight="bold", size=18),
                                ft.Container(
                                    content=ft.Text(
                                        "The AI model uses Natural Language Processing to analyze the incident description. "
                                        "Keywords like 'harassment', 'repeated', and contextual patterns trigger severity escalation. "
                                        "Cross-referencing with historical reports enhances accuracy and pattern recognition.",
                                        size=12,
                                    ),
                                    padding=15,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ],
                        ),
                        padding=20,
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
        ),
        padding=20,
        bgcolor=COLORS["background"],
        expand=True,
    )
