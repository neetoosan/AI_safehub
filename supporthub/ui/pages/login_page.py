"""Admin Login Page"""

import flet as ft
from config.settings import COLORS
from utils.responsive import get_responsive_config
from ui.components.styled_inputs import (
    create_styled_text_field,
    create_styled_button,
    create_error_message,
)


def create_login_page(on_login=None, responsive=None):
    """Create admin/moderator login authentication page"""
    
    if responsive is None:
        responsive = get_responsive_config(ft.Page())
    
    # Create styled inputs
    email_container, email_input, email_error = create_styled_text_field(
        label="Email Address",
        responsive=responsive,
        hint_text="Enter your email",
        icon=ft.Icons.EMAIL,
    )
    
    password_container, password_input, password_error = create_styled_text_field(
        label="Password",
        responsive=responsive,
        hint_text="Enter your password",
        icon=ft.Icons.LOCK,
        password=True,
    )
    
    error_message = ft.Column(visible=False)
    
    def handle_login(e):
        # Clear previous errors
        email_error.visible = False
        password_error.visible = False
        error_message.visible = False
        error_message.controls.clear()
        
        # Validate
        if not email_input.value:
            email_error.value = "Email is required"
            email_error.visible = True
            return
        
        if "@" not in email_input.value:
            email_error.value = "Please enter a valid email"
            email_error.visible = True
            return
        
        if not password_input.value:
            password_error.value = "Password is required"
            password_error.visible = True
            return
        
        if len(password_input.value) < 6:
            password_error.value = "Password must be at least 6 characters"
            password_error.visible = True
            return
        
        if on_login:
            on_login(email_input.value, password_input.value)
    
    login_button = create_styled_button(
        "Login to Dashboard",
        responsive,
        on_click=handle_login,
        button_type="primary",
    )
    
    forgot_password_link = ft.TextButton(
        "Forgot Password?",
        on_click=lambda e: None,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=40),  # Spacer
                ft.Text(
                    "AI SupportHub",
                    size=36,
                    weight="bold",
                    color=COLORS["primary"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Admin Login",
                    size=20,
                    weight="500",
                    color=COLORS["text"],
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=30),
                
                # Email field
                email_container,
                
                # Password field
                password_container,
                
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(expand=True),
                            forgot_password_link,
                        ]
                    ),
                    padding=ft.Padding(bottom=10),
                ),
                
                # Error message area
                error_message,
                
                # Login button
                login_button,
                
                ft.Container(expand=True),
                
                ft.Text(
                    "Don't have an account? Register your organization",
                    size=12,
                    color="#999",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=responsive.padding_large(),
        bgcolor=COLORS["background"],
        expand=True,
    )
