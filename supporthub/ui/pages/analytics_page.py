"""Analytics and Trends Page"""

import flet as ft
from config.settings import COLORS


def create_analytics_page():
    """Analytics dashboard for reports, patterns, and trends"""

    def build_stat_card(title: str, value: str, color: str) -> ft.Container:
        """Build a statistics card"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(title, size=12, color=COLORS["text"]),
                    ft.Text(value, size=24, weight="bold", color=color),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=150,
            height=100,
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            padding=15,
        )

    def build_pattern_item(pattern: str, count: str, color: str):
        """Build a pattern item"""
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=8,
                        height=8,
                        bgcolor=color,
                        border_radius=4,
                    ),
                    ft.Text(pattern, expand=True),
                    ft.Text(count, size=12, color="#999"),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            margin=ft.margin.only(bottom=8),
        )

    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "Analytics & Trends",
                            size=32,
                            weight="bold",
                            color=COLORS["primary"],
                        ),
                        padding=20,
                    ),
                    ft.Divider(),
                    # Summary Stats
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                build_stat_card("Total Reports", "127", COLORS["primary"]),
                                build_stat_card("This Month", "42", COLORS["secondary"]),
                                build_stat_card("Patterns Found", "8", COLORS["warning"]),
                                build_stat_card("Resolution Rate", "78%", COLORS["success"]),
                            ],
                            spacing=10,
                            wrap=True,
                        ),
                        padding=20,
                    ),
                    ft.Divider(),
                    # Charts Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Report Trends (Last 30 Days)", weight="bold", size=16),
                                ft.Container(
                                    content=ft.Text(
                                        "[Chart placeholder - Reports over time]",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    height=300,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ]
                        ),
                        padding=20,
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Abuse Type Distribution", weight="bold", size=16),
                                ft.Container(
                                    content=ft.Text(
                                        "[Chart placeholder - Pie chart of abuse types]",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    height=300,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ]
                        ),
                        padding=20,
                    ),
                    # Top Patterns
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Top Recurring Patterns", weight="bold", size=16),
                                build_pattern_item(
                                    "Workplace Harassment",
                                    "12 incidents",
                                    COLORS["critical"],
                                ),
                                build_pattern_item(
                                    "Cyberbullying", "8 incidents", COLORS["warning"]
                                ),
                                build_pattern_item(
                                    "Discrimination", "6 incidents", COLORS["secondary"]
                                ),
                            ]
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
