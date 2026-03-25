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
source: "https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything"
---

# Package Managers Need to Cool Down

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-24
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything)

---

## 📝 要約・抜粋

Package Managers Need to Cool Down
Today's LiteLLM supply chain attack inspired me to revisit the idea of dependency cooldowns, the practice of only installing updated dependencies once they've been out in the wild for a few days to give the community a chance to spot if they've been subverted in some way.
This recent piece (March 4th) piece by Andrew Nesbitt reviews the current state of dependency cooldown mechanisms across different packaging tools. It's surprisingly well supported! There's been a flurry of activity across major packaging tools, including:

pnpm 10.16 (September 2025) — minimumReleaseAge with minimumReleaseAgeExclude for trusted packages
Yarn 4.10.0 (September 2025) — npmMinimalAgeGate (in minutes) with npmPreapprovedPackages for exemptions
Bun 1.3 (October 2025) — minimumReleaseAge via bunfig.toml
Deno 2.6 (December 2025) — --minimum-dependency-age for deno update and deno outdated
uv 0.9.17 (December 2025) — added relative duration support to existing --exclude-newer, plus per-package overrides via exclude-newer-package
pip 26.0 (January 2026) — --uploaded-prior-to (absolute timestamps only; relative duration support requested)
npm 11.10.0 (February 2026) — min-release-age

pip currently only supports absolute rather than relative dates but Seth Larson has a workaround for that using a scheduled cron to update the absolute date in the pip.conf config file.

    Tags: javascript, packaging, pip, pypi, python, security, npm, deno, supply-chain, uv

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
