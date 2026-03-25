---
tags:
  - Simon Willison
  - AI
  - ソフトウェア開発
  - 英語
created: 2026-03-25
updated: 2026-03-25
著者: Simon Willison
公開日: 2026-03-20
source: "https://simonwillison.net/2026/Mar/20/sqlite-tags-benchmark/#atom-everything"
---

# SQLite Tags Benchmark: Comparing 5 Tagging Strategies

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-20
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/20/sqlite-tags-benchmark/#atom-everything)

---

## 📝 要約・抜粋

Research: SQLite Tags Benchmark: Comparing 5 Tagging Strategies
    I had Claude Code run a micro-benchmark comparing different approaches to implementing tagging in SQLite. Traditional many-to-many tables won, but FTS5 came a close second. Full table scans with LIKE queries performed better than I expected, but full table scans with JSON arrays and json_each() were much slower.
    
        Tags: json, sqlite

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
