"""Reporter Evidence Upload Screen - Using Tkinter (RELIABLE VERSION)"""

import flet as ft
from config.settings import COLORS
from utils.responsive import ResponsiveConfig, create_responsive_text
import tkinter as tk
from tkinter import filedialog
import os


def create_reporter_evidence_screen(on_next=None, on_back=None, responsive=None, file_picker=None):
    """Create evidence upload screen for reporter - Using tkinter for file selection"""
    
    if responsive is None:
        responsive = ResponsiveConfig(360, 740)
    
    # State for uploaded files
    uploaded_files = []
    current_upload_type = None
    
    evidence_list = ft.Column(controls=[], spacing=responsive.margin_small())
    
    def update_evidence_list():
        """Update the evidence list display"""
        evidence_list.controls.clear()
        
        if not uploaded_files:
            evidence_list.controls.append(
                ft.Text("No evidence added yet.", color="#999", italic=True)
            )
        else:
            for i, file_data in enumerate(uploaded_files):
                file_name = file_data["name"]
                file_size = f"{file_data['size'] / 1024:.1f} KB"
                evidence_type = file_data["type"]
                
                # Determine icon based on type
                icon = ft.Icons.INSERT_DRIVE_FILE
                if "Screenshot" in evidence_type or any(ext in file_name.lower() for ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']):
                    icon = ft.Icons.IMAGE
                elif "Audio" in evidence_type or any(ext in file_name.lower() for ext in ['.mp3', '.wav', '.m4a', '.ogg']):
                    icon = ft.Icons.AUDIO_FILE
                elif "Video" in evidence_type or any(ext in file_name.lower() for ext in ['.mp4', '.avi', '.mov', '.mkv']):
                    icon = ft.Icons.VIDEO_FILE
                
                evidence_list.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(icon, color=COLORS["secondary"], size=24),
                                        ft.Column(
                                            controls=[
                                                create_responsive_text(
                                                    evidence_type, 
                                                    responsive, 
                                                    size_type="body", 
                                                    weight="bold"
                                                ),
                                                create_responsive_text(
                                                    f"{file_name} ({file_size})", 
                                                    responsive, 
                                                    size_type="small", 
                                                    color="#666"
                                                ),
                                            ],
                                            spacing=2,
                                        ),
                                    ],
                                    spacing=10,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CLOSE,
                                    icon_color=COLORS["critical"],
                                    tooltip="Remove file",
                                    on_click=lambda e, idx=i: remove_file(idx)
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        padding=responsive.padding_medium(),
                        bgcolor="#f0f0f0",
                        border_radius=responsive.border_radius(),
                    )
                )
        
        evidence_list.update()

    def remove_file(index):
        """Remove a file from the uploaded files list"""
        if 0 <= index < len(uploaded_files):
            uploaded_files.pop(index)
            update_evidence_list()
    
    def handle_upload_click(e):
        """Handle file upload button click - Using tkinter"""
        nonlocal current_upload_type
        
        # Get evidence type from button data
        current_upload_type = e.control.data
        
        try:
            # Create a hidden tkinter root window
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            root.wm_attributes('-topmost', 1)  # Bring to front
            
            # Define file type filters based on evidence type
            filetypes = [("All files", "*.*")]
            if "Screenshot" in current_upload_type:
                filetypes = [
                    ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                    ("All files", "*.*")
                ]
            elif "Audio" in current_upload_type:
                filetypes = [
                    ("Audio files", "*.mp3 *.wav *.m4a *.ogg *.aac"),
                    ("All files", "*.*")
                ]
            elif "Video" in current_upload_type:
                filetypes = [
                    ("Video files", "*.mp4 *.avi *.mov *.mkv *.wmv"),
                    ("All files", "*.*")
                ]
            elif "Document" in current_upload_type:
                filetypes = [
                    ("Documents", "*.pdf *.doc *.docx *.txt"),
                    ("All files", "*.*")
                ]
            
            # Open file dialog
            file_paths = filedialog.askopenfilenames(
                parent=root,
                title=f"Select {current_upload_type}",
                filetypes=filetypes
            )
            
            # Destroy the tkinter window
            root.destroy()
            
            # Process selected files
            if file_paths:
                for file_path in file_paths:
                    if os.path.exists(file_path):
                        file_size = os.path.getsize(file_path)
                        file_name = os.path.basename(file_path)
                        
                        uploaded_files.append({
                            "name": file_name,
                            "path": file_path,
                            "size": file_size,
                            "type": current_upload_type
                        })
                
                update_evidence_list()
        
        except Exception as ex:
            print(f"Error opening file dialog: {ex}")
            # Show error to user
            error_dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(f"Could not open file dialog: {str(ex)}"),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: close_dialog(error_dialog))
                ]
            )
            e.page.dialog = error_dialog
            error_dialog.open = True
            e.page.update()
    
    def close_dialog(dialog):
        """Close a dialog"""
        dialog.open = False
        dialog.page.update()
    
    evidence_types = [
        "📷 Screenshots",
        "🎵 Audio Recording",
        "📹 Video",
        "📄 Document",
        "💬 Chat/Message",
        "✉️ Email",
    ]
    
    def handle_next(e):
        if on_next:
            on_next({"evidence_files": uploaded_files})
    
    def handle_back(e):
        if on_back:
            on_back()
    
    # Evidence type buttons - using regular Button (not async)
    evidence_buttons = ft.Column(
        controls=[
            ft.Button(
                content=ft.Row(
                    controls=[
                        create_responsive_text(
                            f"Add {ev_type}", 
                            responsive, 
                            size_type="body", 
                            color=ft.Colors.WHITE
                        ),
                        ft.Icon(ft.Icons.UPLOAD_FILE, color=ft.Colors.WHITE, size=16),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                width=responsive.input_width(),
                height=responsive.button_height(),
                bgcolor=COLORS["secondary"],
                color=ft.Colors.WHITE,
                data=ev_type,  # Store type in data
                on_click=handle_upload_click,  # Regular (not async) handler
            )
            for ev_type in evidence_types
        ],
        spacing=responsive.margin_small(),
    )
    
    notes = ft.TextField(
        label="Additional notes (optional)",
        hint_text="Any other context that might be helpful...",
        multiline=True,
        min_lines=responsive.text_field_multiline_min_lines(),
        max_lines=responsive.text_field_multiline_max_lines(),
        width=responsive.input_width(),
    )
    
    page_content = ft.Column(
        controls=[
            # Header
            create_responsive_text(
                "Add Evidence",
                responsive,
                size_type="h1",
                weight="bold",
                color=COLORS["primary"],
                text_align=ft.TextAlign.CENTER,
            ),
            
            ft.Container(height=responsive.margin_medium()),
            
            create_responsive_text(
                "Help us understand what happened by sharing evidence",
                responsive,
                size_type="small",
                color=COLORS["secondary"],
                text_align=ft.TextAlign.CENTER,
            ),
            
            ft.Container(height=responsive.spacing_vertical()),
            
            # Progress indicator
            create_responsive_text(
                "Step 2 of 4: Evidence",
                responsive,
                size_type="small",
                color="#999",
                weight="bold",
            ),
            
            ft.Container(height=responsive.spacing_vertical()),
            
            create_responsive_text(
                "Upload evidence files:",
                responsive,
                size_type="body",
                weight="bold",
            ),
            
            ft.Container(height=responsive.margin_medium()),
            
            evidence_buttons,
            
            ft.Container(height=responsive.spacing_vertical()),
            
            create_responsive_text(
                "Files attached:",
                responsive,
                size_type="body",
                weight="bold",
            ),
            
            ft.Container(height=responsive.margin_medium()),
            
            evidence_list,
            
            ft.Container(height=responsive.spacing_vertical()),
            
            ft.Divider(),
            
            ft.Container(height=responsive.margin_medium()),
            
            notes,
            
            ft.Container(height=responsive.spacing_vertical()),
            
            # Buttons
            ft.Row(
                controls=[
                    ft.Button(
                        content=create_responsive_text(
                            "Back", 
                            responsive, 
                            size_type="body", 
                            color=COLORS["primary"]
                        ),
                        expand=True,
                        height=responsive.button_height(),
                        bgcolor=COLORS["background"],
                        on_click=handle_back,
                    ),
                    ft.Button(
                        content=create_responsive_text(
                            "Next", 
                            responsive, 
                            size_type="body", 
                            color=ft.Colors.WHITE
                        ),
                        expand=True,
                        height=responsive.button_height(),
                        bgcolor=COLORS["primary"],
                        on_click=handle_next,
                    ),
                ],
                spacing=responsive.margin_medium(),
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
    )
    
    # Wrap in container
    page_container = ft.Container(
        content=page_content,
        bgcolor=COLORS["background"],
        padding=responsive.padding_large(),
        expand=True,
    )
    
    # Initialize empty list
    update_evidence_list()
    
    return page_container