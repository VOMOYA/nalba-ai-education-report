---
tags:
  - Simon Willison
  - AI
  - ソフトウェア開発
  - 英語
created: 2026-03-22
updated: 2026-03-22
著者: Simon Willison
公開日: 2026-03-21
source: "https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/#atom-everything"
---

# Using Git with coding agents

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-21
> - **URL**：[元記事を読む](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/#atom-everything)

---

## 📝 要約・抜粋

Agentic Engineering Patterns >
    Git is a key tool for working with coding agents. Keeping code in version control lets us record how that code changes over time and investigate and reverse any mistakes. All of the coding agents are fluent in using Git's features, both basic and advanced.
This fluency means we can be more ambitious about how we use Git ourselves. We don't need to  memorize how to do things with Git, but staying aware of what's possible means we can take advantage of the full suite of Git's abilities.
Git essentials
Each Git project lives in a repository - a folder on disk that can track changes made to the files within it. Those changes are recorded in commits - timestamped bundles of changes to one or more files accompanied by a commit message describing those changes and an author recording who made them.
Git supports branches, which allow you to construct and experiment with new changes independently of each other. Branches can then be merged back into your main branch (using various methods) once they are deemed ready.
Git repositories can be cloned onto a new machine, and that clone includes both the current files and the full history of changes to them.
This means developers - or coding agents - can browse and explore that history without any extra network traffic, making history diving effectively free.
Git repositories can live just on your own machine,  but Git is designed to support collaboration and backups by publishing them to a remote, which c…

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
