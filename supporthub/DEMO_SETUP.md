"""Demo Setup Guide for AI SupportHub

This guide helps you get the demo running quickly for sponsor presentations.
"""

# ==========================================
# QUICK START - Demo Setup (5 minutes)
# ==========================================

## Step 1: Clone and Setup Environment
```bash
cd /home/neetoosan/Documents/supportHub/supporthub
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 2: Install Dependencies (AI API Version - No Model Training)
```bash
pip install -r requirements.txt
```

## Step 3: Run Demo WITHOUT Hugging Face API (Instant)
The demo includes mock data, so it works immediately without API setup:

```bash
python -m app.main
```

This will:
- Launch the admin dashboard UI using Flet
- Show demo data with AI classifications
- Display pattern detection, severity scoring, and analytics
- Use mock data for all AI services

## Step 4 (Optional): Add Real AI with Hugging Face API

For enhanced demo with real AI:

### 4a. Get Free Hugging Face API Key
1. Go to https://huggingface.co/settings/tokens
2. Create a free account
3. Generate a free API token

### 4b. Configure API Key
Create/update `.env` file in the project:
```
HUGGINGFACE_API_KEY=your_token_here
```

### 4c. Restart App
```bash
python -m app.main
```

Now the app will use:
- **Zero-shot text classification** for abuse type detection
- **Semantic similarity** for pattern matching
- **Real NLP analysis** powered by Hugging Face

## ==========================================
# DEMO SCENARIOS FOR SPONSORS
# ==========================================

### Scenario 1: Show Reports Queue
1. Login (any email/password)
2. View AI-ranked reports
3. Highlight severity scores and AI confidence
4. Show AI Insights tab with explanations

### Scenario 2: Demonstrate AI Analysis
1. Open a report detail
2. Click "AI Insights" tab
3. Show:
   - Classification results (harassment, bullying, etc.)
   - Confidence scores
   - Contributing factors
   - "Why This Analysis?" explainability section

### Scenario 3: Show Pattern Detection
1. Navigate to Analytics page
2. Show "Top Recurring Patterns"
3. Explain how AI identifies recurring offenders
4. Show linked incidents

### Scenario 4: Dashboard Analytics
1. Show key metrics (total reports, high severity, resolved)
2. Display trends and incident distribution
3. Highlight safety and resolution rates

## ==========================================
# KEY FEATURES TO HIGHLIGHT
# ==========================================

✓ Anonymous Reporting - Privacy-first design
✓ AI Classification - Automatic abuse type detection
✓ Severity Scoring - Risk assessment (0-10)
✓ Pattern Detection - Identifies recurring offenders
✓ Explainability - Shows WHY AI made decisions
✓ Admin Dashboard - Comprehensive case management
✓ Real-time Alerts - Critical reports prioritized
✓ Audit Logging - Full transparency

## ==========================================
# ARCHITECTURE HIGHLIGHTS FOR SPONSORS
# ==========================================

### Frontend
- Built with Flet (cross-platform Python UI)
- Color-coded severity levels
- Real-time UI updates
- Responsive dashboard design

### Backend (Ready for Integration)
- FastAPI/Flask ready
- RESTful API structure
- SQLAlchemy ORM for database
- Role-based access control

### AI/ML Integration
- Hugging Face API (No expensive GPU)
- Zero-shot classification (Works with any text)
- Semantic similarity matching
- Explainable AI (LIME/SHAP ready)

### Database
- SQLAlchemy models prepared
- Support for PostgreSQL/SQLite
- Audit logging for compliance
- Schema migrations with Alembic

## ==========================================
# DEPLOYMENT FOR PRODUCTION
# ==========================================

When ready to deploy:

1. **Backend Server**:
   ```bash
   pip install fastapi uvicorn
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

2. **Database**:
   ```bash
   export DATABASE_URL=postgresql://user:pass@host/db
   python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

3. **Docker Container**:
   ```bash
   docker build -t supporthub .
   docker run -p 8000:8000 -e HUGGINGFACE_API_KEY=xxx supporthub
   ```

## ==========================================
# TROUBLESHOOTING
# ==========================================

**Issue**: App won't start  
**Solution**: `pip install --upgrade flet`

**Issue**: No AI classifications showing  
**Solution**: Mock data is enabled - check `.env` for HUGGINGFACE_API_KEY

**Issue**: Database error  
**Solution**: Delete `supporthub.db` and restart - it will recreate

**Issue**: Slow API responses  
**Solution**: Hugging Face free tier has rate limits. For production, upgrade to Pro.

## ==========================================
# NEXT STEPS AFTER DEMO
# ==========================================

1. Implement reporter mobile app (Flutter/React Native)
2. Connect real database (PostgreSQL)
3. Deploy backend API (AWS/GCP)
4. Integrate with organization systems
5. Fine-tune AI models if needed
6. Set up notification system (Email/SMS)
7. Implement evidence encryption
8. Configure audit logging
9. Add two-factor authentication
10. Perform security audit

## Support & Contact
For setup issues or feature questions, check the README.md file
