<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"私たちは、エージェントがシームレスに相互通信できる世界を想像しています。<br/>
  そしてBinduは、あなたのエージェントを生きたサーバーに変え、エージェントのインターネットの点（Bindu）にします。"</em>
</p>

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> •
  <a href="README.es.md">🇪🇸 Español</a> •
  <a href="README.fr.md">🇫🇷 Français</a> •
  <a href="README.ja.md">🇯🇵 日本語</a> •
  <a href="README.bn.md">🇧🇩 বাংলা</a> •
  <a href="README.hi.md">🇮🇳 हिन्दी</a> •
  <a href="README.ta.md">🇮🇳 தமிழ்</a> •
  <a href="README.de.md">🇩🇪 Deutsch</a> •
  <a href="README.nl.md">🇳🇱 Nederlands</a>
</p>

<br/>

<p align="center">
  <a href="https://youtu.be/obY1bGOoWG8?si=uEeDb0XWrtYOQTL7">
    <img src="https://img.youtube.com/vi/obY1bGOoWG8/maxresdefault.jpg" alt="チュートリアルビデオを見る"/>
  </a>
</p>

<br/>

[![GitHub License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Hits](https://hits.sh/github.com/getbindu/create-bindu-agent.svg)](https://hits.sh/github.com/getbindu/create-bindu-agent/)
[![Main](https://github.com/getbindu/create-bindu-agent/actions/workflows/main.yml/badge.svg)](https://github.com/getbindu/create-bindu-agent/actions/workflows/main.yml)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/getbindu/create-bindu-agent/pulls)
[![Join Discord](https://img.shields.io/badge/Join%20Discord-7289DA?logo=discord&logoColor=white)](https://discord.gg/3w5zuYUuwt)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.getbindu)
[![GitHub stars](https://img.shields.io/github/stars/getbindu/create-bindu-agent)](https://github.com/getbindu/create-bindu-agent/stargazers)

<br/>


## ゼロから本番環境対応エージェントまで2分で

**Create Bindu Agent**は、エージェントのインターネットの言語を話す本番環境対応のAIエージェントを構築する最速の方法です。ボイラープレートなし。設定地獄なし。設定するだけで、**A2A**、**AP2**、**X402**プロトコルを使用して通信する完全にデプロイ可能なエージェントが手に入ります。

<br/>

## クイックスタート

**最初のエージェントまでの時間：約2分** ⏱️

ローカルマシンで、プロジェクトディレクトリを作成したいディレクトリに移動し、次のコマンドを実行します：

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

### 次に何が起こるか？

以下の入力を求められます：
- **プロジェクト名**と**説明**
- **エージェントフレームワーク**（Agno、LangChain、CrewAIなど）
- **ライセンスタイプ**（MIT、Apache、BSD、GPL、ISC）
- **著者の詳細**

そして、**ドーン！** 💥 エージェントプロジェクトの準備が整いました：

```
your-agent/
├── agent_config.json          # A2A/AP2/X402設定を含むエージェント設定
├── your_agent/
│   ├── main.py               # エージェントのエントリーポイント（すでにBindu化済み！）
│   └── __init__.py
├── skills/                   # エージェントスキルを追加するためのテンプレート
├── tests/                    # 事前設定されたpytestテスト
├── pyproject.toml            # uvで管理される依存関係
├── Dockerfile                # コンテナ化の準備完了
├── .github/workflows/        # CI/CDパイプライン
└── README.md                 # 完全なセットアップ手順
```

### エージェントをローカルで実行

```bash
cd your-agent
uv sync                       # 依存関係をインストール
uv run python -m your_agent.main  # エージェントサーバーを起動
```

**それだけです！** エージェントは`http://localhost:8030`で稼働し、A2A、AP2、X402プロトコルを使用して他のエージェントと通信する準備が整いました。

<br/>


## なぜこれが重要なのか

**問題**：エージェントを構築するのは簡単です。それらを相互に通信させる？それが難しい部分です。

**古い方法**：
```python
# エージェントロジックを書く
# APIエンドポイントを見つける
# 認証を実装する
# エラー処理を追加する
# デプロイを設定する
# A2A、AP2、X402のプロトコルアダプターを書く
# モニタリングを設定する
# ... 3日後、もしかしたら動くかも？
```

**Binduの方法**：
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
# 4つの質問に答える
# 完了。エージェントはA2A、AP2、X402を話します。
```

<br/>


## なぜこれを使うのか？

- **2分セットアップ**：簡単な質問に答えるだけで、完全な本番環境対応のエージェントシステムが手に入ります。
- **軽量**：ボイラープレートなし。設定地獄なし。
- **シンプル**：複雑なセットアップなし。設定するだけで完全にデプロイ可能なエージェントが手に入ります。
- **セキュア**：組み込みの認証、エラー追跡、モニタリング。
- **プロトコル対応**：A2A、AP2、X402の組み込みサポート — エージェントは普遍的な言語を話します
- **フレームワーク非依存**：Agno、LangChain、CrewAI、LlamaIndex、FastAgentなどで動作
- **本番環境対応**：CI/CD、テスト、Docker、ドキュメント、デプロイ設定を含みます。
- **可観測性**：Phoenix、Langfuse、Jaegerの組み込みサポート。
- **ベストプラクティス**：ruff、mypy、pytest、pre-commitフック、コード品質ツールで事前設定
- **どこでもデプロイ**：エージェントは生きたサーバーになり、エージェントのインターネットに参加する準備が整います

<br/>

## 何が得られるか

このCookiecutterテンプレートは、必要なすべてを備えた完全なBindu Agentプロジェクトを構築します：

- 依存関係管理のための[uv](https://docs.astral.sh/uv/)
- [GitHub Actions](https://github.com/features/actions)によるCI/CD
- [pre-commit](https://pre-commit.com/)によるプレコミットフック
- [ruff](https://github.com/charliermarsh/ruff)、[ty](https://docs.astral.sh/ty/)によるコード品質
- GitHubで新しいリリースを作成することによる[PyPI](https://pypi.org)への公開
- [pytest](https://docs.pytest.org/en/7.1.x/)と[codecov](https://about.codecov.io/)によるテストとカバレッジ
- [MkDocs](https://www.mkdocs.org/)によるドキュメント
- [Docker](https://www.docker.com/)または[Podman](https://podman.io/)によるコンテナ化




<br/>

## 仕組み

```bash
┌─────────────────────────────────────────────────────────────┐
│  1. cookiecutterを実行  →  2. 質問に答える  →  3. デプロイ！│
└─────────────────────────────────────────────────────────────┘
                              ↓
        エージェントが稼働し、A2A、AP2、X402で通信しています
                              ↓
              エージェントのインターネットに参加する準備完了 🌐
```

<br/>

### 舞台裏の魔法

Bindu Agentを作成すると、単なるテンプレートではなく、**生きたサーバー**が手に入ります：

- **普遍的なプロトコルを話す**：エージェント間通信のためのA2A、エージェント商取引のためのAP2、支払いレールのためのX402
- **設計によるセキュリティ**：組み込みの認証、エラー追跡、モニタリング
- **発見可能**：エージェントはウェブ上の他のエージェントによって発見され、接続されます
- **フレームワークの柔軟性**：独自のエージェントフレームワーク（Agno、LangChain、CrewAIなど）を使用
- **本番環境対応**：localhostからクラウドまで、数日ではなく数分で

<br/>

### ビジョン

```bash
夜空を覗く
}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
{{            +             +                  +   @          {{
}}   |                *           o     +                .    }}
{{  -O-    o               .               .          +       {{
}}   |                    _,.-----.,_         o    |          }}
{{           +    *    .-'.         .'-.          -O-         {{
}}      *            .'.-'   .---.   `'.'.         |     *    }}
{{ .                /_.-'   /     \   .'-.\                   {{
}}         ' -=*<  |-._.-  |   @   |   '-._|  >*=-    .     + }}
{{ -- )--           \`-.    \     /    .-'/                   {{
}}       *     +     `.'.    '---'    .'.'    +       o       }}
{{                  .  '-._         _.-'  .                   {{
}}         |               `~~~~~~~`       - --===D       @   }}
{{   o    -O-      *   .                  *        +          {{
}}         |                      +         .            +    }}
{{ jgs          .     @      o                        *       {{
}}       o                          *          o           .  }}
{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
```

各シンボルはエージェント — 知性の火花です。
そして小さな点がBindu、エージェントのインターネットの起源点です。<br/>

<br/>



## エージェントのインターネット

あなたのBindu Agentは単なる別のAPIではありません — **エージェントのインターネットの市民**です：

- **A2A（エージェント間）**：AIエージェント間のシームレスな通信
- **AP2（エージェントプロトコル2）**：エージェントの商取引とトランザクション機能
- **X402（支払いプロトコル）**：エージェントサービスの組み込み支払いレール

各プロトコルは`agent_config.json`で事前設定されています。エージェントは初日から普遍的な言語を話します。

<br/>

## もっと学ぶ

- **[Binduドキュメント](https://docs.getbindu)** - Binduの機能を深く掘り下げる
- **[Bindu GitHub](https://github.com/getbindu/Bindu)** - エージェントを動かすコアライブラリ
- **[Discordに参加](https://discord.gg/3w5zuYUuwt)** - ヘルプを得て、アイデアを共有し、コミュニティとつながる
- **[サンプルエージェント](https://github.com/getbindu/Bindu/tree/main/examples)** - Binduエージェントの実際の動作を見る

<br/>

## 未来のために構築

私たちは**エージェントスウォーム**の時代に入っています — 何千ものAIエージェントが協力し、交渉し、取引します。Binduはあなたのエージェントがこの未来に備えていることを保証します：

- **相互運用可能**：あらゆるエージェントフレームワークで動作
- **標準準拠**：A2A、AP2、X402プロトコルが組み込まれています
- **本番グレード**：おもちゃでもデモでもない — 本物のインフラストラクチャ
- **コミュニティ主導**：[getbindu](https://getbindu)でムーブメントに参加

<br/>

## 貢献

私たちは貢献を💛します！あなたが：
- 新しいエージェントフレームワークテンプレートを追加している
- ドキュメントを改善している
- バグを修正している
- Binduエージェントの作品を共有している

[貢献ガイドライン](CONTRIBUTING.md)をチェックして、[Discord](https://discord.gg/3w5zuYUuwt)で参加してください！

<br/>

## 謝辞

このプロジェクトは部分的に[cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv/tree/main)に基づいています

## スター履歴

[![Star History Chart](https://api.star-history.com/svg?repos=getbindu/create-bindu-agent&type=date&legend=top-left)](https://www.star-history.com/#getbindu/create-bindu-agent&type=date&legend=top-left)

---

<p align="center">
  <strong>アムステルダムのチームが💛で構築 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>アイデアからエージェントのインターネットまで2分で。</strong><br/>
  <em>あなたのエージェント。あなたのフレームワーク。普遍的なプロトコル。</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/create-bindu-agent">⭐ GitHubでスターをつける</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Discordに参加</a> •
  <a href="https://docs.getbindu">📚 ドキュメントを読む</a>
</p>
