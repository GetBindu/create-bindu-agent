<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"Nous imaginons un monde d'agents où ils peuvent communiquer entre eux de manière transparente.<br/>
  Et Bindu transforme votre agent en serveur vivant, le point (Bindu) dans l'Internet des Agents."</em>
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
    <img src="https://img.youtube.com/vi/obY1bGOoWG8/maxresdefault.jpg" alt="Regarder la Vidéo Tutoriel"/>
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


## De Zéro à Agent Prêt pour la Production en 2 Minutes

**Create Bindu Agent** est le moyen le plus rapide de créer des agents IA prêts pour la production qui parlent le langage de l'Internet des Agents. Pas de code passe-partout. Pas d'enfer de configuration. Configurez simplement et obtenez un agent entièrement déployable qui communique en utilisant les protocoles **A2A**, **AP2** et **X402**.

<br/>

## Démarrage Rapide

**Temps jusqu'au premier agent : ~2 minutes** ⏱️

Sur votre machine locale, naviguez vers le répertoire dans lequel vous souhaitez créer un répertoire de projet et exécutez la commande suivante :

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

### Que Se Passe-t-il Ensuite ?

Vous serez invité à fournir :
- **Nom du projet** et **description**
- **Framework d'agent** (Agno, LangChain, CrewAI, etc.)
- **Type de licence** (MIT, Apache, BSD, GPL, ISC)
- **Détails de l'auteur**

Ensuite, **boum !** 💥 Votre projet d'agent est prêt avec :

```
your-agent/
├── agent_config.json          # Configuration de l'agent avec paramètres A2A/AP2/X402
├── your_agent/
│   ├── main.py               # Point d'entrée de votre agent (déjà Bindu-fié !)
│   └── __init__.py
├── skills/                   # Modèle pour ajouter des compétences d'agent
├── tests/                    # Tests pytest préconfigurés
├── pyproject.toml            # Dépendances gérées par uv
├── Dockerfile                # Prêt pour la conteneurisation
├── .github/workflows/        # Pipelines CI/CD
└── README.md                 # Instructions de configuration complètes
```

### Exécutez Votre Agent Localement

```bash
cd your-agent
uv sync                       # Installer les dépendances
uv run python -m your_agent.main  # Démarrer le serveur de l'agent
```

**C'est tout !** Votre agent est maintenant en ligne sur `http://localhost:8030` et prêt à communiquer avec d'autres agents en utilisant les protocoles A2A, AP2 et X402.

<br/>


## Pourquoi C'est Important

**Le Problème** : Construire des agents est facile. Les faire communiquer entre eux ? C'est la partie difficile.

**L'Ancienne Méthode** :
```python
# Écrivez la logique de votre agent
# Déterminez les points de terminaison de l'API
# Implémentez l'authentification
# Ajoutez la gestion des erreurs
# Configurez le déploiement
# Écrivez des adaptateurs de protocole pour A2A, AP2, X402
# Configurez la surveillance
# ... 3 jours plus tard, peut-être que ça marche ?
```

**La Méthode Bindu** :
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
# Répondez à 4 questions
# Terminé. Votre agent parle A2A, AP2 et X402.
```

<br/>


## Pourquoi Utiliser Ceci ?

- **Configuration en 2 Minutes** : Répondez à des questions simples, obtenez un système agentique complet prêt pour la production.
- **Léger** : Pas de code passe-partout. Pas d'enfer de configuration.
- **Simple** : Pas de configuration complexe. Configurez simplement et obtenez un agent entièrement déployable.
- **Sécurisé** : Authentification intégrée, suivi des erreurs et surveillance.
- **Prêt pour les Protocoles** : Support intégré pour A2A, AP2 et X402 — votre agent parle le langage universel
- **Agnostique du Framework** : Fonctionne avec Agno, LangChain, CrewAI, LlamaIndex, FastAgent et plus
- **Prêt pour la Production** : Inclut CI/CD, tests, Docker, documentation et configurations de déploiement.
- **Observabilité** : Support intégré pour Phoenix, Langfuse et Jaeger.
- **Meilleures Pratiques** : Préconfiguré avec ruff, mypy, pytest, hooks de pré-commit et outils de qualité de code
- **Déployez N'importe Où** : Votre agent devient un serveur vivant, prêt à rejoindre l'Internet des Agents

<br/>

## Ce Que Vous Obtenez

Ce modèle Cookiecutter construit un projet Bindu Agent complet avec tout ce dont vous avez besoin :

- [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances
- CI/CD avec [GitHub Actions](https://github.com/features/actions)
- Hooks de pré-commit avec [pre-commit](https://pre-commit.com/)
- Qualité du code avec [ruff](https://github.com/charliermarsh/ruff), [ty](https://docs.astral.sh/ty/)
- Publication sur [PyPI](https://pypi.org) en créant une nouvelle version sur GitHub
- Tests et couverture avec [pytest](https://docs.pytest.org/en/7.1.x/) et [codecov](https://about.codecov.io/)
- Documentation avec [MkDocs](https://www.mkdocs.org/)
- Conteneurisation avec [Docker](https://www.docker.com/) ou [Podman](https://podman.io/)




<br/>

## Comment Ça Marche

```bash
┌─────────────────────────────────────────────────────────────┐
│  1. Exécutez cookiecutter  →  2. Répondez  →  3. Déployez ! │
└─────────────────────────────────────────────────────────────┘
                              ↓
        Votre agent est maintenant en ligne et parle A2A, AP2, X402
                              ↓
              Prêt à rejoindre l'Internet des Agents 🌐
```

<br/>

### La Magie En Coulisses

Lorsque vous créez un Bindu Agent, vous n'obtenez pas seulement un modèle — vous obtenez un **serveur vivant** qui :

- **Parle les Protocoles Universels** : A2A pour la communication agent-à-agent, AP2 pour le commerce agentique, X402 pour les rails de paiement
- **Sécurisé par Conception** : Authentification intégrée, suivi des erreurs et surveillance
- **Découvrable** : Votre agent peut être trouvé et connecté par d'autres agents sur le web
- **Flexible en Framework** : Apportez votre propre framework d'agent (Agno, LangChain, CrewAI, etc.)
- **Prêt pour la Production** : De localhost au cloud en minutes, pas en jours

<br/>

### La Vision

```bash
un aperçu du ciel nocturne
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

Chaque symbole est un agent — une étincelle d'intelligence.
Et le petit point est Bindu, le point d'origine dans l'Internet des Agents.<br/>

<br/>



## L'Internet des Agents

Votre Bindu Agent n'est pas juste une autre API — c'est un **citoyen de l'Internet des Agents** :

- **A2A (Agent-à-Agent)** : Communication transparente entre agents IA
- **AP2 (Protocole Agentique 2)** : Capacités de commerce et de transaction pour les agents
- **X402 (Protocole de Paiement)** : Rails de paiement intégrés pour les services d'agents

Chaque protocole est préconfiguré dans votre `agent_config.json`. Votre agent parle le langage universel dès le premier jour.

<br/>

## En Savoir Plus

- **[Documentation Bindu](https://docs.getbindu)** - Plongez dans les capacités de Bindu
- **[Bindu GitHub](https://github.com/getbindu/Bindu)** - La bibliothèque centrale qui alimente votre agent
- **[Rejoignez Discord](https://discord.gg/3w5zuYUuwt)** - Obtenez de l'aide, partagez des idées et connectez-vous avec la communauté
- **[Exemples d'Agents](https://github.com/getbindu/Bindu/tree/main/examples)** - Voyez les agents Bindu en action

<br/>

## Construit pour l'Avenir

Nous entrons dans l'ère des **essaims d'agents** — où des milliers d'agents IA collaborent, négocient et effectuent des transactions. Bindu garantit que votre agent est prêt pour cet avenir :

- **Interopérable** : Fonctionne avec n'importe quel framework d'agents
- **Conforme aux Normes** : Protocoles A2A, AP2, X402 intégrés
- **Qualité Production** : Pas un jouet, pas une démo — une vraie infrastructure
- **Piloté par la Communauté** : Rejoignez le mouvement sur [getbindu](https://getbindu)

<br/>

## Contribuer

Nous 💛 les contributions ! Que vous soyez :
- En train d'ajouter de nouveaux modèles de framework d'agents
- En train d'améliorer la documentation
- En train de corriger des bugs
- En train de partager vos créations d'agents Bindu

Consultez nos [Directives de Contribution](CONTRIBUTING.md) et rejoignez-nous sur [Discord](https://discord.gg/3w5zuYUuwt) !

<br/>

## Remerciements

Ce projet est partiellement basé sur [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv/tree/main)

## Historique des Étoiles

[![Star History Chart](https://api.star-history.com/svg?repos=getbindu/create-bindu-agent&type=date&legend=top-left)](https://www.star-history.com/#getbindu/create-bindu-agent&type=date&legend=top-left)

---

<p align="center">
  <strong>Construit avec 💛 par l'équipe d'Amsterdam 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>De l'idée à l'Internet des Agents en 2 minutes.</strong><br/>
  <em>Votre agent. Votre framework. Protocoles universels.</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/create-bindu-agent">⭐ Donnez-nous une étoile sur GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Rejoignez Discord</a> •
  <a href="https://docs.getbindu">📚 Lisez la Documentation</a>
</p>
