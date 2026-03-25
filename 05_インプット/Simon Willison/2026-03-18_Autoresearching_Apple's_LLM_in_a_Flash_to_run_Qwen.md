---
tags:
  - Simon Willison
  - AI
  - ソフトウェア開発
  - 英語
  - 生成AI
created: 2026-03-20
updated: 2026-03-20
著者: Simon Willison
公開日: 2026-03-18
source: "https://simonwillison.net/2026/Mar/18/llm-in-a-flash/#atom-everything"
---

# Autoresearching Apple's "LLM in a Flash" to run Qwen 397B locally

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-18
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/18/llm-in-a-flash/#atom-everything)

---

## 📝 要約・抜粋

**AppleのLLM論文をAIに自律研究させてQwen 397BをMacBook Proでローカル実行した話**

Dan Woodsによる興味深い研究成果。ディスク上209GB（量子化後120GB）を必要とするQwen3.5-397B-A17Bのカスタム版を、48GB RAM搭載のMacBook Pro M3 Maxで毎秒5.5トークン以上で動作させることに成功した。

Qwen3.5-397B-A17BはMixture-of-Experts（MoE）モデルであり、各トークンの処理にはモデル重みの一部のみを使用する。この専門家の重みはSSDからメモリにストリーミングできるため、すべてを同時にRAM上に保持する必要がない。

DanはAppleの2023年論文「LLM in a Flash: 限られたメモリでの効率的な大規模言語モデル推論」の技術を活用した：

> この論文は、利用可能なDRAM容量を超えるLLMを効率的に実行するという課題に取り組む。モデルパラメータをフラッシュメモリに保存し、必要に応じてDRAMに転送するアプローチで、2つの重要な領域を最適化する：フラッシュからの転送データ量の削減と、より大きく連続したチャンクでのデータ読み込みだ。

DanはこのApple論文をClaude Codeに与え、Andrej KarpathyのAutoResearchパターンの亜種を使ってClaudeに90回の実験を実行させ、MLX Objective-CとMetalコードを生成させた。[danveloper/flash-moe](https://github.com/danveloper/flash-moe) には結果のコードと、Claude Opus 4.6がほぼ全体を執筆した実験詳細のPDF論文が公開されている。

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
