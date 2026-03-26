"""Responsive Burger Menu Component - Fixed Version"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig


def create_burger_menu(
    responsive: ResponsiveConfig,
    current_admin_view: str,
    on_dashboard: callable,
    on_queue: callable,
    on_detail: callable,
    on_insights: callable,
    on_analytics: callable,
    on_settings: callable,
    on_logout: callable,
    is_open: bool = False,
    on_close: callable = None,
):
    """
    Create a responsive burger menu overlay that actually works
    
    Args:
        responsive: ResponsiveConfig instance
        current_admin_view: Current active view name
        on_dashboard: Callback for dashboard
        on_queue: Callback for reports queue
        on_detail: Callback for report detail
        on_insights: Callback for AI insights
        on_analytics: Callback for analytics
        on_settings: Callback for settings
        on_logout: Callback for logout
        is_open: Whether menu is open
        on_close: Callback when menu closes
    
    Returns:
        ft.Container with menu overlay
    """

    def build_menu_item(icon, label, is_active, on_click_func):
        """Build a menu item with proper click handling"""
        
        def handle_click(e):
            """Handle menu item click"""
            if on_click_func:
                on_click_func(e)
        
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        icon,
                        size=24,
                        color=ft.Colors.WHITE if is_active else COLORS["text"],
                    ),
                    ft.Text(
                        label,
                        size=16,
                        weight="bold" if is_active else "normal",
                        color=ft.Colors.WHITE if is_active else COLORS["text"],
                    ),
                ],
                spacing=15,
            ),
            padding=ft.Padding(left=15, right=15, top=12, bottom=12),
            bgcolor=COLORS["primary"] if is_active else "transparent",
            border_radius=8,
            on_click=handle_click,
            ink=True,  # Add ripple effect
        )

    def handle_close_click(e):
        """Handle close button click"""
        if on_close:
            on_close(e)

    def handle_overlay_click(e):
        """Handle overlay background click"""
        if on_close:
            on_close(e)

    # Build menu items list
    menu_items = [
        # Header
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "SupportHub",
                        size=20,
                        weight="bold",
                        color=ft.Colors.WHITE,
                    ),
                    ft.Container(expand=True),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=ft.Colors.WHITE,
                        on_click=handle_close_click,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=COLORS["primary"],
        ),
        
        ft.Divider(height=1, color="#e0e0e0"),
        
        build_menu_item(
            ft.Icons.DASHBOARD,
            "Dashboard",
            current_admin_view == "dashboard",
            on_dashboard,
        ),
        build_menu_item(
            ft.Icons.LIST,
            "Reports Queue",
            current_admin_view == "queue",
            on_queue,
        ),
        build_menu_item(
            ft.Icons.DESCRIPTION,
            "Report Detail",
            current_admin_view == "detail",
            on_detail,
        ),
        build_menu_item(
            ft.Icons.INSIGHTS,
            "AI Insights",
            current_admin_view == "insights",
            on_insights,
        ),
        build_menu_item(
            ft.Icons.ANALYTICS,
            "Analytics",
            current_admin_view == "analytics",
            on_analytics,
        ),
        build_menu_item(
            ft.Icons.SETTINGS,
            "Settings",
            current_admin_view == "settings",
            on_settings,
        ),
        
        ft.Container(expand=True),
        
        ft.Divider(height=1, color="#e0e0e0"),
        
        build_menu_item(
            ft.Icons.LOGOUT,
            "Logout",
            False,
            on_logout,
        ),
    ]
    
    # Drawer menu content
    drawer = ft.Container(
        content=ft.Column(
            controls=menu_items,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        width=280,
        height=responsive.page_height,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            blur_radius=10,
            color="#00000030",
            offset=ft.Offset(2, 0),
        ),
    )

    # Overlay background
    overlay = ft.Container(
        bgcolor="#00000099",
        on_click=handle_overlay_click,
        expand=True,
    )

    # Menu layout: overlay takes remaining space, drawer is fixed width
    menu_row = ft.Row(
        controls=[
            drawer,
            overlay,
        ],
        spacing=0,
        expand=True,
    )

    # Top-level container with visibility control
    return ft.Container(
        content=menu_row,
        visible=is_open,
        expand=True,
    )


def create_burger_button(on_click: callable, size: int = 24):
    """
    Create burger menu button
    
    Args:
        on_click: Callback function
        size: Icon size
    
    Returns:
        ft.IconButton
    """
    return ft.IconButton(
        icon=ft.Icons.MENU,
        icon_size=size,
        icon_color=ft.Colors.WHITE,
        on_click=on_click,
        tooltip="Open menu",
    )