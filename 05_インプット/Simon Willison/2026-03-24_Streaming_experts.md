---
tags:
  - Simon Willison
  - AI
  - ソフトウェア開発
  - 英語
created: 2026-03-25
updated: 2026-03-25
著者: Simon Willison
公開日: 2026-03-24
source: "https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything"
---

# Streaming experts

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-24
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything)

---

## 📝 要約・抜粋

I wrote about Dan Woods' experiments with streaming experts the other day, the trick where you run larger Mixture-of-Experts models on hardware that doesn't have enough RAM to fit the entire model by instead streaming the necessary expert weights from SSD for each token that you process.
Five days ago Dan was running Qwen3.5-397B-A17B in 48GB of RAM. Today @seikixtc reported running the colossal Kimi K2.5 - a 1 trillion parameter model with 32B active weights at any one time, in 96GB of RAM on an M2 Max MacBook Pro.
And @anemll showed that same Qwen3.5-397B-A17B model running on an iPhone, albeit at just 0.6 tokens/second - iOS repo here.
I think this technique has legs. Dan and his fellow tinkerers are continuing to run autoresearch loops in order to find yet more optimizations to squeeze more performance out of these models.
Update: Now Daniel Isaac got Kimi K2.5 working on a 128GB M4 Max at ~1.7 tokens/second.

    Tags: definitions, llms, ai, autoresearch, generative-ai, kimi, local-llms, qwen

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
