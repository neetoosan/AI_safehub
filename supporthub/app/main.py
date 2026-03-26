"""App initialization and entry point - WITH WINDOW RESIZE HANDLING"""

import sys
import os

# Add supporthub directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import flet as ft
from config.settings import APP_NAME, COLORS
from utils.responsive import get_responsive_config
from services.evidence_service import EvidenceService
from ui import create_login_page, create_dashboard_page
from ui.pages.welcome_page import create_welcome_screen
from ui.pages.who_are_you_page import create_who_are_you_screen
from ui.pages.admin_registration_page import create_admin_registration_screen
from ui.pages.reporter_track_or_report_page import create_reporter_track_or_report_page
from ui.pages.reporter_report_form_page import create_reporter_report_form_screen
from ui.pages.reporter_track_page import create_reporter_track_screen
from ui.pages.reporter_evidence_page import create_reporter_evidence_screen
from ui.pages.reporter_review_page import create_reporter_review_screen
from ui.pages.reporter_confirmation_page import create_reporter_confirmation_screen
from ui.pages.reports_queue_page import create_reports_queue_page
from ui.pages.report_detail_page import create_report_detail_page
from ui.pages.ai_insights_page import create_ai_insights_page
from ui.pages.analytics_page import create_analytics_page
from ui.pages.settings_page import create_settings_page
from ui.components.burger_menu import create_burger_menu, create_burger_button


def main(page: ft.Page):
    """Main application entry point"""
    page.title = APP_NAME
    page.window_width = 1400
    page.window_height = 900
    page.bgcolor = COLORS["background"]
    
    # Enable responsiveness
    page.window_resizable = True
    page.window_min_width = 360
    page.window_min_height = 600

    # Get responsive config
    responsive = get_responsive_config(page)

    # Application state
    current_user = None
    current_role = None  # "admin" or "reporter"
    current_admin_view = "dashboard"  # Track which admin page is shown
    report_data = {}  # Accumulates data through report form screens
    selected_report_id = None  # For viewing report details
    menu_open = False  # Track burger menu state
    
    # ===== WINDOW RESIZE HANDLER =====
    
    def handle_window_resize(e):
        """Handle window resize events - update responsive config and rebuild UI"""
        nonlocal responsive
        
        # Update responsive config with new dimensions
        responsive.page_width = int(page.window_width)
        responsive.page_height = int(page.window_height)
        responsive.device_type = responsive._detect_device_type()
        
        print(f"Window resized: {responsive.page_width}x{responsive.page_height} - Device: {responsive.device_type}")
        
        # Rebuild current view if in admin dashboard
        if current_role == "admin" and current_user:
            build_admin_dashboard_view()
    
    # Register resize handler
    page.on_resize = handle_window_resize
    
    # ===== WELCOME & ONBOARDING FLOWS =====
    
    def show_welcome():
        """Show welcome screen"""
        page.clean()
        
        def handle_continue():
            show_who_are_you()
        
        welcome = create_welcome_screen(on_continue=handle_continue, responsive=responsive)
        page.add(welcome)
        page.update()
    
    def show_who_are_you():
        """Show role selection screen"""
        page.clean()
        
        def handle_reporter():
            nonlocal current_role
            current_role = "reporter"
            show_track_or_report_choice()
        
        def handle_admin():
            nonlocal current_role
            current_role = "admin"
            show_admin_login_choice()
        
        who_are_you = create_who_are_you_screen(
            on_reporter=handle_reporter,
            on_admin=handle_admin,
            responsive=responsive
        )
        page.add(who_are_you)
        page.update()
    
    # ===== ADMIN FLOW =====
    
    def show_admin_login_choice():
        """Show choice between login and registration"""
        page.clean()
        
        # Simple choice page
        def handle_login_choice(e):
            show_admin_login()
        
        def handle_register_choice(e):
            show_admin_registration()
        
        def handle_back(e):
            show_who_are_you()
        
        choice_page = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=responsive.spacing_vertical()),
                    
                    ft.Text(
                        "Admin Access",
                        size=responsive.font_size_h1(),
                        weight="bold",
                        color=COLORS["primary"],
                        text_align=ft.TextAlign.CENTER,
                    ),
                    
                    ft.Container(height=responsive.margin_medium()),
                    
                    ft.Text(
                        "Do you have an existing account or are you registering your organization?",
                        size=responsive.font_size_body(),
                        color=COLORS["text"],
                        text_align=ft.TextAlign.CENTER,
                    ),
                    
                    ft.Container(height=responsive.spacing_vertical()),
                    
                    ft.Button(
                        content=ft.Text("Login to Existing Account", color=ft.Colors.WHITE),
                        expand=True,
                        height=responsive.button_height(),
                        bgcolor=COLORS["primary"],
                        on_click=handle_login_choice,
                    ),
                    
                    ft.Container(height=responsive.margin_medium()),
                    
                    ft.Button(
                        content=ft.Text("Register New Organization", color=ft.Colors.WHITE),
                        expand=True,
                        height=responsive.button_height(),
                        bgcolor=COLORS["secondary"],
                        on_click=handle_register_choice,
                    ),
                    
                    ft.Container(height=responsive.spacing_vertical()),
                    
                    ft.Button(
                        content=ft.Text("Back", color=COLORS["primary"]),
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
            padding=responsive.padding_large(),
            bgcolor=COLORS["background"],
            expand=True,
        )
        
        page.add(choice_page)
        page.update()
    
    def show_admin_login():
        """Show admin login page"""
        page.clean()
        
        def handle_login(email, password):
            # Mock authentication
            if email and password:
                nonlocal current_user
                current_user = {
                    "role": "admin",
                    "email": email,
                    "organization": "Sample Organization",
                }
                show_admin_dashboard()
        
        def handle_back():
            show_admin_login_choice()
        
        login_page = create_login_page(on_login=handle_login, responsive=responsive)
        
        # Wrap login page with back button
        page_with_back = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.ARROW_BACK,
                                    on_click=lambda e: handle_back(),
                                ),
                                ft.Text("Back", size=responsive.font_size_body()),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=responsive.padding_medium(),
                    ),
                    login_page,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
        )
        
        page.add(page_with_back)
        page.update()
    
    def show_admin_registration():
        """Show admin organization registration form"""
        page.clean()
        
        def handle_register(org_data):
            nonlocal current_user
            current_user = {
                "role": "admin",
                "organization": org_data["org_name"],
                "admin_name": org_data["admin_name"],
                "admin_email": org_data["admin_email"],
            }
            show_admin_dashboard()
        
        def handle_back():
            show_admin_login_choice()
        
        registration = create_admin_registration_screen(on_register=handle_register, on_back=handle_back, responsive=responsive)
        page.add(registration)
        page.update()
    
    # ===== ADMIN DASHBOARD & SUBPAGES =====
    
    def show_admin_dashboard():
        """Show admin dashboard with navigation"""
        nonlocal current_admin_view
        current_admin_view = "dashboard"
        build_admin_dashboard_view()
    
    def show_reports_queue():
        """Show reports queue page"""
        nonlocal current_admin_view
        current_admin_view = "queue"
        build_admin_dashboard_view()
    
    def show_report_detail(report_id):
        """Show report detail page"""
        nonlocal current_admin_view, selected_report_id
        current_admin_view = "detail"
        selected_report_id = report_id
        build_admin_dashboard_view()
    
    def show_ai_insights():
        """Show AI insights page"""
        nonlocal current_admin_view
        current_admin_view = "insights"
        build_admin_dashboard_view()
    
    def show_analytics():
        """Show analytics page"""
        nonlocal current_admin_view
        current_admin_view = "analytics"
        build_admin_dashboard_view()
    
    def show_settings():
        """Show settings page"""
        nonlocal current_admin_view
        current_admin_view = "settings"
        build_admin_dashboard_view()
    
    def build_admin_dashboard_view():
        """Build and display admin dashboard with burger menu"""
        nonlocal menu_open
        page.clean()
        
        # CRITICAL: Refresh responsive config based on CURRENT window size
        responsive.page_width = int(page.window_width)
        responsive.page_height = int(page.window_height)
        responsive.device_type = responsive._detect_device_type()
        
        print(f"Building admin view - Width: {responsive.page_width}, Device: {responsive.device_type}, Mobile: {responsive.is_mobile()}")
        
        def handle_logout(e):
            """Handle logout - close menu and return to welcome"""
            nonlocal menu_open
            menu_open = False
            show_welcome()
        
        def handle_menu_toggle(e):
            """Toggle menu open/close"""
            nonlocal menu_open
            menu_open = not menu_open
            print(f"Menu toggled: {menu_open}")  # Debug
            build_admin_dashboard_view()
        
        def handle_menu_close(e):
            """Close menu"""
            nonlocal menu_open
            menu_open = False
            print(f"Menu closed: {menu_open}")  # Debug
            build_admin_dashboard_view()
        
        # Menu navigation handlers - these are called when menu items are clicked
        def handle_menu_dashboard(e):
            """Navigate to dashboard"""
            print("Dashboard clicked")  # Debug
            nonlocal menu_open
            menu_open = False
            show_admin_dashboard()
        
        def handle_menu_queue(e):
            """Navigate to reports queue"""
            print("Queue clicked")  # Debug
            nonlocal menu_open
            menu_open = False
            show_reports_queue()
        
        def handle_menu_detail(e):
            """Navigate to report detail"""
            print("Detail clicked")  # Debug
            nonlocal menu_open
            menu_open = False
            show_report_detail("1042")
        
        def handle_menu_insights(e):
            """Navigate to AI insights"""
            print("Insights clicked")  # Debug
            nonlocal menu_open
            menu_open = False
            show_ai_insights()
        
        def handle_menu_analytics(e):
            """Navigate to analytics"""
            print("Analytics clicked")  # Debug
            nonlocal menu_open
            menu_open = False
            show_analytics()
        
        def handle_menu_settings(e):
            """Navigate to settings"""
            print("Settings clicked")  # Debug
            nonlocal menu_open
            menu_open = False
            show_settings()
        
        # Get content based on current view - PASS RESPONSIVE CONFIG
        if current_admin_view == "dashboard":
            content = create_dashboard_page()
        elif current_admin_view == "queue":
            content = create_reports_queue_page(responsive=responsive)
        elif current_admin_view == "detail":
            content = create_report_detail_page(selected_report_id)
        elif current_admin_view == "insights":
            content = create_ai_insights_page()
        elif current_admin_view == "analytics":
            content = create_analytics_page()
        elif current_admin_view == "settings":
            content = create_settings_page()
        else:
            content = create_dashboard_page()
        
        # Header with burger menu button
        header = ft.Container(
            content=ft.Row(
                controls=[
                    create_burger_button(handle_menu_toggle),
                    ft.Text(
                        current_admin_view.title(),
                        size=18,
                        weight="bold",
                        color=ft.Colors.WHITE,
                    ),
                    ft.Container(expand=True),
                    ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=24, color=ft.Colors.WHITE),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=15,
            bgcolor=COLORS["primary"],
            height=60,
        )
        
        # Menu overlay
        menu = create_burger_menu(
            responsive=responsive,
            current_admin_view=current_admin_view,
            on_dashboard=handle_menu_dashboard,
            on_queue=handle_menu_queue,
            on_detail=handle_menu_detail,
            on_insights=handle_menu_insights,
            on_analytics=handle_menu_analytics,
            on_settings=handle_menu_settings,
            on_logout=handle_logout,
            is_open=menu_open,
            on_close=handle_menu_close,
        )
        
        # Content area - menu will overlay on top of this
        main_layout = ft.Column(
            controls=[
                header,
                content,
            ],
            spacing=0,
            expand=True,
        )
        
        # Wrap main content and menu together - menu overlays content
        page_with_menu = ft.Stack(
            controls=[
                main_layout,  # Bottom layer - content
                menu,         # Top layer - menu overlay (when visible)
            ],
            expand=True,
        )
        
        page.add(page_with_menu)
        page.update()
    
    # ===== REPORTER FLOW =====
    
    def show_track_or_report_choice():
        """Show choice between tracking and reporting"""
        page.clean()
        
        def handle_track():
            show_reporter_track()
        
        def handle_report():
            show_reporter_form()
        
        def handle_back():
            show_who_are_you()
        
        choice_page = create_reporter_track_or_report_page(
            on_track=handle_track,
            on_report=handle_report,
            on_back=handle_back
        )
        page.add(choice_page)
        page.update()
    
    def show_reporter_track():
        """Show reporter tracking page"""
        page.clean()
        
        def handle_back():
            show_track_or_report_choice()
        
        track_page = create_reporter_track_screen(
            on_back=handle_back,
            responsive=responsive
        )
        page.add(track_page)
        page.update()
    
    def show_reporter_form():
        """Show reporter incident report form"""
        page.clean()
        nonlocal report_data
        report_data = {}
        
        def handle_next(form_data):
            nonlocal report_data
            report_data.update(form_data)
            show_reporter_evidence()
        
        def handle_back():
            show_track_or_report_choice()
        
        form = create_reporter_report_form_screen(
            on_next=handle_next,
            on_back=handle_back,
            responsive=responsive
        )
        page.add(form)
        page.update()
    
    def show_reporter_evidence():
        """Show reporter evidence upload screen"""
        page.clean()
        
        def handle_next(evidence_data):
            nonlocal report_data
            
            # Process uploaded files
            files = evidence_data.get("evidence_files", [])
            saved_attachments = []
            
            for file_info in files:
                # Upload file to storage
                result = evidence_service.upload_evidence(
                    report_id=None, # Report ID generated later
                    file_path=file_info["path"],
                    file_name=file_info["name"],
                    file_type=file_info["type"]
                )
                
                if "error" not in result:
                    saved_attachments.append(result)
            
            # Update report data with saved attachment metadata
            report_data["attachments"] = saved_attachments
            report_data["evidence_notes"] = evidence_data.get("notes", "") # Assuming notes field exists
            
            show_reporter_review()
        
        def handle_back():
            show_reporter_form()
            
        evidence_page = create_reporter_evidence_screen(
            on_next=handle_next,
            on_back=handle_back,
            responsive=responsive
        )
        page.add(evidence_page)
        page.update()
    
    def show_reporter_review():
        """Show report review screen"""
        page.clean()
        
        def handle_submit(final_data):
            nonlocal report_data
            report_data.update(final_data)
            # TODO: Save report to database
            show_reporter_confirmation()
        
        def handle_back():
            show_reporter_evidence()
        
        review = create_reporter_review_screen(
            report_data=report_data,
            on_submit=handle_submit,
            on_back=handle_back,
            responsive=responsive
        )
        page.add(review)
        page.update()
    
    def show_reporter_confirmation():
        """Show confirmation screen"""
        page.clean()
        
        def handle_continue():
            # Return to welcome to allow another report or exit
            show_welcome()
        
        confirmation = create_reporter_confirmation_screen(
            on_continue=handle_continue,
            responsive=responsive
        )
        page.add(confirmation)
        page.update()
    
    # ===== START APPLICATION =====
    
    # Start with welcome screen
    show_welcome()



if __name__ == "__main__":
    ft.run(main)