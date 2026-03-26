# AI SupportHub - Complete Application Structure

Complete harassment and abuse reporting platform with AI-powered analysis.

## Project Structure

```
supporthub/
├── app/                    # Application entry point
├── config/                 # Configuration & settings
├── auth/                   # Authentication & authorization
├── models/                 # Database models (SQLAlchemy)
├── database/               # Database setup & migrations
├── services/               # Business logic services
├── ai/                     # AI/NLP components
├── api/                    # REST API routes
├── ui/                     # Flet UI components
│   ├── layouts/            # Page layouts
│   ├── pages/              # Application pages
│   └── components/         # Reusable UI components
├── utils/                  # Utility functions
├── tests/                  # Test suite
└── logs/                   # Application logs
```

## Getting Started

### Installation

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize database:
```bash
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
```

5. Run application:
```bash
python -m app.main
```

## Features

### Reporter App (Mobile)
- Anonymous incident reporting
- Evidence upload support
- Real-time status tracking
- Safety resources & panic exit

### Admin Dashboard (Desktop)
- AI-ranked reports queue
- Detailed report viewer
- AI insights & explainability
- Pattern detection
- Analytics & trends
- Case management
- Audit logging

### AI Services
- **NLP Classification**: Abuse type detection
- **Severity Scoring**: 0-10 risk assessment
- **Pattern Detection**: Recurring offender identification
- **Explainability**: Human-readable AI decisions

## Configuration

See `.env` file for configuration options:
- Database connection
- Firebase setup
- Security settings
- Email/notification service
- AWS S3 (optional)

## Development

### Run Tests
```bash
pytest
pytest --cov=supporthub  # With coverage
```

### Code Quality
```bash
black supporthub/  # Format code
flake8 supporthub/  # Lint
```

## API Documentation

API endpoints (when backend is fully implemented):
- `POST /api/reports` - Submit new report
- `GET /api/reports` - List reports
- `GET /api/reports/{id}` - Get report details
- `GET /api/analytics/dashboard` - Dashboard metrics
- `GET /api/analytics/trends` - Trend analysis

## Security

- Anonymous report submissions
- End-to-end encryption for evidence
- Role-based access control (RBAC)
- Audit logging for all actions
- HTTPS/TLS for data in transit
- Hash-based reporter anonymity

## Design System

**Colors**:
- Primary: #1F3A5F (Deep Blue)
- Secondary: #2FA4A9 (Soft Teal)
- Warning: #F2B705 (Muted Amber)
- Critical: #C94A4A (Muted Red)
- Success: #4CAF8E (Soft Green)

## Contributing

1. Follow PEP 8 style guide
2. Add tests for new features
3. Update documentation
4. Create pull requests with clear descriptions

## License

[To be determined]

## Support

For issues and questions, please contact the development team.
