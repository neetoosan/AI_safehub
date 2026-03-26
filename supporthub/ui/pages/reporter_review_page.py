"""Reporter Review & Submit Screen"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text, create_responsive_button


def create_reporter_review_screen(report_data=None, on_submit=None, on_back=None, responsive=None):
    """Create review and submit screen for reporter"""
    
    if report_data is None:
        report_data = {}
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    def handle_submit(e):
        if on_submit:
            on_submit(report_data)
    
    def handle_back(e):
        if on_back:
            on_back()
    
    # Build review sections
    review_items = []
    
    if "incident_type" in report_data:
        review_items.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        create_responsive_text("Type of Incident", responsive, size_type="body", weight="bold", color=COLORS["primary"]),
                        create_responsive_text(report_data.get("incident_type", ""), responsive, size_type="small"),
                    ]
                ),
                padding=responsive.padding_medium(),
                bgcolor="#f9f9f9",
                border_radius=responsive.border_radius(),
            )
        )
    
    if "description" in report_data:
        review_items.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        create_responsive_text("Description", responsive, size_type="body", weight="bold", color=COLORS["primary"]),
                        create_responsive_text(report_data.get("description", ""), responsive, size_type="small"),
                    ]
                ),
                padding=responsive.padding_medium(),
                bgcolor="#f9f9f9",
                border_radius=responsive.border_radius(),
            )
        )
    
    if "when_occurred" in report_data:
        review_items.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        create_responsive_text("When", responsive, size_type="body", weight="bold", color=COLORS["primary"]),
                        create_responsive_text(report_data.get("when_occurred", ""), responsive, size_type="small"),
                    ]
                ),
                padding=responsive.padding_medium(),
                bgcolor="#f9f9f9",
                border_radius=responsive.border_radius(),
            )
        )
    
    if "evidence_types" in report_data and report_data["evidence_types"]:
        review_items.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        create_responsive_text("Evidence", responsive, size_type="body", weight="bold", color=COLORS["primary"]),
                        create_responsive_text(", ".join(report_data.get("evidence_types", [])), responsive, size_type="small"),
                    ]
                ),
                padding=responsive.padding_medium(),
                bgcolor="#f9f9f9",
                border_radius=responsive.border_radius(),
            )
        )
    
    return ft.Container(
        content=ft.Column(
            controls=[
                # Header
                create_responsive_text(
                    "Review Your Report",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                create_responsive_text(
                    "Please review your information before submitting",
                    responsive,
                    size_type="small",
                    color=COLORS["secondary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Progress indicator
                create_responsive_text(
                    "Step 3 of 4: Review",
                    responsive,
                    size_type="small",
                    color="#999",
                    weight="bold",
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Review items
                *review_items,
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Privacy notice
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(
                                        icon=ft.Icons.VERIFIED_USER,
                                        color=COLORS["success"],
                                        size=20,
                                    ),
                                    create_responsive_text(
                                        "Your identity is completely protected",
                                        responsive,
                                        size_type="small",
                                        color=COLORS["success"],
                                        weight="bold",
                                    ),
                                ],
                                spacing=responsive.margin_small(),
                            ),
                            ft.Container(height=responsive.margin_small()),
                            create_responsive_text(
                                "Your report will be processed by our AI system to identify harassment patterns and ensure fair treatment. No personal information will be stored.",
                                responsive,
                                size_type="caption",
                                color="#666",
                            ),
                        ]
                    ),
                    padding=responsive.padding_medium(),
                    bgcolor="#f0fdf4",
                    border_radius=responsive.border_radius(),
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Buttons
                ft.Row(
                    controls=[
                        ft.Button(
                            content=create_responsive_text("Back", responsive, size_type="body", color=COLORS["primary"]),
                            expand=True,
                            height=responsive.button_height(),
                            bgcolor=COLORS["background"],
                            on_click=handle_back,
                        ),
                        ft.Button(
                            content=create_responsive_text("Submit Report", responsive, size_type="body", color=ft.Colors.WHITE),
                            expand=True,
                            height=responsive.button_height(),
                            bgcolor=COLORS["primary"],
                            on_click=handle_submit,
                        ),
                    ],
                    spacing=responsive.margin_medium(),
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
