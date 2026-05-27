# Streamlit ML Demo

A clean, portfolio-ready Streamlit web application demonstrating a predictive system UI and data visualization workflow.

## Overview

This project is a simple Streamlit app built for demonstration and recruiter presentation. It includes a polished UI, structured inputs, example analytics, and a professional repository layout.

## Features

- Interactive user form with inputs for name, age, salary, gender, and education
- File upload support for images
- Table and chart visualization using Pandas and Matplotlib
- Sidebar navigation and responsive layout
- Structured, production-ready folder architecture

## Architecture

The application follows a simple yet scalable structure:

- `src/`: main application code
- `assets/`: images and static media assets
- `docs/`: project documentation and architecture details
- `tests/`: test suite for basic validation
- `scripts/`: helper launch scripts and workflow automation

## Folder Structure

```text
Streamlit-main/
├── assets/
│   └── images/
│       └── peacock.jpg
├── docs/
│   └── architecture.md
├── scripts/
│   └── run_app.ps1
├── src/
│   ├── app.py
│   └── __init__.py
├── tests/
│   └── test_app.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

- macOS / Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To launch the Streamlit app:

```bash
streamlit run src/app.py
```

Or run the provided script on Windows:

```powershell
./scripts/run_app.ps1
```

## Screenshots

Add screenshots here to demonstrate the UI and key application screens.

## Future Scope

- Add a real predictive model with file-based inference
- Add backend API endpoints using FastAPI or Flask
- Add automated tests for visual components and input validation
- Add CI/CD workflows and deployment instructions

## Author

- Built for portfolio presentation and recruiter review
- Contact: `your.email@example.com`
