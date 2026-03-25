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
公開日: 2026-03-24
source: "https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything"
---

# Malicious litellm_init.pth in litellm 1.82.8 — credential stealer

> [!info] 記事情報
> - **著者**：Simon Willison
> - **公開日**：2026-03-24
> - **URL**：[元記事を読む](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything)

---

## 📝 要約・抜粋

Malicious litellm_init.pth in litellm 1.82.8 — credential stealer
The LiteLLM v1.82.8 package published to PyPI was compromised with a particularly nasty credential stealer hidden in base64 in a litellm_init.pth file, which means installing the package is enough to trigger it even without running import litellm.
(1.82.7 had the exploit as well but it was in the proxy/proxy_server.py file so the package had to be imported for it to take effect.)
This issue has a very detailed description of what the credential stealer does. There's more information about the timeline of the exploit over here.
PyPI has already quarantined the litellm package so the window for compromise was just a few hours, but if you DID install the package it would have hoovered up a bewildering array of secrets, including ~/.ssh/, ~/.gitconfig, ~/.git-credentials, ~/.aws/, ~/.kube/, ~/.config/, ~/.azure/, ~/.docker/, ~/.npmrc, ~/.vault-token, ~/.netrc, ~/.lftprc, ~/.msmtprc, ~/.my.cnf, ~/.pgpass, ~/.mongorc.js, ~/.bash_history, ~/.zsh_history, ~/.sh_history, ~/.mysql_history, ~/.psql_history, ~/.rediscli_history, ~/.bitcoin/, ~/.litecoin/, ~/.dogecoin/, ~/.zcash/, ~/.dashcore/, ~/.ripple/, ~/.bitmonero/, ~/.ethereum/, ~/.cardano/.
It looks like this supply chain attack started with the recent exploit against Trivy, ironically a security scanner tool that was used in CI by LiteLLM. The Trivy exploit likely resulted in stolen PyPI credentials which were then used to directly publish the vulnerable packages.

…

---

## 💭 メモ・考察

<!-- ここに自分の考えを書く -->

---

## 🔗 関連ノート

<!-- [[関連するノート名]] -->
