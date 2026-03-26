"""Admin Dashboard - Main Dashboard Overview Page"""

import flet as ft
from config.settings import COLORS


def create_dashboard_page():
    """Create main dashboard overview showing key metrics and recent activity"""

    def build_stat_card(title: str, value: str, color: str) -> ft.Container:
        """Build a statistics card"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(title, size=14, color=COLORS["text"]),
                    ft.Text(value, size=28, weight="bold", color=color),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=200,
            height=120,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            padding=15,
        )

    def build_activity_item(title: str, category: str, time: str) -> ft.Container:
        """Build an activity item"""
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(title, weight="bold", size=14, color=COLORS["text"]),
                            ft.Text(category, size=12, color=COLORS["secondary"]),
                        ]
                    ),
                    ft.Text(time, size=12, color="#999", text_align=ft.TextAlign.RIGHT),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            margin=ft.margin.only(bottom=10),
        )

    return ft.Container(
        content=ft.Column(
            controls=[
                # Header
                ft.Container(
                    content=ft.Text(
                        "Dashboard Overview",
                        size=32,
                        weight="bold",
                        color=COLORS["primary"],
                    ),
                    padding=20,
                ),
                # Statistics Cards Row
                ft.Row(
                    controls=[
                        build_stat_card("Total Reports", "127", COLORS["primary"]),
                        build_stat_card("High Severity", "12", COLORS["critical"]),
                        build_stat_card("Pending Review", "34", COLORS["warning"]),
                        build_stat_card("Resolved", "81", COLORS["success"]),
                    ],
                    spacing=10,
                    wrap=True,
                ),
                # Recent Activity Section
                ft.Divider(),
                ft.Text("Recent Activity", size=20, weight="bold", color=COLORS["primary"]),
                ft.ListView(
                    controls=[
                        build_activity_item(
                            "Report #1042 - Harassment Case",
                            "High Priority",
                            "2 hours ago",
                        ),
                        build_activity_item(
                            "Pattern Detected - Recurring Offender",
                            "Pattern Alert",
                            "4 hours ago",
                        ),
                        build_activity_item(
                            "Report #1038 - Resolved",
                            "Completed",
                            "1 day ago",
                        ),
                    ],
                    expand=True,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=20,
        bgcolor=COLORS["background"],
        expand=True,
    )
