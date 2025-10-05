# Timeline

!!! tip "Mermaid でタイムライン表示"
下のガントチャートは **Mermaid** で描画されます。

```mermaid
gantt
    title AWS SAA 3ヶ月学習タイムライン（合格フォーカス）
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d

    section フェーズ0：準備
    AWS環境・ping-t設定・書籍準備                     :done, prep, 2025-10-06, 3d

    section フェーズ1：基礎と安全性（Week1〜5）
    Week1〜2 IAM・セキュリティ・責任共有モデル        :active, w1, 2025-10-09, 14d
    Week3〜4 VPC／ネットワーク設計（最重要・最難関）   :w3, 2025-10-23, 14d
    Week5 ストレージ＋可用性（S3・EBS・Route53）      :w5, 2025-11-06, 7d

    section フェーズ2：設計判断と性能（Week6〜9）
    Week6 コンピュート（EC2／Lambda／Fargate）        :w6, 2025-11-13, 7d
    Week7〜8 データベース（RDS／Aurora／DynamoDB）     :w7, 2025-11-20, 14d
    Week9 ネットワーク最適化／監視・運用（CloudFront等）:w9, 2025-12-04, 7d

    section フェーズ3：模試・仕上げ（Week10〜12）
    Week10 コスト最適化／横断整理（RI／Savings Plan） :w10, 2025-12-11, 7d
    Week11 模試・ping-t全復習                         :w11, 2025-12-18, 7d
    Week12 WAF6本柱整理＋直前調整                     :crit, w12, 2025-12-25, 7d

    section 試験本番
    SAA受験（合格目標）                              :milestone, exam, 2026-01-05, 1d
```

## 週次チェックリスト

- [ ] Week1-2：IAM 30〜50 問 + 書籍 1〜2 回転
- [ ] Week3-4：VPC 50〜70 問 + ハンズオン
- [ ] Week5：S3/EBS/可用性
- [ ] Week6：Compute
- [ ] Week7-8：DB（RDS/Aurora/DynamoDB）
- [ ] Week9：エッジ/監視
- [ ] Week10：コスト
- [ ] Week11：模試＋総復習
- [ ] Week12：最終調整
