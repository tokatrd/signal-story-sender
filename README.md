# signal-story-sender

I wanted my n8n homelab alerts to post as Signal Stories and signal-cli doesn't make it obvious how, so here's my wrapper. Posting a story is a separate subcommand (`sendStory`, image required) — not a flag on `send`.

## Prerequisites

- Python 3.8+.
- signal-cli installed and your number linked (`signal-cli link`) or registered (`signal-cli register` + `verify`). Needs a version with the `sendStory` subcommand.

## Try it (dry-run, safe)

```bash
python3 signal_story.py --sender +10000000000 --story --attachment today.jpg --dry-run
# prints: signal-cli -u +10000000000 sendStory -a today.jpg
python3 signal_story.py --sender +10000000000 --to +10000000001 --message "homelab OK" --dry-run
```

## Really sending

`--execute` without `--dry-run` performs a REAL send. Omit it to just print.

```bash
python3 test_cmd.py  # expect: signal-story-sender smoke OK
```

## n8n

1. Workflows → Import from File → pick `workflow.json`.
2. Fix the `command` path (`$HOME` should resolve; adjust account number + image path).
3. The imported command has no `--dry-run`, so a successful run posts for real. `onError` is set to continue.

MIT — see LICENSE.

*Put together with some AI help.*
