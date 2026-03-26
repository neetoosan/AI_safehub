"""Sidebar Navigation Component"""

import flet as ft
from config.settings import COLORS


class Sidebar(ft.Control):
    """Left sidebar with navigation menu"""

    def __init__(self, on_nav_change=None):
        super().__init__()
        self.on_nav_change = on_nav_change
        self.width = 250

    def build(self):
        nav_items = [
            ("Dashboard", ft.icons.HOME),
            ("Reports Queue", ft.icons.LIST_ALT),
            ("AI Insights", ft.icons.AUTO_AWESOME),
            ("Analytics", ft.icons.TRENDING_UP),
            ("Settings", ft.icons.SETTINGS),
            ("Audit Logs", ft.icons.HISTORY),
        ]

        nav_buttons = []
        for label, icon in nav_items:
            nav_buttons.append(
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Icon(icon, color=COLORS["primary"]),
                            ft.Text(label),
                        ],
                        spacing=10,
                    ),
                    width=250,
                    on_click=lambda e, l=label: self.on_nav_change(l)
                    if self.on_nav_change
                    else None,
                    style=ft.ButtonStyle(
                        color=COLORS["text"],
                        bgcolor={
                            ft.MaterialState.HOVERED: COLORS["background"],
                        },
                    ),
                )
            )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "SupportHub",
                            size=20,
                            weight="bold",
                            color=COLORS["primary"],
                        ),
                        padding=15,
                    ),
                    ft.Divider(),
                    *nav_buttons,
                    ft.Container(expand=True),
                    ft.Divider(),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.LOGOUT, color=COLORS["critical"]),
                                ft.Text("Logout", color=COLORS["critical"]),
                            ],
                            spacing=10,
                        ),
                        width=250,
                    ),
                ],
                spacing=0,
            ),
            bgcolor=ft.Colors.WHITE,
            border_radius=0,
            shadow=ft.BoxShadow(blur_radius=5, color="#00000010"),
        )
