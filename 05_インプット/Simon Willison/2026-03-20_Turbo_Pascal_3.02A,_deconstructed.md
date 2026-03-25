---
tags:
  - Simon Willison
  - AI
  - ソフトウェア開発
  - 英語
created: 2026-03-22
updated: 2026-03-22
著者: Simon Willison
公開日: 2026-03-20
source: "https://simonwillison.net/2026/Mar/20/turbo-pascal/#atom-everything"
---

# Turbo Pascal 3.02A, deconstructed

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-20
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/20/turbo-pascal/#atom-everything)

---

## 📝 要約・抜粋

Turbo Pascal 3.02A, deconstructed
In Things That Turbo Pascal is Smaller Than James Hague lists things (from 2011) that are larger in size than Borland's 1985 Turbo Pascal 3.02 executable - a 39,731 byte file that somehow included a full text editor IDE and Pascal compiler.
This inspired me to track down a copy of that executable (available as freeware since 2000) and see if Claude could interpret the binary and decompile it for me.
It did a great job, so I had it create this interactive artifact illustrating the result. Here's the sequence of prompts I used (in regular claude.ai chat, not Claude Code):

Read this https://prog21.dadgum.com/116.html
Now find a copy of that binary online
Explore this (I attached the zip file)
Build an artifact - no react - that embeds the full turbo.com binary and displays it in a way that helps understand it - broke into labeled segments for different parts of the application, decompiled to visible source code (I guess assembly?) and with that assembly then reconstructed into readable code with extensive annotations

Update: Annoyingly the Claude share link doesn't show the actual code that Claude executed, but here's the zip file it gave me when I asked to download all of the intermediate files.
I ran Codex CLI with GPT-5.4 xhigh against that zip file to see if it would spot any obvious hallucinations, and it did not. This project is low-enough stakes that this gave me enough confidence to publish the result!

    Tags: computer-history, tool…

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
