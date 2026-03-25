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
source: "https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything"
---

# Profiling Hacker News users based on their comments

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-21
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything)

---

## 📝 要約・抜粋

Here's a mildly dystopian prompt I've been experimenting with recently: "Profile this user", accompanied by a copy of their last 1,000 comments on Hacker News.
Obtaining those comments is easy. The Algolia Hacker News API supports listing comments sorted by date that have a specific tag, and the author of a comment is tagged there as author_username. Here's a JSON feed of my (simonw) most recent comments, for example:
https://hn.algolia.com/api/v1/search_by_date?tags=comment,author_simonw&hitsPerPage=1000
The Algolia API is served with open CORS headers, which means you can access the API from JavaScript running on any web page.
Last August I had ChatGPT build me a simple tool for hitting that API for any user which fetches their comments and gives me a mobile-friendly "copy to clipboard" button. I've since tweaked it a few times with Claude.
I can then paste the whole lot into any LLM - these days I mostly use Claude Opus 4.6 for this - and prompt "profile this user" to see what it can figure out.
It's startlingly effective! It feels invasive to quote the profile of another user here, so I'll show you what it produces for me:

This is Simon Willison — a prolific, independent software developer, blogger, and one of the most visible voices in the AI-assisted coding space. Here's a profile drawn from his comments:
Professional identity: Independent developer and writer. Co-creator of Django, creator of Datasette and many other open source tools. On the board of the Python Softw…

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
