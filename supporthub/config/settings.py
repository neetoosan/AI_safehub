"""Configuration and settings for SupportHub"""

import os
from dotenv import load_dotenv

load_dotenv()

# App Settings
APP_NAME = "AI SupportHub"
APP_VERSION = "0.1.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./supporthub.db")

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Firebase
FIREBASE_CONFIG = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
}

# Colors - Design System
COLORS = {
    "primary": "#FF887D",          # Soft Coral - Primary / Main Accent
    "secondary": "#FF7D7F",        # Warm Rose - Secondary / Highlights
    "card_bg": "#FF957D",          # Peach Tint - Cards / Backgrounds / Hover States
    "background": "#FAFBF9",       # Off White - App background (neutral)
    "text": "#2E2E2E",             # Charcoal Gray - Body text
    "warning": "#F2B705",          # Muted Amber - Alerts
    "critical": "#C94A4A",         # Muted Red - High Severity
    "success": "#4CAF8E",          # Soft Green - Resolved
}

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "logs/app.log"
