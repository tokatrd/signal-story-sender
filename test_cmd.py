"""Smoke: dry-run prints a plausible signal-cli command."""
import os, subprocess, pathlib
os.chdir(pathlib.Path(__file__).parent)


r = subprocess.run(
    [
        "python3",
        "signal_story.py",
        "--sender",
        "+1000",
        "--to",
        "+1001",
        "--message",
        "hi",
        "--story",
        "--dry-run",
    ],
    capture_output=True,
    text=True,
)
assert r.returncode == 0 and "signal-cli" in r.stdout and "--story" in r.stdout, (
    r.stdout
)
print("signal-story-sender smoke OK")
