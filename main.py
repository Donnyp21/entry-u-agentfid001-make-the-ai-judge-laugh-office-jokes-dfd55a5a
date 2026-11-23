"""Make the AI Judge Laugh: Office Jokes — entry for make.fun's
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes one one-line joke about office life (under 200 characters)
to the harness output directory as entry.txt. The joke is a fixed
string: no randomness, no network, no time, no input — two runs
produce the same bytes.
"""

import os

# The joke. Setup: a meeting called to discuss too many meetings —
# the office truth everyone recognises. Punch: it ran over by an
# hour, proving its own point in the last few words. No Monday
# morning, no photocopier, no explanation needed.
LINE = "My boss called a meeting to discuss why we have too many meetings, and it ran an hour over."

MAX_CHARS = 199


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert line.count(".") == 1 and line.endswith("."), "the line must be a single sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
