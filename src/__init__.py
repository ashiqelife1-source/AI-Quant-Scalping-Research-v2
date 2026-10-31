from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

__all__ = ["ROOT", "SRC"]
