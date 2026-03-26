"""Severity Badge Component"""

import flet as ft
from config.settings import COLORS


class SeverityBadge(ft.Control):
    """Badge component for displaying severity levels with color coding"""

    def __init__(self, severity: str, score: float = None):
        super().__init__()
        self.severity = severity
        self.score = score

    def build(self):
        severity_map = {
            "Critical": (COLORS["critical"], "🔴"),
            "High": (COLORS["warning"], "🟠"),
            "Medium": (COLORS["secondary"], "🟡"),
            "Low": (COLORS["success"], "🟢"),
        }

        color, emoji = severity_map.get(self.severity, (COLORS["text"], "⚪"))

        content = ft.Row(
            controls=[
                ft.Container(
                    width=12,
                    height=12,
                    bgcolor=color,
                    border_radius=6,
                ),
                ft.Text(self.severity, size=12, weight="bold"),
                ft.Text(f"{self.score:.1f}/10", size=11, color="#999")
                if self.score
                else None,
            ],
            spacing=6,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        return ft.Container(
            content=content,
            padding=ft.Padding(left=10, right=10, top=6, bottom=6),
            bgcolor=color,
            opacity=0.15,
            border_radius=6,
        )
