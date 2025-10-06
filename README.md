# AWS SAA Study Hub

AWS Certified Solutions Architect – Associate (SAA) の学習を効率化するためのリポジトリです。  
MkDocs + Material テーマで構築したドキュメントサイトを GitHub Pages で公開し、進捗ログや PDF 資料から
自動生成されるページを組み合わせて、学習状況を一元管理できます。

---

## 📌 このリポジトリでできること

- **学習ポータルの公開**: MkDocs サイトを GitHub Pages に自動デプロイ。
- **自動生成コンテンツ**:
  - `progress.csv` から週次学習サマリー (`docs/Progress Weekly Summary.md`) を作成。
  - `docs/references/*.pdf` を列挙し、参照資料のインデックス (`docs/references/index.md`) を生成。
  - `docs/notes/*.md` からノート一覧 (`docs/notes/index.md`) を生成。
- **スケジュール運用**: GitHub Actions が定期実行され、データに合わせてコンテンツとサイトを更新。
- **シングルソース管理**: CSV・Markdown・PDF を同じリポジトリでバージョン管理し、そのままサイトに反映。

---

## 🗂 ディレクトリ構成（抜粋）

| パス | 内容 |
| --- | --- |
| `docs/` | MkDocs のソース。トップページ、タイムライン、学習ノート、進捗ページなど。 |
| `docs/references/` | 参照用 PDF と `refs_meta.json`（任意）。インデックス生成スクリプトの入力。 |
| `docs/notes/` | 学習ノートの Markdown。ノート一覧は自動生成。 |
| `progress.csv` | 日々の学習ログ。週次サマリーの元データ。 |
| `scripts/` | CSV/PDF/ノートを加工して Markdown を生成する Python スクリプト群。 |
| `mkdocs.yml` | サイト設定（ナビゲーション・テーマ・拡張機能）。 |
| `.github/workflows/` | ビルドと定期更新を担う GitHub Actions ワークフロー。 |

---

## 🚀 はじめ方

1. **リポジトリを取得し、依存パッケージを入れる**

   ```bash
   git clone <your-fork-url>
   cd aws-saa-ghpages-kit
   python3 -m venv .venv && source .venv/bin/activate
   pip install mkdocs-material
   ```

2. **必要に応じて派生コンテンツをローカル生成**

   ```bash
   python scripts/build_references_index.py
   python scripts/build_notes_index.py
   python scripts/build_weekly_summary.py
   ```

3. **サイトをプレビュー**

   ```bash
   mkdocs serve
   ```

4. **公開**

   `main` ブランチに push すると、GitHub Actions が自動的にサイトをビルドし GitHub Pages に反映します。

---

## ✍️ コンテンツ作成フロー

- **学習ノート**: `docs/notes/` に Markdown ファイルを追加。スクリプト実行後、ノート一覧に自動反映。
- **参照資料**: `docs/references/` に PDF を追加。必要に応じて `refs_meta.json` にタイトルや説明を記載。
- **学習ログ**: `progress.csv` にレコードを追記（`date, week, topic, planned_hours, actual_hours, ...`）。週次サマリーに集計されます。

これらのファイルを更新してコミットすると、ワークフローが対応する Markdown を再生成してくれます。

---

## 🤖 自動化ワークフロー

| ファイル | トリガー | 処理内容 |
| --- | --- | --- |
| `.github/workflows/pages.yml` | `main` への push、手動実行 | MkDocs + 依存パッケージのセットアップ → サイトをビルド → Pages 用アーティファクトをアップロード → GitHub Pages にデプロイ。 |
| `.github/workflows/weekly-summary.yml` | 週次 cron（毎週日曜 12:00 UTC）、手動実行 | 3 つのスクリプト（週次サマリー・リファレンス・ノート）を実行し、更新があればコミットして push。 |

ローカルでも同じスクリプトを実行できるため、コミット前に結果を確認したい場合に活用してください。

---

## ✅ 運用のヒント

- 大きな PDF は確定版のみをコミットし、差し替えは必要最小限にすると履歴が扱いやすくなります。
- `progress.csv` は表計算ソフトなどで整形しつつ編集し、欠損値やフォーマット崩れを防ぎましょう。
- `docs/` 配下の Markdown は直接編集し、`docs/Progress Weekly Summary.md` など自動生成ファイルは手で修正しないようにします。
- 依存パッケージや `mkdocs.yml` を変更した際は `mkdocs serve` で表示を確認してから push すると安心です。

学習とアウトプットの場として、自由にカスタマイズしてご活用ください！

