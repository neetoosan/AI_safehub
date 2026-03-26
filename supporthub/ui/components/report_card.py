"""Report Card Component"""

import flet as ft
from config.settings import COLORS


class ReportCard(ft.Control):
    """Reusable report card component for displaying report summaries"""

    def __init__(self, report_id: str, title: str, severity: str, time: str):
        super().__init__()
        self.report_id = report_id
        self.title = title
        self.severity = severity
        self.time = time

    def build(self):
        severity_colors = {
            "Critical": COLORS["critical"],
            "High": COLORS["warning"],
            "Medium": COLORS["secondary"],
            "Low": COLORS["success"],
        }

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(f"#{self.report_id}", weight="bold", size=12),
                        bgcolor=COLORS["primary"],
                        opacity=0.1,
                        padding=10,
                        border_radius=4,
                        width=60,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(self.title, weight="bold", size=14),
                            ft.Text(self.time, size=11, color="#999"),
                        ],
                        expand=True,
                        spacing=2,
                    ),
                    ft.Container(
                        content=ft.Text(
                            self.severity,
                            size=11,
                            weight="bold",
                            color=ft.Colors.WHITE,
                        ),
                        bgcolor=severity_colors.get(self.severity, COLORS["secondary"]),
                        padding=ft.Padding(left=12, right=12, top=6, bottom=6),
                        border_radius=12,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            padding=12,
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            margin=ft.margin.only(bottom=8),
        )
