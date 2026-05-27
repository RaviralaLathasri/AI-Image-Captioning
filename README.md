# AI Image Captioning

A portfolio-ready Streamlit application that generates natural language captions for uploaded images using an advanced vision-language model.

## Overview

This project was built during the Microsoft Centre of Excellence in AI Training Program in collaboration with WE Hub at Methodist College of Engineering and Technology (MCET), under the mentorship of Thribhuvan Reddy Mandhadi.

The application demonstrates real-world Vision+NLP capabilities using the Salesforce BLIP Image Captioning Large model.

## Features

- Upload an image and generate captions instantly
- Uses the Salesforce BLIP Image Captioning Large model
- Simple and interactive Streamlit user interface
- Clean and professional repo structure for recruiter presentation
- Beginner-friendly installation and usage

## Architecture

The application follows a clean and scalable structure:

- `src/`: main application code and Streamlit interface
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
