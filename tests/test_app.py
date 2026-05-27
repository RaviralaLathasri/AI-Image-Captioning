import importlib.util
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

import app


def test_main_callable():
    assert callable(app.main)


def test_app_imports():
    assert hasattr(app, "main")
    assert hasattr(app, "render_sidebar")
