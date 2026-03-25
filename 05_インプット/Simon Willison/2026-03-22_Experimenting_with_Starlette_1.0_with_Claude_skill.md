---
tags:
  - Simon Willison
  - AI
  - ソフトウェア開発
  - 英語
  - 生成AI
created: 2026-03-25
updated: 2026-03-25
著者: Simon Willison
公開日: 2026-03-22
source: "https://simonwillison.net/2026/Mar/22/starlette/#atom-everything"
---

# Experimenting with Starlette 1.0 with Claude skills

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-22
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything)

---

## 📝 要約・抜粋

Starlette 1.0 is out! This is a really big deal. I think Starlette may be the Python framework with the most usage compared to its relatively low brand recognition because Starlette is the foundation of FastAPI, which has attracted a huge amount of buzz that seems to have overshadowed Starlette itself.
Kim Christie started working on Starlette in 2018 and it quickly became my favorite out of the new breed of Python ASGI frameworks. The only reason I didn't use it as the basis for my own Datasette project was that it didn't yet promise stability, and I was determined to provide a stable API for Datasette's own plugins... albeit I still haven't been brave enough to ship my own 1.0 release (after 26 alphas and counting)!
Then in September 2025 Marcelo Trylesinski announced that Starlette and Uvicorn were transferring to their GitHub account, in recognition of their many years of contributions and to make it easier for them to receive sponsorship against those projects.
The 1.0 version has a few breaking changes compared to the 0.x series, described in the release notes for 1.0.0rc1 that came out in February.
The most notable of these is a change to how code runs on startup and shutdown. Previously that was handled by on_startup and on_shutdown parameters, but the new system uses a neat lifespan mechanism instead based around an async context manager:
@contextlib.asynccontextmanager
async def lifespan(app):
    async with some_async_resource():
        print("Run at startup!")
  …

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
