"""Smoke: command shapes match real signal-cli syntax. Dry-run only."""

import os, subprocess, pathlib

os.chdir(pathlib.Path(__file__).parent)

# plain send: send -m msg RECIPIENT, no --story anywhere
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
        "--dry-run",
    ],
    capture_output=True,
    text=True,
)
assert r.returncode == 0, r.stderr
assert "sendStory" not in r.stdout and "--story" not in r.stdout, r.stdout
assert "-m" in r.stdout and "+1001" in r.stdout, r.stdout

# story: sendStory -a file, no -m, no recipients
r = subprocess.run(
    [
        "python3",
        "signal_story.py",
        "--sender",
        "+1000",
        "--story",
        "--attachment",
        "pic.jpg",
        "--dry-run",
    ],
    capture_output=True,
    text=True,
)
assert r.returncode == 0, r.stderr
assert "sendStory" in r.stdout and "-a" in r.stdout, r.stdout
assert "send --story" not in r.stdout, r.stdout

# story without attachment must fail loudly, not print a bogus command
r = subprocess.run(
    ["python3", "signal_story.py", "--sender", "+1000", "--story", "--dry-run"],
    capture_output=True,
    text=True,
)
assert r.returncode != 0, "story without attachment should exit non-zero"

print("signal-story-sender smoke OK")
