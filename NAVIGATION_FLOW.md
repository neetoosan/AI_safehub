# AI SupportHub - Complete Navigation Flow

## Overview
This document outlines the complete navigation architecture connecting all screens in the AI SupportHub application.

## Application Structure

### 1. Welcome & Onboarding
```
┌─────────────────────────────────────────┐
│         WELCOME SCREEN                  │
│    (Welcome to AI SupportHub)            │
│          [Continue] →                    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│       WHO ARE YOU SCREEN                │
│     Choose role: Reporter/Admin         │
└─────────────────────────────────────────┘
          ↓                      ↓
     [Reporter]            [Admin]
          ↓                      ↓
```

### 2. Admin Flow
```
┌─────────────────────────────────────────┐
│    ADMIN LOGIN CHOICE                   │
│   [Login] or [Register]                 │
└─────────────────────────────────────────┘
    ↓                          ↓
    
┌────────────────────┐   ┌──────────────────────────┐
│   ADMIN LOGIN      │   │  ADMIN REGISTRATION      │
│  (Existing User)   │   │  (New Organization)      │
└────────────────────┘   └──────────────────────────┘
    ↓                          ↓
    └──────────────┬───────────┘
                   ↓
         ┌─────────────────────────────────┐
         │    ADMIN DASHBOARD              │
         │ (with Sidebar Navigation)       │
         └─────────────────────────────────┘
                   ↓
    ┌──────────────┼──────────────┬──────────────┬──────────────┐
    ↓              ↓              ↓              ↓              ↓
┌─────┐      ┌──────────┐  ┌─────────┐  ┌──────────┐   ┌──────────┐
│Main │      │ Reports  │  │ Report  │  │   AI     │   │Analytics │
│Dash │      │  Queue   │  │ Detail  │  │Insights  │   │          │
└─────┘      └──────────┘  └─────────┘  └──────────┘   └──────────┘

    All pages also have:
    [Settings] - Organization settings
    [Logout] - Returns to Welcome screen
```

### 3. Reporter Flow
```
┌──────────────────────────────────────────────────┐
│  REPORTER FORM - STEP 1/4: Incident Details     │
│  Fields: Type, Description, When, Location      │
│  [Back] [Next] →                                │
└──────────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────────┐
│  REPORTER EVIDENCE - STEP 2/4: Evidence          │
│  Select: Screenshots, Audio, Video, Document    │
│  [Back] [Next] →                                │
└──────────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────────┐
│  REPORTER REVIEW - STEP 3/4: Review              │
│  Summary of all provided information             │
│  [Back] [Submit] →                              │
└──────────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────────┐
│  REPORTER CONFIRMATION - STEP 4/4: Success       │
│  Report ID, Submission Time, Next Steps          │
│  [Continue] → Returns to Welcome                │
└──────────────────────────────────────────────────┘
```

## Screen Details

### Onboarding Screens (Responsive)
- **Welcome Screen**: Intro, logo, continue button
- **Who Are You Screen**: Role selection with gesture detectors
- **Admin Login Choice**: Choose between login or register

### Admin Pages
- **Admin Login**: Email/password form with "Forgot Password" option
- **Admin Registration**: Organization and admin account setup
  - Org Name, Type, Contact Email
  - Admin Name, Email, Password
  
- **Dashboard Main**: Key metrics and recent activity
  - Statistics: Total Reports, High Severity, Pending, Resolved
  - Recent Activity Feed
  
- **Reports Queue**: AI-ranked list of reports
  - Priority scores, Severity levels
  - Quick view of pending reports
  
- **Report Detail**: Full report information
  - Reporter info (anonymized), Evidence, Timeline
  - Admin actions, Notes
  
- **AI Insights**: Pattern analysis and trends
  - Recurring offenders, Common triggers
  - AI recommendations
  
- **Analytics**: Statistical overview
  - Charts, Trends, Report categories
  - Response times, Resolution rates
  
- **Settings**: Organization configuration
  - Notification preferences, User management
  - API settings, Security options

### Reporter Pages (Responsive, Scrollable)
- **Form (Step 1)**: Incident details collection
- **Evidence (Step 2)**: Evidence type selection
- **Review (Step 3)**: Data verification before submission
- **Confirmation (Step 4)**: Success with Report ID

## Navigation Properties

### All Admin Pages
- **Sidebar**: Always visible on left
- **Active State**: Current page highlighted
- **Logout Button**: Bottom of sidebar, returns to Welcome
- **Responsive**: Sidebar collapses on mobile (<768px)

### All Reporter Pages
- **Scrollable**: `scroll=ft.ScrollMode.AUTO`
- **Buttons**: `expand=True` with flexible spacing
- **Alignment**: Buttons use `SPACE_BETWEEN` for small screens
- **Responsive**: Full width on mobile, centered on desktop

## State Management

### Application State
```python
current_user = None                    # Logged-in user info
current_role = "admin" | "reporter"    # Selected role
current_admin_view = "dashboard"       # Current admin page
selected_report_id = None              # For report detail
report_data = {}                       # Accumulates through reporter flow
```

### Data Flow
1. **Admin Registration**: Collects org info → Dashboard
2. **Reporter Form**: Collects across 4 steps → Confirmation
3. **Admin Views**: Dashboard sidebar navigation

## Key Features

### Navigation Consistency
✓ Back buttons available on all screens (except Welcome)
✓ Logout accessible from all admin pages
✓ Clear visual hierarchy with responsive design
✓ State management maintains user session

### Responsive Design
✓ All buttons use `expand=True` for small screens
✓ Sidebar responsive (hides on mobile)
✓ Text scales with device type
✓ Touch-friendly spacing

### User Flows
✓ Complete reporter journey: Form → Evidence → Review → Confirmation
✓ Complete admin journey: Login/Register → Dashboard → Reports
✓ Seamless role selection
✓ Easy logout and role switching

## Future Enhancements

1. **Persistent Sessions**: Save login state across app restarts
2. **Deep Linking**: Direct URL access to specific pages
3. **Back Stack**: Multiple back navigation levels
4. **Search/Filter**: Quick navigation to specific reports
5. **Notifications**: Real-time alerts integrated into sidebar
6. **Export**: Export reports from detail view
7. **Bulk Actions**: Process multiple reports at once
