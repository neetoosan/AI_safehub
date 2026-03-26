"""Reporter Submission Confirmation Screen"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text, create_responsive_button
from datetime import datetime


def create_reporter_confirmation_screen(report_id=None, on_continue=None, responsive=None):
    """Create submission confirmation screen for reporter"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    # Generate report ID if not provided
    if not report_id:
        report_id = f"RPT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def handle_continue(e):
        if on_continue:
            on_continue()
    
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=responsive.spacing_vertical()),
                
                # Success icon
                ft.Icon(
                    icon=ft.Icons.CHECK_CIRCLE,
                    size=responsive.icon_size() + 20,
                    color=COLORS["success"],
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Success message
                create_responsive_text(
                    "Thank You!",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                create_responsive_text(
                    "Your report has been submitted",
                    responsive,
                    size_type="h2",
                    color=COLORS["secondary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Report details
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    create_responsive_text("Report ID:", responsive, size_type="body", weight="bold"),
                                    create_responsive_text(report_id, responsive, size_type="body", color=COLORS["secondary"]),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Container(height=responsive.margin_medium()),
                            ft.Row(
                                controls=[
                                    create_responsive_text("Submitted:", responsive, size_type="body", weight="bold"),
                                    create_responsive_text(datetime.now().strftime("%Y-%m-%d %H:%M"), responsive, size_type="body", color=COLORS["secondary"]),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                        ],
                    ),
                    padding=responsive.padding_medium(),
                    bgcolor="#f9f9f9",
                    border_radius=responsive.border_radius(),
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # What happens next
                create_responsive_text(
                    "What happens next?",
                    responsive,
                    size_type="h3",
                    weight="bold",
                    color=COLORS["primary"],
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                # Steps
                *[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=create_responsive_text(
                                    str(i+1),
                                    responsive,
                                    size_type="body",
                                    color=ft.Colors.WHITE,
                                    weight="bold",
                                ),
                                width=30,
                                height=30,
                                bgcolor=COLORS["secondary"],
                                border_radius=50,
                            ),
                            create_responsive_text(step, responsive, size_type="small"),
                        ],
                        spacing=responsive.margin_medium(),
                        alignment=ft.MainAxisAlignment.START,
                    )
                    for i, step in enumerate([
                        "Our AI analyzes your report for patterns",
                        "Moderators review high-severity cases",
                        "Appropriate action is taken",
                        "You can track updates anonymously",
                    ])
                ],
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Privacy reminder
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.INFO,
                                color=COLORS["secondary"],
                            ),
                            create_responsive_text(
                                "Save your Report ID to track status",
                                responsive,
                                size_type="small",
                                color=COLORS["secondary"],
                            ),
                        ],
                        spacing=responsive.margin_small(),
                    ),
                    padding=responsive.padding_medium(),
                    bgcolor="#e6f2ff",
                    border_radius=responsive.border_radius(),
                ),
                
                ft.Container(height=responsive.spacing_vertical(), expand=True),
                
                # Continue button
                ft.Button(
                    content=create_responsive_text("Continue", responsive, color=ft.Colors.WHITE),
                    expand=True,
                    height=responsive.button_height(),
                    bgcolor=COLORS["primary"],
                    on_click=handle_continue,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        bgcolor=COLORS["background"],
        padding=responsive.padding_large(),
        expand=True,
    )
