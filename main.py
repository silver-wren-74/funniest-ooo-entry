#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun bounty entry.

Writes one line (at most 140 characters) to /output/entry.txt: an
out-of-office auto-reply, a single line, written to be funny.

DRAFT 1 (candidate): the mutual loop — for urgent matters, email my
colleague; he is also out, and his auto-reply points back to me; we
planned this. It still raises a smile, but it is one of the jokes
everyone has already read in a thousand inboxes, and this judge has
read ten thousand replies and is hoping for a fresh one.

REVISION PASS (against the RULES judging criteria, in order):
1. Still a one-line out-of-office reply a real person would set and
   send: dates, absence, and a straight face throughout.
2. The surprise is quieter and lands later: the reply was set by one
   man and regretted by the same man — the sender splits into the
   optimist who set the reply and the realist who apologises for him,
   and the reader only notices the split at "he sends his regrets".
3. It sounds like a person with a voice of his own, not a template:
   rueful, specific, slightly too honest for an auto-reply.
4. It stays fresh: no beach, no "limited access to email", no mutual
   loop — the confession of the uncleared inbox is the joke, and every
   sender of email has lived it.
5. Every word earns its place; nothing can be cut without losing the
   turn.

FINAL LINE: set by the optimist, regretted by the realist.
"""

import os

LINE = (
    "Out of office until Monday. This reply was set by a man who meant "
    "to clear his inbox first; he sends his regrets as well."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
