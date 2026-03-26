"""Welcome Screen - First screen shown when opening the app"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text


def create_welcome_screen(on_continue=None, responsive=None):
    """Create welcome screen with app introduction"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    def handle_continue(e):
        if on_continue:
            on_continue()

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=responsive.spacing_vertical()),  # Spacer
                
                # Logo/Icon area
                ft.Container(
                    content=ft.Icon(
                        icon=ft.Icons.VERIFIED_USER,
                        size=responsive.icon_size(),
                        color=COLORS["primary"],
                    ),
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                # Title
                create_responsive_text(
                    "AI SupportHub",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                # Subtitle
                create_responsive_text(
                    "Safe. Anonymous. Fair.",
                    responsive,
                    size_type="h2",
                    color=COLORS["secondary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Description
                ft.Container(
                    content=create_responsive_text(
                        "A secure platform for reporting harassment and abuse in schools, "
                        "workplaces, and communities.\n\n"
                        "• Anonymous reporting\n"
                        "• AI-powered analysis\n"
                        "• Fair & transparent\n"
                        "• Confidential handling",
                        responsive,
                        size_type="body",
                        color=COLORS["text"],
                        text_align=ft.TextAlign.CENTER,
                    ),
                    padding=responsive.padding_medium(),
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Continue Button - Responsive sizing
                ft.Button(
                    content=create_responsive_text("Get Started", responsive, size_type="body", color=ft.Colors.WHITE),
                    width=responsive.button_width_flexible(),
                    height=responsive.button_height(),
                    bgcolor=COLORS["primary"],
                    on_click=handle_continue,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Footer text
                create_responsive_text(
                    "Your safety is our priority",
                    responsive,
                    size_type="small",
                    color="#999",
                    text_align=ft.TextAlign.CENTER,
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
