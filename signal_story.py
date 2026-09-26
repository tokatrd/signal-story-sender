"""Build signal-cli --story command. Dry-run by default so CI needs no phone."""

import argparse, shlex, subprocess


def build_cmd(sender, recipients, message=None, attachment=None, story=False):
    # real signal-cli syntax: signal-cli -u SENDER send -m "msg" [-a file] RECIPIENT...
    cmd = ["signal-cli", "-u", sender, "send"]
    if story:
        cmd.append("--story")
    if message:
        cmd += ["-m", message]
    if attachment:
        cmd += ["-a", attachment]
    cmd += recipients
    return cmd


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sender", required=True)
    ap.add_argument("--to", nargs="+", required=True)
    ap.add_argument("--message", default="homelab alert ✓")
    ap.add_argument("--attachment")
    ap.add_argument("--story", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--execute", action="store_true")
    a = ap.parse_args()
    cmd = build_cmd(a.sender, a.to, a.message, a.attachment, a.story)
    print(shlex.join(cmd))
    if a.execute and not a.dry_run:
        subprocess.run(cmd, check=True)
