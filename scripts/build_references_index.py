
import os, json, html

ROOT = os.path.dirname(os.path.dirname(__file__))
REF_DIR = os.path.join(ROOT, "docs", "references")
OUT = os.path.join(REF_DIR, "index.md")
META_PATH = os.path.join(REF_DIR, "refs_meta.json")

def human_title(fn: str) -> str:
    name = os.path.splitext(fn)[0]
    name = name.replace("_", " ").replace("-", " ")
    return name.title()

def main():
    files = [f for f in os.listdir(REF_DIR) if f.lower().endswith(".pdf")]
    files.sort()
    meta = {}
    if os.path.exists(META_PATH):
        try:
            with open(META_PATH, encoding="utf-8") as m:
                meta = json.load(m)
        except Exception:
            meta = {}

    lines = ["# 📚 References", "", "以下は `docs/references/` 配下のPDFを自動列挙した一覧です。", "", "| 資料名 | 説明 | リンク |", "|---|---|---|"]
    for f in files:
        info = meta.get(f, {})
        title = info.get("title") or human_title(f)
        desc = info.get("description") or ""
        link = f"{f}"
        lines.append(f"| {html.escape(title)} | {html.escape(desc)} | [ダウンロード]({link}) |")

    if not files:
        lines += ["", "> まだPDFがありません。`docs/references/` にファイルを追加して再実行してください。"]

    with open(OUT, "w", encoding="utf-8") as w:
        w.write("\n".join(lines))

if __name__ == "__main__":
    main()
