# signal-story-sender

I wanted my n8n homelab alerts to post as Signal Stories and signal-cli doesn't make it obvious how, so here's my wrapper. Dry-run prints the command so you don't need a phone number to test.

**What it does:**
- `signal_story.py` builds the correct `signal-cli send --story` invocation (`--dry-run` prints the command, so CI needs no phone number).
- `workflow.json` — n8n workflow: schedule → exec `signal_story.py` → fallback to plain `send` if Stories unsupported.

## Run
```bash
python3 signal_story.py --sender +10000000000 --to +10000000001 --message "homelab OK" --story --dry-run
python3 test_cmd.py
```

*Put together with some AI help.*
