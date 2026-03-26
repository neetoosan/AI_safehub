"""Track Incident Screen - Check status of existing incident"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text


def create_reporter_track_screen(on_back=None, responsive=None):
    """Create screen for tracking existing incident by ID"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    tracking_id = ft.TextField(
        label="Tracking ID",
        hint_text="Enter your incident tracking ID (e.g., 1042)",
        width=responsive.input_width(),
        autofocus=True,
    )
    
    status_container = ft.Container(
        visible=False,
        content=ft.Column(
            controls=[],
            spacing=responsive.margin_medium(),
        ),
    )
    
    error_text = ft.Text(
        "",
        size=responsive.font_size_small(),
        color=COLORS["critical"],
        visible=False,
    )
    
    def handle_search(e):
        """Handle tracking ID search"""
        if not tracking_id.value:
            error_text.value = "Please enter a tracking ID"
            error_text.visible = True
            status_container.visible = False
        else:
            error_text.visible = False
            
            # Mock incident status lookup
            # In production, this would query a database or API
            incident_statuses = {
                "1042": {
                    "status": "Under Review",
                    "submitted": "2026-02-05 14:30",
                    "type": "Harassment",
                    "severity": "High",
                    "last_updated": "2026-02-06 10:15",
                },
                "1041": {
                    "status": "Resolved",
                    "submitted": "2026-02-03 09:15",
                    "type": "Bullying",
                    "severity": "Medium",
                    "last_updated": "2026-02-05 16:45",
                },
            }
            
            incident = incident_statuses.get(tracking_id.value.strip())
            
            if incident:
                # Display incident status
                status_color = COLORS["warning"] if incident["status"] == "Under Review" else COLORS["success"]
                
                status_container.content = ft.Column(
                    controls=[
                        ft.Container(height=responsive.margin_medium()),
                        
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    create_responsive_text(
                                        "Incident Status",
                                        responsive,
                                        size_type="h2",
                                        weight="bold",
                                        color=COLORS["primary"],
                                    ),
                                    
                                    ft.Container(height=responsive.margin_small()),
                                    
                                    ft.Divider(height=1, color=COLORS["border"]),
                                    
                                    ft.Container(height=responsive.margin_small()),
                                    
                                    ft.Row(
                                        controls=[
                                            create_responsive_text(
                                                "Tracking ID:",
                                                responsive,
                                                size_type="body",
                                                weight="bold",
                                                color=COLORS["text"],
                                            ),
                                            create_responsive_text(
                                                tracking_id.value.strip(),
                                                responsive,
                                                size_type="body",
                                                color=COLORS["secondary"],
                                            ),
                                        ],
                                        spacing=responsive.margin_small(),
                                    ),
                                    
                                    ft.Row(
                                        controls=[
                                            create_responsive_text(
                                                "Status:",
                                                responsive,
                                                size_type="body",
                                                weight="bold",
                                                color=COLORS["text"],
                                            ),
                                            create_responsive_text(
                                                incident["status"],
                                                responsive,
                                                size_type="body",
                                                color=status_color,
                                                weight="bold",
                                            ),
                                        ],
                                        spacing=responsive.margin_small(),
                                    ),
                                    
                                    ft.Row(
                                        controls=[
                                            create_responsive_text(
                                                "Type:",
                                                responsive,
                                                size_type="body",
                                                weight="bold",
                                                color=COLORS["text"],
                                            ),
                                            create_responsive_text(
                                                incident["type"],
                                                responsive,
                                                size_type="body",
                                                color=COLORS["text"],
                                            ),
                                        ],
                                        spacing=responsive.margin_small(),
                                    ),
                                    
                                    ft.Row(
                                        controls=[
                                            create_responsive_text(
                                                "Severity:",
                                                responsive,
                                                size_type="body",
                                                weight="bold",
                                                color=COLORS["text"],
                                            ),
                                            create_responsive_text(
                                                incident["severity"],
                                                responsive,
                                                size_type="body",
                                                color=COLORS["critical"] if incident["severity"] == "High" else COLORS["warning"],
                                            ),
                                        ],
                                        spacing=responsive.margin_small(),
                                    ),
                                    
                                    ft.Row(
                                        controls=[
                                            create_responsive_text(
                                                "Submitted:",
                                                responsive,
                                                size_type="body",
                                                weight="bold",
                                                color=COLORS["text"],
                                            ),
                                            create_responsive_text(
                                                incident["submitted"],
                                                responsive,
                                                size_type="body",
                                                color=COLORS["text"],
                                            ),
                                        ],
                                        spacing=responsive.margin_small(),
                                    ),
                                    
                                    ft.Row(
                                        controls=[
                                            create_responsive_text(
                                                "Last Updated:",
                                                responsive,
                                                size_type="body",
                                                weight="bold",
                                                color=COLORS["text"],
                                            ),
                                            create_responsive_text(
                                                incident["last_updated"],
                                                responsive,
                                                size_type="body",
                                                color=COLORS["text"],
                                            ),
                                        ],
                                        spacing=responsive.margin_small(),
                                    ),
                                ],
                            ),
                            bgcolor=ft.Colors.WHITE,
                            border_radius=responsive.border_radius(),
                            padding=responsive.padding_medium(),
                            shadow=ft.BoxShadow(
                                blur_radius=4,
                                color="#00000010",
                            ),
                        ),
                    ],
                )
                status_container.visible = True
            else:
                error_text.value = f"No incident found with tracking ID: {tracking_id.value.strip()}"
                error_text.visible = True
                status_container.visible = False
        
        tracking_id.page.update()
    
    def handle_back(e):
        if on_back:
            on_back()
    
    return ft.Container(
        content=ft.Column(
            controls=[
                # Header
                create_responsive_text(
                    "Track an Incident",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                create_responsive_text(
                    "Enter your tracking ID to check the status of your report",
                    responsive,
                    size_type="small",
                    color=COLORS["secondary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Tracking ID Input
                tracking_id,
                
                ft.Container(height=responsive.margin_medium()),
                
                # Error message
                error_text,
                
                # Search Button
                ft.Button(
                    content=create_responsive_text("Search", responsive, size_type="body", color=ft.Colors.WHITE),
                    expand=True,
                    height=responsive.button_height(),
                    bgcolor=COLORS["secondary"],
                    on_click=handle_search,
                ),
                
                # Status Display Container
                status_container,
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Back Button
                ft.Button(
                    content=create_responsive_text("Back", responsive, size_type="body", color=COLORS["primary"]),
                    expand=True,
                    height=responsive.button_height(),
                    bgcolor=COLORS["background"],
                    on_click=handle_back,
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
