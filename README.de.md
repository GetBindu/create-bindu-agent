<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"Wir stellen uns eine Welt von Agenten vor, in der sie nahtlos miteinander kommunizieren können.<br/>
  Und Bindu verwandelt Ihren Agenten in einen lebenden Server, den Punkt (Bindu) im Internet der Agenten."</em>
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
    <img src="https://img.youtube.com/vi/obY1bGOoWG8/maxresdefault.jpg" alt="Tutorial-Video ansehen"/>
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


## Von Null zu produktionsbereitem Agenten in 2 Minuten

**Create Bindu Agent** ist der schnellste Weg, produktionsbereite KI-Agenten zu erstellen, die die Sprache des Internets der Agenten sprechen. Kein Boilerplate. Keine Konfigurationshölle. Einfach konfigurieren und einen vollständig bereitstellbaren Agenten erhalten, der über die Protokolle **A2A**, **AP2** und **X402** kommuniziert.

<br/>

## Schnellstart

**Zeit bis zum ersten Agenten: ~2 Minuten** ⏱️

Navigieren Sie auf Ihrem lokalen Rechner zu dem Verzeichnis, in dem Sie ein Projektverzeichnis erstellen möchten, und führen Sie den folgenden Befehl aus:

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

### Was passiert als Nächstes?

Sie werden aufgefordert:
- **Projektname** und **Beschreibung**
- **Agenten-Framework** (Agno, LangChain, CrewAI, usw.)
- **Lizenztyp** (MIT, Apache, BSD, GPL, ISC)
- **Autorendetails**

Dann, **boom!** 💥 Ihr Agentenprojekt ist bereit mit:

```
your-agent/
├── agent_config.json          # Agentenkonfiguration mit A2A/AP2/X402-Einstellungen
├── your_agent/
│   ├── main.py               # Ihr Agenten-Einstiegspunkt (bereits Bindu-fiziert!)
│   └── __init__.py
├── skills/                   # Vorlage zum Hinzufügen von Agentenfähigkeiten
├── tests/                    # Vorkonfigurierte pytest-Tests
├── pyproject.toml            # Von uv verwaltete Abhängigkeiten
├── Dockerfile                # Bereit für Containerisierung
├── .github/workflows/        # CI/CD-Pipelines
└── README.md                 # Vollständige Einrichtungsanweisungen
```

### Führen Sie Ihren Agenten lokal aus

```bash
cd your-agent
uv sync                       # Abhängigkeiten installieren
uv run python -m your_agent.main  # Agentenserver starten
```

**Das war's!** Ihr Agent ist jetzt unter `http://localhost:8030` live und bereit, mit anderen Agenten über die Protokolle A2A, AP2 und X402 zu kommunizieren.

<br/>


## Warum das wichtig ist

**Das Problem**: Agenten zu bauen ist einfach. Sie miteinander sprechen zu lassen? Das ist der schwierige Teil.

**Der alte Weg**:
```python
# Schreiben Sie Ihre Agentenlogik
# Finden Sie API-Endpunkte heraus
# Implementieren Sie Authentifizierung
# Fügen Sie Fehlerbehandlung hinzu
# Konfigurieren Sie die Bereitstellung
# Schreiben Sie Protokolladapter für A2A, AP2, X402
# Richten Sie Monitoring ein
# ... 3 Tage später, vielleicht funktioniert es?
```

**Der Bindu-Weg**:
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
# Beantworten Sie 4 Fragen
# Fertig. Ihr Agent spricht A2A, AP2 und X402.
```

<br/>


## Warum dies verwenden?

- **2-Minuten-Setup**: Beantworten Sie einfache Fragen, erhalten Sie ein vollständiges produktionsbereites agentisches System.
- **Leichtgewichtig**: Kein Boilerplate. Keine Konfigurationshölle.
- **Einfach**: Keine komplexe Einrichtung. Einfach konfigurieren und einen vollständig bereitstellbaren Agenten erhalten.
- **Sicher**: Integrierte Authentifizierung, Fehlerverfolgung und Monitoring.
- **Protokollbereit**: Integrierte Unterstützung für A2A, AP2 und X402 — Ihr Agent spricht die universelle Sprache
- **Framework-agnostisch**: Funktioniert mit Agno, LangChain, CrewAI, LlamaIndex, FastAgent und mehr
- **Produktionsbereit**: Enthält CI/CD, Tests, Docker, Dokumentation und Bereitstellungskonfigurationen.
- **Beobachtbarkeit**: Integrierte Unterstützung für Phoenix, Langfuse und Jaeger.
- **Best Practices**: Vorkonfiguriert mit ruff, mypy, pytest, Pre-Commit-Hooks und Code-Qualitätswerkzeugen
- **Überall bereitstellen**: Ihr Agent wird zu einem lebenden Server, bereit, dem Internet der Agenten beizutreten

<br/>

## Was Sie bekommen

Diese Cookiecutter-Vorlage erstellt ein vollständiges Bindu-Agent-Projekt mit allem, was Sie brauchen:

- [uv](https://docs.astral.sh/uv/) für Abhängigkeitsverwaltung
- CI/CD mit [GitHub Actions](https://github.com/features/actions)
- Pre-Commit-Hooks mit [pre-commit](https://pre-commit.com/)
- Code-Qualität mit [ruff](https://github.com/charliermarsh/ruff), [ty](https://docs.astral.sh/ty/)
- Veröffentlichung auf [PyPI](https://pypi.org) durch Erstellen eines neuen Releases auf GitHub
- Tests und Coverage mit [pytest](https://docs.pytest.org/en/7.1.x/) und [codecov](https://about.codecov.io/)
- Dokumentation mit [MkDocs](https://www.mkdocs.org/)
- Containerisierung mit [Docker](https://www.docker.com/) oder [Podman](https://podman.io/)




<br/>

## Wie es funktioniert

```bash
┌─────────────────────────────────────────────────────────────┐
│  1. Cookiecutter ausführen  →  2. Antworten  →  3. Bereitstellen!   │
└─────────────────────────────────────────────────────────────┘
                              ↓
        Ihr Agent ist jetzt live und spricht A2A, AP2, X402
                              ↓
              Bereit, dem Internet der Agenten beizutreten 🌐
```

<br/>

### Die Magie hinter den Kulissen

Wenn Sie einen Bindu-Agenten erstellen, erhalten Sie nicht nur eine Vorlage — Sie erhalten einen **lebenden Server**, der:

- **Universelle Protokolle spricht**: A2A für Agent-zu-Agent-Kommunikation, AP2 für agentischen Handel, X402 für Zahlungsschienen
- **Sicher durch Design**: Integrierte Authentifizierung, Fehlerverfolgung und Monitoring
- **Auffindbar**: Ihr Agent kann von anderen Agenten im Web gefunden und verbunden werden
- **Framework-flexibel**: Bringen Sie Ihr eigenes Agenten-Framework mit (Agno, LangChain, CrewAI, usw.)
- **Produktionsbereit**: Von localhost zur Cloud in Minuten, nicht Tagen

<br/>

### Die Vision

```bash
ein Blick in den Nachthimmel
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

Jedes Symbol ist ein Agent — ein Funke der Intelligenz.
Und der kleine Punkt ist Bindu, der Ursprungspunkt im Internet der Agenten.<br/>

<br/>



## Das Internet der Agenten

Ihr Bindu-Agent ist nicht nur eine weitere API — er ist ein **Bürger des Internets der Agenten**:

- **A2A (Agent-zu-Agent)**: Nahtlose Kommunikation zwischen KI-Agenten
- **AP2 (Agentisches Protokoll 2)**: Handels- und Transaktionsfähigkeiten für Agenten
- **X402 (Zahlungsprotokoll)**: Integrierte Zahlungsschienen für Agentendienste

Jedes Protokoll ist in Ihrer `agent_config.json` vorkonfiguriert. Ihr Agent spricht vom ersten Tag an die universelle Sprache.

<br/>

## Mehr erfahren

- **[Bindu-Dokumentation](https://docs.getbindu)** - Tauchen Sie tief in die Fähigkeiten von Bindu ein
- **[Bindu GitHub](https://github.com/getbindu/Bindu)** - Die Kernbibliothek, die Ihren Agenten antreibt
- **[Discord beitreten](https://discord.gg/3w5zuYUuwt)** - Hilfe erhalten, Ideen teilen und mit der Community verbinden
- **[Beispiel-Agenten](https://github.com/getbindu/Bindu/tree/main/examples)** - Sehen Sie Bindu-Agenten in Aktion

<br/>

## Für die Zukunft gebaut

Wir treten in das Zeitalter der **Agentenschwärme** ein — wo Tausende von KI-Agenten zusammenarbeiten, verhandeln und Transaktionen durchführen. Bindu stellt sicher, dass Ihr Agent für diese Zukunft bereit ist:

- **Interoperabel**: Funktioniert mit jedem Agenten-Framework
- **Standardkonform**: A2A-, AP2-, X402-Protokolle integriert
- **Produktionsreif**: Kein Spielzeug, keine Demo — echte Infrastruktur
- **Community-getrieben**: Treten Sie der Bewegung bei [getbindu](https://getbindu) bei

<br/>

## Mitwirken

Wir 💛 Beiträge! Egal ob Sie:
- Neue Agenten-Framework-Vorlagen hinzufügen
- Dokumentation verbessern
- Fehler beheben
- Ihre Bindu-Agenten-Kreationen teilen

Schauen Sie sich unsere [Beitragsrichtlinien](CONTRIBUTING.md) an und treten Sie uns auf [Discord](https://discord.gg/3w5zuYUuwt) bei!

<br/>

## Danksagungen

Dieses Projekt basiert teilweise auf [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv/tree/main)

## Star-Verlauf

[![Star History Chart](https://api.star-history.com/svg?repos=getbindu/create-bindu-agent&type=date&legend=top-left)](https://www.star-history.com/#getbindu/create-bindu-agent&type=date&legend=top-left)

---

<p align="center">
  <strong>Mit 💛 vom Team aus Amsterdam gebaut 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>Von der Idee zum Internet der Agenten in 2 Minuten.</strong><br/>
  <em>Ihr Agent. Ihr Framework. Universelle Protokolle.</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/create-bindu-agent">⭐ Geben Sie uns einen Stern auf GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Discord beitreten</a> •
  <a href="https://docs.getbindu">📚 Dokumentation lesen</a>
</p>
