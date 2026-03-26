"""Base Layout for Admin Dashboard"""

import flet as ft
from config.settings import COLORS
from ui.components import Sidebar
from ui.pages import (
    DashboardPage,
    ReportsQueuePage,
    ReportDetailPage,
    AIInsightsPage,
    AnalyticsPage,
    SettingsPage,
)


class BaseLayout(ft.Control):
    """Main layout with sidebar and content area"""

    def __init__(self):
        super().__init__()
        self.current_page = None
        self.expand = True

    def on_navigation_change(self, page_name):
        """Handle navigation between pages"""
        pages = {
            "Dashboard": DashboardPage,
            "Reports Queue": ReportsQueuePage,
            "AI Insights": AIInsightsPage,
            "Analytics": AnalyticsPage,
            "Settings": SettingsPage,
        }

        page_class = pages.get(page_name)
        if page_class:
            self.current_page = page_class()
            self.content.controls[1] = self.current_page
            self.update()

    def build(self):
        sidebar = Sidebar(on_nav_change=self.on_navigation_change)

        # Initialize with Dashboard
        self.current_page = DashboardPage()

        return ft.Row(
            controls=[
                sidebar,
                self.current_page,
            ],
            spacing=0,
            expand=True,
        )
