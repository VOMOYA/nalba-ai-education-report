---
tags:
  - 探究
  - AI×教育
  - 方法論
  - 教育政策
  - 学習ロードマップ
created: 2026-03-17
updated: 2026-03-17
---

# 探究学習 × AI教育 深化のための学習マップ

> 探究学習の理論（[[探究学習の理論・エビデンス総覧]]）を起点に、さらに深めるべき思想・資料・研究者を体系的に整理したナビゲーションノート。

---

## 全体マップ

```mermaid
mindmap
  root((知識を深める\n2つの軸))
    探究学習の思想的深化
      教育哲学の系譜
        デューイ → フレイレ → イリイチ
        ビースタ 現代教育哲学
        批判的教育学 Critical Pedagogy
      日本の探究教育
        苫野一徳 教育哲学
        西岡加名恵 評価論
        田中博之 実践設計
      研究の最前線
        生成AI × IBL の融合
        デジタル技術との統合
        学習アナリティクス
    AI × 教育の思想
      国際機関の指針
        UNESCO AI 教育フレームワーク
        OECD Learning Compass 2030
        AIリテラシーフレームワーク
      批判的視点
        セルウィン AIの限界論
        アルゴリズムバイアス
        公正性・エクイティ
      実践的応用
        生成AI活用の倫理
        Human-AI Collaboration
        コンピテンシー論の更新
```

---

## 第1部：探究学習の思想的系譜を深める

### 教育哲学者の系譜

```mermaid
graph TD
  D["ジョン・デューイ\n1859–1952\n経験と探究の哲学\n『民主主義と教育』1916"]
  F["パウロ・フレイレ\n1921–1997\n批判的教育学の父\n『被抑圧者の教育学』1970"]
  I["イヴァン・イリイチ\n1926–2002\n脱学校論\n『脱学校の社会』1971"]
  P["シーモア・パパート\n1928–2016\n構成主義\nLOGO言語・作る学び"]
  B["ガート・ビースタ\n1957–\n現代最重要教育哲学者\n主体化・測定主義批判"]
  S["ニール・セルウィン\n現代\n批判的EdTech研究\nAIの限界論"]

  D -->|"対話・実践へ"| F
  D -->|"制度批判へ"| I
  D -->|"デジタル時代へ"| P
  F --> B
  I --> B
  B -->|"AI時代へ"| S

  style D fill:#FFE4B5
  style B fill:#90EE90,color:#000
  style S fill:#87CEEB,color:#000
```

---

### 思想家ごとの核心概念と読み方

#### パウロ・フレイレ（Paulo Freire）— 必読

```mermaid
graph LR
  A["銀行型教育\nBanking Education\n教師が知識を預け入れる\n一方向モデル"] -->|"批判・転換"| B["問題提起型教育\nProblem-posing Education\n学習者と教師が共に問いを立てる"]
  B --> C["コンシェンティザソン\n意識化\n自分の置かれた状況を\n批判的に意識する力"]
  C --> D["プラクシス\nPraxis\n省察と行動の往復による\n世界の変革"]
```

**探究学習との接続：** フレイレの「問い」は、IBL の Questioning フェーズの哲学的根拠。探究を「内容の習得」でなく「世界との関係を問い直す行為」として捉える視点を与える。

**読む順序：**
1. 『被抑圧者の教育学』*Pedagogy of the Oppressed*（1970）— 必読原典
2. *Pedagogy of Hope*（1992）— より実践的・対話的
3. *Rethinking Freire and Illich*（Enslin et al., 2023）— 現代的批判的再読

---

#### イヴァン・イリイチ（Ivan Illich）— 制度の外から見る目

**核心：**「学習は学校制度なしに深く起きる。むしろ制度が学習を歪める」

```mermaid
graph TD
  A["学校制度の問題\n・カリキュラムによる学習の囲い込み\n・資格による知識の序列化\n・専門家依存の助長"] --> B["学習ウェブ Learning Webs\n・物へのアクセス\n・スキルの交換\n・同輩のマッチング\n・広義の教育者"]
  B --> C["自己組織的・\n自律的な学習\nSelf-directed Learning"]
  C -->|"現代での具現化"| D["インターネット・\nオープンコース\nAIチューター・\nPKMシステム"]
```

**探究学習との接続：** 「学習ウェブ」はAI時代の個別最適化学習・非制度的探究の先駆概念。Obsidian × Claude Code による知的探究まさにその実践。

---

#### ガート・ビースタ（Gert Biesta）— 現代最重要思想家

```mermaid
graph TD
  Q["教育の目的は何か？"]

  subgraph 3["教育の3領域（Biesta）"]
    A["資格付与\nQualification\n知識・スキル・能力の習得"]
    B["社会化\nSocialisation\n文化・規範・実践への参入"]
    C["主体化\nSubjectification\n固有の存在として立ち現れること"]
  end

  Q --> 3

  CRISIS["現代の危機\n測定主義（measurementism）\n学習化（learnification）\n教育がサービスに矮小化される"]
  C -->|"脅かされている"| CRISIS

  style C fill:#FFD700,color:#000
  style CRISIS fill:#ffcccc
```

**「学習化（learnification）」とは：** 教育が「何を学んだか」の測定・最適化に縮減され、「何のために学ぶか」「どんな人間になるか」という問いが消える危険。AI教育の文脈で最重要な批判概念。

**主著の読み方：**
| 書籍 | テーマ | 難度 |
|------|--------|------|
| *Beyond Learning*（2006） | 民主主義教育の再定義 | ★★★ |
| *Good Education in an Age of Measurement*（2010） | 測定主義批判・3領域論 | ★★ |
| *The Beautiful Risk of Education*（2013） | 不確実性と教育の本質 | ★★★ |

---

### 批判的教育学（Critical Pedagogy）の系譜

```mermaid
graph LR
  F["フレイレ\n意識化・対話"] --> G["ヘンリー・ジルー\nHenry Giroux\n批判的市民性\n文化政治学"]
  F --> A["マイケル・アップル\nMichael Apple\nカリキュラムの\nイデオロギー分析"]
  G --> BH["ベル・フックス\nbell hooks\nエンゲージド・\nペダゴジー\n包括的・反抑圧的実践"]
  A --> S["ニール・セルウィン\nNeil Selwyn\n批判的EdTech\nAI監視・\nアルゴリズム権力批判"]

  style S fill:#87CEEB
  style BH fill:#DDA0DD,color:#000
```

---

### 日本の探究教育：注目すべき研究者

| 研究者 | 所属 | 専門 | 代表著作 |
|--------|------|------|---------|
| **苫野一徳** | 熊本大学 | 教育哲学・「自由の相互承認」 | 『教育の力』（講談社現代新書）|
| **西岡加名恵** | 京都大学 | 教育方法学・パフォーマンス評価・UbD | 『新しい教育評価入門』（有斐閣）|
| **石井英真** | 京都大学 | カリキュラム論・学力論 | 『授業づくりの深め方』|
| **田中博之** | 早稲田大学 | 教育工学・探究授業設計 | 『高等学校 探究授業の創り方』|
| **奈須正裕** | 上智大学 | 学習科学・個別最適な学び | 『「資質・能力」と学びのメカニズム』|

---

## 第2部：AI × 教育の思想を深める

### 国際機関の枠組み

```mermaid
graph TD
  subgraph UN["国際機関のAI教育フレームワーク"]
    U["UNESCO\n・AI倫理勧告 2021\n・生成AIガイダンス 2023\n・教師コンピテンシー 2024\n・学生コンピテンシー 2024"]
    O["OECD\n・Learning Compass 2030\n・Digital Education Outlook 2023\n・AI × Equity 報告 2024"]
    E["EC / OECD 共同\nAIリテラシー\nフレームワーク 2025\nailiteracyframework.org"]
  end
  UN --> JP["日本\n文科省\n生成AI利活用\nガイドライン Ver.2.0\n2024年12月"]
```

---

### OECD Learning Compass 2030

```mermaid
graph TD
  WELL["ウェルビーイング\nWell-being 2030\n個人・社会・地球"]

  subgraph TC["トランスフォーマティブ・コンピテンシー"]
    C1["新たな価値の創造\nCreating New Value"]
    C2["緊張とジレンマの克服\nReconciling Tensions"]
    C3["責任の引き受け\nTaking Responsibility"]
  end

  AGENCY["学習者エージェンシー\nStudent Agency\n中核概念"]

  AGENCY --> TC
  TC --> WELL

  style AGENCY fill:#FFD700,color:#000
  style WELL fill:#90EE90,color:#000
```

**探究学習との接続：** 「学習者エージェンシー」は Banchi & Bell の「開放型探究（Lv4）」と直結。自ら問いを立て、方法を選び、責任を持って結論を出す力。

---

### AIリテラシーの6次元モデル（BJET 2025）

```mermaid
graph LR
  A["①認識\nAwareness\nAIの存在・影響を知る"] --> B["②知識と理解\nKnowledge\nAIの仕組みを理解する"]
  B --> C["③使用と応用\nUse\nAIを実際に使う"]
  C --> D["④評価\nEvaluation\nAIの出力を批判的に評価する"]
  D --> E["⑤創造\nCreation\nAIを使って新しいものを作る"]
  E --> F["⑥倫理的ナビゲーション\nEthical Navigation\n価値判断・社会的影響を考慮する"]

  style F fill:#FFD700,color:#000
```

---

### ニール・セルウィンのAI教育批判

```mermaid
graph TD
  A["AIの教育利用が抱える\n本質的な問題（Selwyn, 2024）"]

  B["教育プロセスの\n統計的モデル化の限界\n→ 数値に還元できない学びの喪失"]
  C["機械可読化\nmachine-readable\n→ AI が処理できる形への\n教育の歪曲"]
  D["社会的害悪の再生産\n→ マイノリティへの\nアルゴリズム的差別"]
  E["生態学的コスト\n→ データ集約型AIの\n環境負荷"]

  A --> B
  A --> C
  A --> D
  A --> E

  F["セルウィンの要求\n教育AI議論の『減速と再調整』\n権力・抵抗・公正を中心に置く"]
  B --> F
  C --> F
  D --> F
  E --> F

  style F fill:#ffcccc
```

**読む：** *Should Robots Replace Teachers?*（Polity Press, 2019）— AI教育批判の最重要書

---

### アルゴリズムバイアスと公正性

```mermaid
graph TD
  BIAS["アルゴリズムバイアスの\n4段階モデル（FairAIED, 2024）"]

  B1["①未知のバイアス\nUnknown Bias\n存在に気づいていない偏り"]
  B2["②既知のバイアス\nKnown Bias\n特定されたが未対処の偏り"]
  B3["③公正\nFairness\n個人・集団への不当な扱いを排除"]
  B4["④公平\nEquity\n構造的不平等そのものへの対処"]

  BIAS --> B1 --> B2 --> B3 --> B4

  style B4 fill:#90EE90,color:#000
```

---

## 第3部：読書・学習ロードマップ

### フェーズ別学習計画

```mermaid
graph TD
  subgraph P1["フェーズ1 基礎固め（〜3ヶ月）"]
    R1["苫野一徳『教育の力』\n教育の本質を問い直す"]
    R2["フレイレ『被抑圧者の教育学』\n批判的教育学の原典"]
    R3["UNESCO 生成AIガイダンス 2023\nAI教育政策の国際基準"]
  end

  subgraph P2["フェーズ2 思想の深化（3〜6ヶ月）"]
    R4["Biesta『Good Education\nin an Age of Measurement』\n測定主義批判・3領域論"]
    R5["Selwyn『Should Robots\nReplace Teachers?』\nAI教育批判の必読書"]
    R6["OECD Learning Compass 2030\nコンピテンシー論の最前線"]
  end

  subgraph P3["フェーズ3 専門化（6ヶ月〜）"]
    R7["Biesta『The Beautiful\nRisk of Education』\n不確実性の教育哲学"]
    R8["IBL × 生成AI の最新論文\nIJSE 2025・F1000 2024"]
    R9["AILit Framework 2025\nEC/OECDのリテラシー枠組み"]
  end

  P1 --> P2 --> P3
```

---

### 書籍リスト

#### 教育哲学・探究学習（洋書）

| タイトル | 著者・年 | 難度 | ポイント |
|---------|---------|------|---------|
| *Pedagogy of the Oppressed* | Freire, 1970 | ★★ | 批判的教育学の原典・探究の政治的意味 |
| *Deschooling Society* | Illich, 1971 | ★★ | 制度批判・学習ウェブの先駆 |
| *Beyond Learning* | Biesta, 2006 | ★★★ | 民主主義教育の哲学的再定義 |
| *Good Education in an Age of Measurement* | Biesta, 2010 | ★★ | 3領域論・測定主義批判 |
| *The Beautiful Risk of Education* | Biesta, 2013 | ★★★ | 不確実性と主体化 |
| *Rethinking Freire and Illich* | Enslin et al., 2023 | ★★★ | フレイレ・イリイチの現代的再読 |

#### AI × 教育（洋書）

| タイトル | 著者・年 | 難度 | ポイント |
|---------|---------|------|---------|
| *Should Robots Replace Teachers?* | Selwyn, 2019 | ★★ | AI教育批判の必読書 |
| *Co-Intelligence* | Mollick, 2024 | ★ | AIとの協働の哲学と実践 |
| *Brave New Words* | Khan, 2024 | ★ | Khan AcademyのAI教育ビジョン |
| *Teaching with AI* | Bowen & Watson | ★★ | 高等教育向けAI実践指南 |
| *Handbook of Artificial Intelligence in Education* | 多著者, 2023 | ★★★ | AIED分野の包括的参照書 |

#### 和書

| タイトル | 著者・年 | ポイント |
|---------|---------|---------|
| 『教育の力』 | 苫野一徳, 2014 | 「自由の相互承認」による公教育哲学・まず読む一冊 |
| 『学校をつくり直す』 | 苫野一徳, 2019 | 学校制度の根本的再設計論 |
| 『新しい教育評価入門』 | 西岡・石井・田中編 | パフォーマンス評価・探究評価の基礎 |
| 『高等学校 探究授業の創り方』 | 田中博之 | 探究授業設計の実践書 |
| 『探究学習白書2024』 | ESIBLA | 日本の探究実態の最新統計 |

---

### 論文・レポートリスト

#### 最新・最重要

| 論文 | 年 | ポイント |
|-----|-----|---------|
| Selwyn「On the Limits of AI in Education」| 2024 | AIの限界論・批判的視点の核 |
| "Systematic review of IBL" F1000Research | 2024 | 探究学習の効果g=0.893の最新統合 |
| "Roles of digital tech in IBL" ScienceDirect | 2024 | テクノロジーと探究の7つの役割 |
| "Adaptive IBL using generative AI" IJSE | 2025 | 生成AI×IBLの実証研究・最前線 |
| "Algorithmic Bias in Educational Systems" WJARR | 2025 | AI教育のバイアス問題・包括的整理 |
| "Towards Responsible AI in Education" Nature | 2025 | 責任あるAI教育の系統的レビュー |
| "AI Literacy Competency Framework" BJET | 2025 | AIリテラシーの6次元モデル |
| UNESCO "Generative AI in Education" | 2023 | 国際機関の公式指針・政策の出発点 |
| OECD "AI and Equity in Education" | 2024 | AI×公正性の国際的分析 |

---

### オンラインリソース

```mermaid
graph LR
  subgraph INT["国際機関"]
    U["UNESCO AI in Education\nunesco.org/digital-education/AI"]
    O["OECD Learning Compass\noecd.org/learning-compass-2030"]
    A["AILit Framework\nailiteracyframework.org"]
  end

  subgraph DB["論文データベース"]
    E["ERIC\neric.ed.gov\n教育学英語論文"]
    J["J-STAGE\njstage.jst.go.jp\n日本学術雑誌"]
    C["CiNii Research\ncir.nii.ac.jp\n日本語論文"]
  end

  subgraph CRIT["批判的EdTech"]
    S["criticaledtech.com\nセルウィンのブログ"]
    H["Stanford HAI\nhai.stanford.edu"]
  end

  subgraph JP["日本"]
    M["文科省 生成AIガイドライン\nmext.go.jp"]
    ES["探究学習白書\nesibla.or.jp"]
  end
```

---

## 第4部：2025年の最重要トレンド

```mermaid
graph TD
  T1["① 生成AI × IBL の融合\nLLMが探究学習の\n適応的支援ツールとして機能\n「AI支援型探究」パラダイム形成中"]

  T2["② 主体化の危機とチャンス\nビースタの「主体化」が\nAIの最適化・効率化圧力と衝突\n→ 現代教育哲学の最大論点"]

  T3["③ 批判的AI教育学の台頭\nセルウィン・ジルーの系譜\nアルゴリズム的権力への批判的意識\n→ AIリテラシーの倫理的核へ"]

  T4["④ 日本固有の転換点\n総合的な探究の時間の本格実施\n× 生成AIガイドラインVer.2.0\n→ 2026年以降の実践の鍵"]

  T5["⑤ コンピテンシー論の更新\nOECD Compass 2030 ×\nAIリテラシーフレームワークの統合\n→ 次期カリキュラム改革の指針"]

  T1 --> T2 --> T3 --> T4 --> T5
```

---

## 自分の探究との接続（KAEL への示唆）

```mermaid
graph TD
  A["北田朋也の実践軸\n探究・ファシリテーション・AI×教育"]

  B["フレイレの対話的探究\n→ 問いを与えるのではなく\n問いを共に生み出すファシリテーション"]

  C["ビースタの主体化\n→ 効率・成果だけでなく\n『その人として立ち現れる』場をつくる"]

  D["セルウィンの批判的視点\n→ AIを使いながらも\nAIに問いを立てる力を育てる"]

  E["OECD エージェンシー\n→ 探究の主導権を\n学習者に段階的に渡していく"]

  A --> B
  A --> C
  A --> D
  A --> E
```

---

## 関連ノート

- [[探究学習の理論・エビデンス総覧]]
- [[ファシリテーションの理論]]
- [[KAEL 活動記録]]
- [[総合的な探究の時間 実践メモ]]
