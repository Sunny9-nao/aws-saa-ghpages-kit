# scripts/build_notes_index.py
import os, re, html

ROOT = os.path.dirname(os.path.dirname(__file__))
NOTES_DIR = os.path.join(ROOT, "docs", "notes")
OUT = os.path.join(NOTES_DIR, "index.md")

def title_of(path):
    # 1行目の「# 見出し」をタイトルとして抽出。なければファイル名を整形
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
    for root, _, files in os.walk(NOTES_DIR):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            if fn.lower() == "index.md":
                continue
            rel = os.path.relpath(os.path.join(root, fn), NOTES_DIR)
            items.append(rel)
    items.sort(key=lambda p: p.lower())

    lines = ["# 🗒️ Notes", "", "以下は `docs/notes/` のMarkdownを自動一覧化したものです。", ""]
    if not items:
        lines += ["> まだノートがありません。`docs/notes/` に `.md` を追加してください。"]
    else:
        lines += ["| タイトル | パス |", "|---|---|"]
        for rel in items:
            path = os.path.join(NOTES_DIR, rel)
            title = title_of(path)
            link = rel.replace("\\\\", "/")
            lines.append(f"| {html.escape(title)} | [{html.escape(link)}]({link}) |")

    with open(OUT, "w", encoding="utf-8") as w:
        w.write("\n".join(lines))

if __name__ == "__main__":
    main()