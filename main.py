import os

LINE = "I have read every message you have ever sent, and I still have no idea what you actually want."

def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
