"""Settings Page for Admin Configuration"""

import flet as ft
from config.settings import COLORS


def create_settings_page():
    """Admin settings and system configuration"""
    
    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "System Settings",
                            size=32,
                            weight="bold",
                            color=COLORS["primary"],
                        ),
                        padding=20,
                    ),
                    ft.Divider(),
                    # General Settings
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("General Settings", weight="bold", size=16),
                                ft.TextField(label="Organization Name", value="My School"),
                                ft.TextField(label="Contact Email"),
                                ft.Dropdown(
                                    label="Report Language",
                                    options=[
                                        ft.dropdown.Option("English"),
                                        ft.dropdown.Option("Spanish"),
                                        ft.dropdown.Option("French"),
                                    ],
                                ),
                            ],
                            spacing=15,
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=8,
                        margin=ft.margin.only(bottom=20),
                    ),
                    # Security Settings
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Security Settings", weight="bold", size=16),
                                ft.Row(
                                    controls=[
                                        ft.Text("Two-Factor Authentication"),
                                        ft.Switch(value=True),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Session Timeout (minutes)"),
                                        ft.TextField(value="30", width=100),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                ),
                            ],
                            spacing=15,
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=8,
                        margin=ft.margin.only(bottom=20),
                    ),
                    # Notification Settings
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Notification Settings", weight="bold", size=16),
                                ft.Row(
                                    controls=[
                                        ft.Text("Critical Reports"),
                                        ft.Switch(value=True),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Pattern Detected"),
                                        ft.Switch(value=True),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Daily Summary"),
                                        ft.Switch(value=False),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                ),
                            ],
                            spacing=15,
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=8,
                        margin=ft.margin.only(bottom=20),
                    ),
                    # Save Button
                    ft.ElevatedButton(
                        content=ft.Text("Save Settings"),
                        width=150,
                        bgcolor=COLORS["primary"],
                        color=ft.Colors.WHITE,
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
