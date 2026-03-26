
import sys
import os

# Add supporthub directory to path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(base_dir, "supporthub"))

import flet as ft
from ui.pages.reports_queue_page import create_reports_queue_page
from utils.responsive import ResponsiveConfig

def main():
    print("Testing Responsive Reports Queue Page...")
    
    # Mock page for ResponsiveConfig
    class MockPage:
        window_width = 375
        window_height = 800
    
    responsive_mobile = ResponsiveConfig(375, 800)
    responsive_desktop = ResponsiveConfig(1400, 900)
    
    try:
        # Test Mobile Build
        mobile_page = create_reports_queue_page(responsive=responsive_mobile)
        print("Mobile Layout Build... OK")
        
        # Test Desktop Build
        desktop_page = create_reports_queue_page(responsive=responsive_desktop)
        print("Desktop Layout Build... OK")
        
    except Exception as e:
        print(f"FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
