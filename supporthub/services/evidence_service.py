"""Evidence Service - Attachment Handling"""

import os
import uuid
import shutil
from typing import Dict, Optional
from datetime import datetime


class EvidenceService:
    """Handle evidence/attachment management"""

    def __init__(self, db=None, upload_dir="uploads"):
        self.db = db
        self.upload_dir = upload_dir
        
        # Ensure upload directory exists
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    def upload_evidence(self, report_id: Optional[str], file_path: str, file_name: str, file_type: str) -> Dict:
        """Upload evidence file from temporary path to permanent storage"""
        
        # Generate unique filename to prevent overwrites
        unique_id = str(uuid.uuid4())
        extension = os.path.splitext(file_name)[1]
        stored_filename = f"{unique_id}{extension}"
        destination_path = os.path.join(self.upload_dir, stored_filename)
        
        try:
            # Copy file from temp location (FilePicker path) to our storage
            shutil.copy2(file_path, destination_path)
            
            # Return metadata
            return {
                "id": unique_id,
                "original_name": file_name,
                "stored_name": stored_filename,
                "path": destination_path,
                "type": file_type,
                "size": os.path.getsize(destination_path),
                "upload_date": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error uploading evidence: {e}")
            return {"error": str(e)}

    def get_evidence_path(self, stored_filename: str) -> Optional[str]:
        """Get full path to evidence file"""
        path = os.path.join(self.upload_dir, stored_filename)
        if os.path.exists(path):
            return path
        return None

    def delete_evidence(self, stored_filename: str) -> bool:
        """Delete evidence file"""
        path = os.path.join(self.upload_dir, stored_filename)
        if os.path.exists(path):
            try:
                os.remove(path)
                return True
            except Exception as e:
                print(f"Error deleting evidence: {e}")
                return False
        return False
