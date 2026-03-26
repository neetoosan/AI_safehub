
import sys
import os
import flet as ft

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "supporthub"))

from utils.responsive import ResponsiveConfig, get_responsive_config
from ui import create_login_page, create_dashboard_page
from ui.pages.welcome_page import create_welcome_screen
from ui.pages.who_are_you_page import create_who_are_you_screen
from ui.pages.admin_registration_page import create_admin_registration_screen
from ui.pages.reporter_report_form_page import create_reporter_report_form_screen
from ui.pages.reporter_evidence_page import create_reporter_evidence_screen
from ui.pages.reporter_review_page import create_reporter_review_screen
from ui.pages.reporter_confirmation_page import create_reporter_confirmation_screen
from ui.pages.reports_queue_page import create_reports_queue_page
from ui.pages.report_detail_page import create_report_detail_page
from ui.pages.ai_insights_page import create_ai_insights_page
from ui.pages.analytics_page import create_analytics_page
from ui.pages.settings_page import create_settings_page

def mock_callback(*args, **kwargs):
    pass

def run_verification():
    print("Starting page verification...")
    
    class MockPage:
        def __init__(self):
            self.window_width = 1200
            self.window_height = 800
            self.platform = "linux"
            self.pwa = False
            self.web = False
            self.route = "/"
    
    page = MockPage()
    responsive = get_responsive_config(page)

    errors = []

    tests = [
        ("Login Page", lambda: create_login_page(on_login=mock_callback, responsive=responsive)),
        ("Dashboard Page", lambda: create_dashboard_page()),
        ("Welcome Screen", lambda: create_welcome_screen(on_continue=mock_callback, responsive=responsive)),
        ("Who Are You Screen", lambda: create_who_are_you_screen(on_reporter=mock_callback, on_admin=mock_callback, responsive=responsive)),
        ("Admin Registration", lambda: create_admin_registration_screen(on_register=mock_callback, on_back=mock_callback, responsive=responsive)),
        ("Reporter Report Form", lambda: create_reporter_report_form_screen(on_next=mock_callback, on_back=mock_callback, responsive=responsive)),
        ("Reporter Evidence Screen", lambda: create_reporter_evidence_screen(on_next=mock_callback, on_back=mock_callback, responsive=responsive)),
        ("Reporter Review Screen", lambda: create_reporter_review_screen(report_data={}, on_submit=mock_callback, on_back=mock_callback, responsive=responsive)),
        ("Reporter Confirmation", lambda: create_reporter_confirmation_screen(on_continue=mock_callback, responsive=responsive)),
        ("Reports Queue", lambda: create_reports_queue_page()),
        ("Report Detail", lambda: create_report_detail_page("1042")),
        ("AI Insights", lambda: create_ai_insights_page()),
        ("Analytics", lambda: create_analytics_page()),
        ("Settings", lambda: create_settings_page()),
    ]

    for name, test_func in tests:
        try:
            print(f"Testing {name}...", end=" ")
            control = test_func()
            if isinstance(control, ft.Control):
                print("OK")
            else:
                print(f"FAILED (Did not return a Control, got {type(control)})")
                errors.append(f"{name} did not return a Control")
        except Exception as e:
            print(f"FAILED ({str(e)})")
            import traceback
            traceback.print_exc()
            errors.append(f"{name} raised exception: {str(e)}")

    print("\nVerification Summary:")
    if not errors:
        print("ALL TESTS PASSED. Navigation should be stable.")
    else:
        print(f"{len(errors)} TESTS FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    run_verification()
