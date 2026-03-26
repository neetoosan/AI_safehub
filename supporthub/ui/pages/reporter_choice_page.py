"""Reporter Choice Screen - Choose between Track or Report New Incident"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text


def create_reporter_choice_screen(on_track=None, on_report_new=None, on_back=None, responsive=None):
    """Create screen where reporter chooses between tracking or reporting"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    def handle_track(e):
        if on_track:
            on_track()
    
    def handle_report_new(e):
        if on_report_new:
            on_report_new()
    
    def handle_back(e):
        if on_back:
            on_back()
    
    card_width = responsive.card_width() if isinstance(responsive.card_width(), (int, float)) else 280
    card_height = responsive.card_height()
    icon_size = responsive.font_size_h2() + 20

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=responsive.spacing_vertical()),
                
                # Header
                create_responsive_text(
                    "Reporter Portal",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_small()),
                
                create_responsive_text(
                    "What would you like to do?",
                    responsive,
                    size_type="h2",
                    color=COLORS["text"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Track Incident Card
                ft.GestureDetector(
                    on_tap=handle_track,
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Icon(
                                    icon=ft.Icons.TRACK_CHANGES,
                                    size=icon_size,
                                    color=COLORS["secondary"],
                                ),
                                ft.Container(height=responsive.margin_medium()),
                                create_responsive_text(
                                    "Track an Incident",
                                    responsive,
                                    size_type="h2",
                                    weight="bold",
                                    color=COLORS["secondary"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=responsive.margin_small()),
                                create_responsive_text(
                                    "Check your report status",
                                    responsive,
                                    size_type="body",
                                    color=COLORS["text"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        width=card_width,
                        height=card_height,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=responsive.border_radius(),
                        padding=responsive.padding_medium(),
                        shadow=ft.BoxShadow(
                            blur_radius=8,
                            color="#00000015",
                        ),
                    ),
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Report New Incident Card
                ft.GestureDetector(
                    on_tap=handle_report_new,
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Icon(
                                    icon=ft.Icons.REPORT_PROBLEM,
                                    size=icon_size,
                                    color=COLORS["primary"],
                                ),
                                ft.Container(height=responsive.margin_medium()),
                                create_responsive_text(
                                    "Report a New Incident",
                                    responsive,
                                    size_type="h2",
                                    weight="bold",
                                    color=COLORS["primary"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=responsive.margin_small()),
                                create_responsive_text(
                                    "Submit a new anonymous report",
                                    responsive,
                                    size_type="body",
                                    color=COLORS["text"],
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                        ),
                        width=card_width,
                        height=card_height,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=responsive.border_radius(),
                        padding=responsive.padding_medium(),
                        shadow=ft.BoxShadow(
                            blur_radius=8,
                            color="#00000015",
                        ),
                    ),
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Back Button
                ft.Button(
                    content=create_responsive_text("Back", responsive, size_type="body", color=COLORS["primary"]),
                    expand=True,
                    height=responsive.button_height(),
                    bgcolor=COLORS["background"],
                    on_click=handle_back,
                ),
                
                ft.Container(expand=True),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        bgcolor=COLORS["background"],
        padding=responsive.padding_large(),
        expand=True,
    )
