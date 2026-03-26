"""Reports Queue - AI-ranked Reports List - FINAL FIX"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig

def create_reports_queue_page(responsive: ResponsiveConfig = None):
    """Display list of reports ranked by AI priority"""
    
    # Debug output
    if responsive:
        print(f"[Queue Page] Width: {responsive.page_width}px, Device: {responsive.device_type}, Mobile: {responsive.is_mobile()}")
    
    # Ensure responsive is properly initialized
    is_mobile = responsive and responsive.is_mobile() if responsive else False
    
    # Mock data for reports
    reports = [
        {
            "id": "1045",
            "title": "Severe Harassment Case",
            "severity": "Critical",
            "priority": 95,
            "time": "2 hours ago",
        },
        {
            "id": "1044",
            "title": "Recurring Pattern Detected",
            "severity": "High",
            "priority": 87,
            "time": "4 hours ago",
        },
        {
            "id": "1043",
            "title": "Workplace Discrimination",
            "severity": "High",
            "priority": 76,
            "time": "6 hours ago",
        },
        {
            "id": "1042",
            "title": "General Complaint",
            "severity": "Medium",
            "priority": 45,
            "time": "1 day ago",
        },
    ]

    def get_severity_color(severity):
        severity_map = {
            "Critical": COLORS["critical"],
            "High": COLORS["warning"],
            "Medium": COLORS["secondary"],
            "Low": COLORS["success"],
        }
        return severity_map.get(severity, COLORS["text"])

    def build_report_row(report):
        # Get dynamic font sizes
        if responsive:
            font_body = responsive.font_size_body()
            font_small = responsive.font_size_small()
            padding = responsive.padding_medium()
        else:
            font_body = 14
            font_small = 12
            padding = 15

        # MOBILE: Card Layout with EXPLICIT WIDTH
        if is_mobile:
            # Calculate exact width for text container
            # Total available = page_width - (outer padding 20*2) - (card padding*2)
            text_width = responsive.page_width - (20 * 2) - (padding * 2)
            
            print(f"[Mobile Card] Text width: {text_width}px (Page: {responsive.page_width}, Padding: {padding})")
            
            return ft.Container(
                content=ft.Column(
                    controls=[
                        # Header Row: ID and Time
                        ft.Row(
                            controls=[
                                ft.Text(
                                    f"#{report['id']}", 
                                    weight="bold", 
                                    color=COLORS["primary"], 
                                    size=font_body,
                                ),
                                ft.Text(
                                    report["time"], 
                                    size=font_small, 
                                    color="#999",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        # Title - THE FIX: Container with explicit width
                        ft.Container(
                            content=ft.Text(
                                report["title"], 
                                weight="bold", 
                                size=font_body,
                            ),
                            width=text_width,  # ✅ EXPLICIT WIDTH
                        ),
                        # Footer Row: Severity, Progress, Arrow
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                        report["severity"], 
                                        color=ft.Colors.WHITE, 
                                        size=font_small,
                                    ),
                                    bgcolor=get_severity_color(report["severity"]),
                                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                    border_radius=10,
                                ),
                                ft.Container(
                                    content=ft.ProgressBar(
                                        value=report["priority"] / 100,
                                        color=get_severity_color(report["severity"]),
                                        height=6,
                                    ),
                                    expand=True,
                                    margin=ft.margin.symmetric(horizontal=8),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.ARROW_FORWARD,
                                    icon_color=COLORS["primary"],
                                    icon_size=20,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=8,
                ),
                padding=padding,
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                margin=ft.margin.only(bottom=10),
            )
        
        # DESKTOP/TABLET: Table Row Layout
        else:
            if responsive and responsive.is_tablet():
                id_width = 70
                severity_width = 90
                progress_width = 100
            else:
                id_width = 80
                severity_width = 110
                progress_width = 120
            
            return ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                f"#{report['id']}", 
                                weight="bold", 
                                size=font_body
                            ),
                            width=id_width,
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        report["title"], 
                                        weight="bold", 
                                        size=font_body,
                                    ),
                                    ft.Text(
                                        report["time"], 
                                        size=font_small, 
                                        color="#999"
                                    ),
                                ],
                                spacing=2,
                            ),
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Container(
                                content=ft.Text(
                                    report["severity"], 
                                    color=ft.Colors.WHITE, 
                                    size=font_small,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                bgcolor=get_severity_color(report["severity"]),
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                border_radius=12,
                            ),
                            width=severity_width,
                        ),
                        ft.Container(
                            content=ft.ProgressBar(
                                value=report["priority"] / 100,
                                color=get_severity_color(report["severity"]),
                                height=8,
                            ),
                            width=progress_width,
                        ),
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.Icons.ARROW_FORWARD,
                                icon_color=COLORS["primary"],
                                icon_size=20,
                            ),
                            width=50,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                ),
                padding=padding,
                bgcolor=ft.Colors.WHITE,
                border_radius=8,
                margin=ft.margin.only(bottom=10),
            )

    # Search & Filter Layout
    if is_mobile:
        search_filter_layout = ft.Column(
            controls=[
                ft.TextField(
                    label="Search reports",
                    prefix_icon=ft.Icons.SEARCH,
                    text_size=responsive.font_size_body() if responsive else 14,
                ),
                ft.Dropdown(
                    label="Sort by",
                    options=[
                        ft.dropdown.Option("Priority"),
                        ft.dropdown.Option("Date"),
                        ft.dropdown.Option("Severity"),
                    ],
                    text_size=responsive.font_size_body() if responsive else 14,
                ),
            ],
            spacing=10,
        )
    else:
        search_filter_layout = ft.Row(
            controls=[
                ft.TextField(
                    label="Search reports",
                    width=300,
                    prefix_icon=ft.Icons.SEARCH,
                ),
                ft.Dropdown(
                    label="Sort by",
                    width=150,
                    options=[
                        ft.dropdown.Option("Priority"),
                        ft.dropdown.Option("Date"),
                        ft.dropdown.Option("Severity"),
                    ],
                ),
            ],
            spacing=15,
        )

    # Reports List
    reports_list = ft.Column(
        controls=[build_report_row(report) for report in reports],
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    # Main Container
    return ft.Container(
        content=ft.Column(
            controls=[
                # Title
                ft.Container(
                    content=ft.Text(
                        "Reports Queue (AI-Ranked)",
                        size=responsive.font_size_h1() if responsive else 32,
                        weight="bold",
                        color=COLORS["primary"],
                    ),
                    padding=ft.padding.only(left=20, right=20, top=20, bottom=10),
                ),
                # Search & Filter
                ft.Container(
                    content=search_filter_layout,
                    padding=ft.padding.only(left=20, right=20, bottom=10),
                ),
                # Reports List
                ft.Container(
                    content=reports_list,
                    padding=ft.padding.symmetric(horizontal=20),
                    expand=True,
                ),
            ],
            spacing=0,
            expand=True,
        ),
        bgcolor=COLORS["background"],
        expand=True,
    )