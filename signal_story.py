"""Build signal-cli commands. Prints by default; only sends with --execute.

Story posting uses the real `sendStory` subcommand (attachment required):
  signal-cli -u SENDER sendStory -a IMAGE.jpg [-g GROUP]
Plain sends use `send`:
  signal-cli -u SENDER send -m "text" RECIPIENT...
"""

import argparse, shlex, subprocess


def build_cmd(sender, recipients, message=None, attachment=None, story=False):
    if story:
        if not attachment:
            raise ValueError(
                "--story requires --attachment (sendStory posts an image/video)"
            )
        return ["signal-cli", "-u", sender, "sendStory", "-a", attachment]
    if not recipients:
        raise ValueError("plain send needs at least one --to recipient")
    cmd = ["signal-cli", "-u", sender, "send"]
    if message:
        cmd += ["-m", message]
    if attachment:
        cmd += ["-a", attachment]
    return cmd + list(recipients)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Build (and optionally run) signal-cli send/sendStory commands."
    )
    ap.add_argument(
        "--sender",
        required=True,
        help="your signal-cli account (phone number, must be linked/registered first)",
    )
    ap.add_argument(
        "--to", nargs="*", default=[], help="recipient phone number(s) for plain sends"
    )
    ap.add_argument(
        "--message",
        default="homelab alert",
        help="text for plain sends (sendStory posts images, not text)",
    )
    ap.add_argument(
        "--attachment", default=None, help="image/video file; required for --story"
    )
    ap.add_argument(
        "--story", action="store_true", help="post as a Story (needs --attachment)"
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print the command without running it (default behaviour anyway)",
    )
    ap.add_argument(
        "--execute",
        action="store_true",
        help="actually run signal-cli (REAL send; omit to just print)",
    )
    a = ap.parse_args()
    try:
        cmd = build_cmd(a.sender, a.to, a.message, a.attachment, a.story)
    except ValueError as e:
        ap.error(str(e))
    print(shlex.join(cmd))
    if a.execute and not a.dry_run:
        subprocess.run(cmd, check=True)
