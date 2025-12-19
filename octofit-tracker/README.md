# OctoFit Tracker

A fitness tracker app to log activities, manage teams, provide leaderboards, and surface personalized workouts.

## Goals
- User authentication and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

## Project structure
```
octofit-tracker/
├── backend/
│   ├── venv/
│   ├── octofit_tracker/
└── frontend/
```

## Quick setup (backend)
1. Create virtual environment:
```bash
python3 -m venv octofit-tracker/backend/venv
```
2. Activate it:
```bash
source octofit-tracker/backend/venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r octofit-tracker/backend/requirements.txt
```
4. (Later) scaffold the Django project and run dev server:
```bash
django-admin startproject octofit_tracker octofit-tracker/backend
python octofit-tracker/backend/manage.py runserver 8000
```

## Frontend
- We'll create a React app in `octofit-tracker/frontend/` and run it on port `3000` during development.

## Ports (as required)
- Backend (Django): 8000 (public)
- Frontend (React): 3000 (public)
- MongoDB: 27017 (private)

## Next steps
- Scaffold the Django project in `octofit-tracker/backend/` and commit initial files.
- Initialize the React frontend.
