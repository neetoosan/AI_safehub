"""Admin Organization Registration Screen"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text, create_responsive_button


def create_admin_registration_screen(on_register=None, on_back=None, responsive=None):
    """Create admin organization registration form"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    # Form fields
    org_name = ft.TextField(
        label="Organization Name",
        hint_text="e.g., My School, ABC Corporation",
        width=responsive.input_width(),
    )
    
    org_type = ft.Dropdown(
        label="Organization Type",
        width=responsive.input_width(),
        options=[
            ft.dropdown.Option("Educational Institution"),
            ft.dropdown.Option("Corporate/Business"),
            ft.dropdown.Option("NGO/Non-profit"),
            ft.dropdown.Option("Government"),
            ft.dropdown.Option("Community Organization"),
            ft.dropdown.Option("Other"),
        ],
    )
    
    contact_email = ft.TextField(
        label="Contact Email",
        hint_text="admin@organization.com",
        width=responsive.input_width(),
    )
    
    admin_name = ft.TextField(
        label="Admin Full Name",
        hint_text="Your full name",
        width=responsive.input_width(),
    )
    
    admin_email = ft.TextField(
        label="Admin Email",
        hint_text="your.email@organization.com",
        width=responsive.input_width(),
    )
    
    admin_password = ft.TextField(
        label="Password",
        hint_text="Create a strong password",
        password=True,
        width=responsive.input_width(),
    )
    
    confirm_password = ft.TextField(
        label="Confirm Password",
        password=True,
        width=responsive.input_width(),
    )
    
    # Status message
    status_text = ft.Text(
        "",
        size=responsive.font_size_small(),
        color=COLORS["critical"],
        visible=False,
    )
    
    def handle_register(e):
        # Validation
        if not org_name.value:
            status_text.value = "Organization name is required"
            status_text.visible = True
        elif not org_type.value:
            status_text.value = "Organization type is required"
            status_text.visible = True
        elif not admin_name.value:
            status_text.value = "Admin name is required"
            status_text.visible = True
        elif not admin_email.value:
            status_text.value = "Admin email is required"
            status_text.visible = True
        elif not admin_password.value:
            status_text.value = "Password is required"
            status_text.visible = True
        elif admin_password.value != confirm_password.value:
            status_text.value = "Passwords do not match"
            status_text.visible = True
        else:
            # Registration successful
            status_text.value = ""
            status_text.visible = False
            
            if on_register:
                org_data = {
                    "org_name": org_name.value,
                    "org_type": org_type.value,
                    "contact_email": contact_email.value,
                    "admin_name": admin_name.value,
                    "admin_email": admin_email.value,
                }
                on_register(org_data)
    
    def handle_back(e):
        if on_back:
            on_back()

    return ft.Container(
        content=ft.Column(
            controls=[
                # Header
                create_responsive_text(
                    "Organization Registration",
                    responsive,
                    size_type="h1",
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.margin_medium()),
                
                create_responsive_text(
                    "Create your admin account and set up your organization",
                    responsive,
                    size_type="body",
                    color=COLORS["text"],
                    text_align=ft.TextAlign.CENTER,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Organization Info Section
                create_responsive_text(
                    "Organization Details",
                    responsive,
                    size_type="h3",
                    weight="bold",
                    color=COLORS["primary"],
                ),
                
                org_name,
                org_type,
                contact_email,
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Admin Info Section
                create_responsive_text(
                    "Admin Account",
                    responsive,
                    size_type="h3",
                    weight="bold",
                    color=COLORS["primary"],
                ),
                
                admin_name,
                admin_email,
                admin_password,
                confirm_password,
                
                ft.Container(height=responsive.spacing_vertical()),
                
                # Status message
                status_text,
                
                ft.Container(height=responsive.margin_medium()),
                
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
                            content=create_responsive_text("Create Account", responsive, size_type="body", color=ft.Colors.WHITE),
                            expand=True,
                            height=responsive.button_height(),
                            bgcolor=COLORS["primary"],
                            on_click=handle_register,
                        ),
                    ],
                    spacing=responsive.margin_medium(),
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                
                ft.Container(height=responsive.spacing_vertical()),
                
                create_responsive_text(
                    "By registering, you agree to our Terms of Service and Privacy Policy",
                    responsive,
                    size_type="caption",
                    color="#999",
                    text_align=ft.TextAlign.CENTER,
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
