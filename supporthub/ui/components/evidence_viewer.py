"""Evidence Viewer Component"""

import flet as ft
from config.settings import COLORS


class EvidenceViewer(ft.Control):
    """Component for viewing evidence attachments (images, audio)"""

    def __init__(self, evidence_list: list = None):
        super().__init__()
        self.evidence_list = evidence_list or [
            {"type": "image", "name": "screenshot.png", "url": ""},
            {"type": "audio", "name": "recording.mp3", "url": ""},
        ]

    def build(self):
        evidence_items = []

        for item in self.evidence_list:
            if item["type"] == "image":
                icon = ft.icons.IMAGE
                color = COLORS["secondary"]
            elif item["type"] == "audio":
                icon = ft.icons.AUDIO_FILE
                color = COLORS["secondary"]
            else:
                icon = ft.icons.DESCRIPTION
                color = COLORS["secondary"]

            evidence_items.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(icon, size=40, color=color),
                            ft.Text(item["name"], size=10, text_align=ft.TextAlign.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                    ),
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=8,
                    padding=10,
                )
            )

        return ft.Container(
            content=ft.GridView(
                controls=evidence_items,
                runs_count=4,
                spacing=10,
                run_spacing=10,
            ),
            padding=10,
        )
