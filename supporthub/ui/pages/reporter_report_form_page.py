"""Reporter Anonymous Report Form - Incident Details Screen"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text, create_responsive_button


def create_reporter_report_form_screen(on_next=None, on_back=None, responsive=None):
    """Create anonymous report form for incident details"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    # Organization field (NEW - Required)
    organization = ft.Dropdown(
        label="Select Your Organization *",
        hint_text="Choose the organization you're reporting to",
        width=responsive.input_width(),
        options=[
            ft.dropdown.Option("Springfield High School"),
            ft.dropdown.Option("Tech Corp Inc."),
            ft.dropdown.Option("Riverside University"),
            ft.dropdown.Option("Green Valley Middle School"),
            ft.dropdown.Option("Downtown Community Center"),
            ft.dropdown.Option("Metro Hospital"),
            ft.dropdown.Option("Other"),
        ],
    )
    
    incident_type = ft.Dropdown(
        label="Type of Incident",
        width=responsive.input_width(),
        options=[
            ft.dropdown.Option("Harassment"),
            ft.dropdown.Option("Discrimination"),
            ft.dropdown.Option("Bullying"),
            ft.dropdown.Option("Threat/Intimidation"),
            ft.dropdown.Option("Assault"),
            ft.dropdown.Option("Other"),
        ],
    )
    
    incident_description = ft.TextField(
        label="Describe what happened",
        hint_text="Provide as much detail as you feel comfortable sharing...",
        multiline=True,
        min_lines=responsive.text_field_multiline_min_lines(),
        max_lines=responsive.text_field_multiline_max_lines(),
        width=responsive.input_width(),
    )
    
    when_occurred = ft.Dropdown(
        label="When did this happen?",
        width=responsive.input_width(),
        options=[
            ft.dropdown.Option("Today"),
            ft.dropdown.Option("Within the past week"),
            ft.dropdown.Option("Within the past month"),
            ft.dropdown.Option("More than a month ago"),
            ft.dropdown.Option("Ongoing"),
        ],
    )
    
    location = ft.TextField(
        label="Where did this happen?",
        hint_text="e.g., Classroom, Meeting, Online Platform",
        width=responsive.input_width(),
    )
    
    witness_count = ft.TextField(
        label="Number of witnesses (optional)",
        hint_text="How many people witnessed this?",
        input_filter=ft.NumbersOnlyInputFilter(),
        width=responsive.input_width(),
    )
    
    status_text = ft.Text(
        "",
        size=responsive.font_size_small(),
        color=COLORS["critical"],
        visible=False,
    )
    
    def handle_continue(e):
        # Validate organization field first
        if not organization.value:
            status_text.value = "Please select your organization"
            status_text.visible = True
        elif not incident_type.value:
            status_text.value = "Please select incident type"
            status_text.visible = True
        elif not incident_description.value or len(incident_description.value) < 10:
            status_text.value = "Please provide detailed description (at least 10 characters)"
            status_text.visible = True
        elif not when_occurred.value:
            status_text.value = "Please select when this happened"
            status_text.visible = True
        else:
            status_text.visible = False
            if on_next:
                report_data = {
                    "organization": organization.value,
                    "incident_type": incident_type.value,
                    "description": incident_description.value,
                    "when_occurred": when_occurred.value,
                    "location": location.value,
                    "witness_count": int(witness_count.value) if witness_count.value else 0,
                }
                on_next(report_data)
    
    def handle_back(e):
        if on_back:
            on_back()
    
    return ft.Container(
        content=ft.Column(
            controls=[
                # Header
                create_responsive_text(
                    "Report an Incident",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                create_responsive_text(
                    "Your report is anonymous and confidential",
                    responsive,
                    size_type="small",
                    color=COLORS["secondary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Progress indicator
                create_responsive_text(
                    "Step 1 of 4: Incident Details",
                    responsive,
                    size_type="small",
                    color="#999",
                    weight="bold",
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                # Form fields - Organization FIRST
                organization,
                ft.Container(height=10),  # Small spacing after organization
                incident_type,
                incident_description,
                when_occurred,
                location,
                witness_count,
                
                ft.Container(height=responsive.margin_medium()),
                
                # Status message
                status_text,
                
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
                            content=create_responsive_text("Next", responsive, size_type="body", color=ft.Colors.WHITE),
                            expand=True,
                            height=responsive.button_height(),
                            bgcolor=COLORS["primary"],
                            on_click=handle_continue,
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
