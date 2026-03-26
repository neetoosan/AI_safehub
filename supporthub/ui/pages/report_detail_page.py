"""Report Detail View Page"""

import flet as ft
from config.settings import COLORS


def create_report_detail_page(report_id: str = "1045"):
    """Detailed view of a single report with evidence and case actions"""
    
    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    # Header with Report ID
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            f"Report #{report_id}",
                                            size=28,
                                            weight="bold",
                                            color=COLORS["primary"],
                                        ),
                                        ft.Text(
                                            "Submitted 2 hours ago",
                                            size=12,
                                            color="#999",
                                        ),
                                    ]
                                ),
                                ft.Container(
                                        content=ft.Container(
                                            content=ft.Text("CRITICAL", color=ft.Colors.WHITE, size=12),
                                            bgcolor=COLORS["critical"],
                                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                            border_radius=12,
                                        ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        padding=20,
                    ),
                    ft.Divider(),
                    # Report Content
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Incident Description", weight="bold", size=16),
                                ft.Container(
                                    content=ft.Text(
                                        "This is a detailed description of the harassment incident reported by the anonymous user. "
                                        "The report contains contextual information and severity indicators.",
                                        size=12,
                                        color=COLORS["text"],
                                    ),
                                    padding=10,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=8,
                                ),
                            ],
                        ),
                        padding=20,
                    ),
                    # Evidence Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Evidence & Attachments", weight="bold", size=16),
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.Icons.IMAGE,
                                                            size=30,
                                                            color=COLORS["secondary"],
                                                        ),
                                                        ft.Text("screenshot.png", size=10),
                                                    ],
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                ),
                                                width=80,
                                                height=80,
                                                bgcolor=ft.Colors.WHITE,
                                                border_radius=8,
                                            ),
                                            ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Icon(
                                                            ft.Icons.AUDIO_FILE,
                                                            size=30,
                                                            color=COLORS["secondary"],
                                                        ),
                                                        ft.Text("audio.mp3", size=10),
                                                    ],
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                ),
                                                width=80,
                                                height=80,
                                                bgcolor=ft.Colors.WHITE,
                                                border_radius=8,
                                            ),
                                        ],
                                        spacing=10,
                                        wrap=True,
                                    ),
                                    padding=10,
                                ),
                            ],
                        ),
                        padding=20,
                    ),
                    # Case Action Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Case Actions & Notes", weight="bold", size=16),
                                ft.TextField(
                                    label="Add case notes",
                                    multiline=True,
                                    min_lines=3,
                                    max_lines=5,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Button(
                                            content=ft.Text(
                                                "Escalate",
                                                color=COLORS["critical"],
                                            ),
                                        ),
                                        ft.Button(
                                            content=ft.Text(
                                                "Mark Resolved",
                                                color=COLORS["success"],
                                            ),
                                        ),
                                        ft.OutlinedButton(content=ft.Text("Reassign")),
                                    ],
                                    spacing=10,
                                    wrap=True,
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
