"""The 3 AM Commit Message entry: genius, denial, and fictional blame."""

import os

TEXT = (
    "wip: if this works I am a genius, if it breaks I was never here, "
    "and git blame is a work of fiction"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
