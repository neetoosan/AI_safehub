
import sys
import os

# Add supporthub directory to path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(base_dir, "supporthub"))

import flet as ft
from ui.pages.reports_queue_page import create_reports_queue_page
from utils.responsive import ResponsiveConfig

def main():
    print("Testing Deep Responsiveness...")
    
    # Mock page for ResponsiveConfig
    class MockPage:
        def __init__(self, w, h):
            self.window_width = w
            self.window_height = h
    
    # Define configurations
    configs = [
        ("Mobile", 375, 800),
        ("Tablet", 768, 1024),
        ("Desktop", 1400, 900)
    ]
    
    for name, w, h in configs:
        print(f"Testing {name} Layout ({w}x{h})...")
        try:
            # Create config
            page = MockPage(w, h)
            responsive = ResponsiveConfig(w, h)
            
            # Verify device type detection
            print(f"  Detected Device: {responsive.device_type}")
            
            # Build page
            content = create_reports_queue_page(responsive=responsive)
            print(f"  Build OK")
            
        except Exception as e:
            print(f"  FAILED: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
