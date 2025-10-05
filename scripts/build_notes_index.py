# scripts/build_notes_index.py
import os, re, html

ROOT = os.path.dirname(os.path.dirname(__file__))
NOTES_DIR = os.path.join(ROOT, "docs", "notes")
OUT = os.path.join(NOTES_DIR, "index.md")

def title_of(path):
    # 最初の # 見出し行をタイトルとして取得。なければファイル名を整形。
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^#\s+(.+)$", line.strip())
            if m:
                return m.group(1).strip()
    base = os.path.splitext(os.path.basename(path))[0]
    return base.replace("_", " ").replace("-", " ").title()

def main():
    if not os.path.isdir(NOTES_DIR):
        os.makedirs(NOTES_DIR, exist_ok=True)

    items = []
    for fn in sorted(os.listdir(NOTES_DIR)):
        if not fn.endswith(".md") or fn.lower() == "index.md":
            continue
        items.append(fn)

    lines = [
        "# 🗒️ Notes",
        "",
        "以下は `docs/notes/` にあるノートを自動で一覧化したものです。",
        "",
        "| ノート一覧 |",
        "|---|",
    ]

    if not items:
        lines += ["> まだノートがありません。`docs/notes/` に `.md` を追加してください。"]
    else:
        for fn in items:
            title = title_of(os.path.join(NOTES_DIR, fn))
            link = fn.replace(".md", "")
            lines.append(f"| [{html.escape(title)}]({link}) |")

    with open(OUT, "w", encoding="utf-8") as w:
        w.write("\n".join(lines))

if __name__ == "__main__":
    main()