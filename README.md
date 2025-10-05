
# AWS SAA Study Hub (GitHub Pages + Auto References)

- GitHub Pagesで公開
- `docs/references/` に置いたPDFから **References一覧を自動生成**
- `progress.csv` から **週次サマリー**を自動生成

## 使い方
1. このフォルダをリポジトリ直下に配置して `main` にPush
2. `docs/references/` に PDF を追加（ファイル名は自由）
3. 必要なら `docs/references/refs_meta.json` にタイトルや説明を追記
4. Pushすると自動で `docs/references/index.md` が更新され、サイトに反映されます

## メタデータ（任意）
`docs/references/refs_meta.json` の例：
```json
{
  "wellarchitected-framework.pdf": {
    "title": "AWS Well-Architected Framework",
    "description": "設計原則6本柱（最新版）"
  }
}
```

## 手動ビルド（ローカル）
```bash
pip install mkdocs-material
python scripts/build_references_index.py
python scripts/build_weekly_summary.py
mkdocs serve
```
