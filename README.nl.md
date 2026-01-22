<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"We stellen ons een wereld van agenten voor waar ze naadloos met elkaar kunnen communiceren.<br/>
  En Bindu verandert je agent in een levende server, het punt (Bindu) in het Internet van Agenten."</em>
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
    <img src="https://img.youtube.com/vi/obY1bGOoWG8/maxresdefault.jpg" alt="Bekijk Tutorial Video"/>
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


## Van Nul naar Productie-Klare Agent in 2 Minuten

**Create Bindu Agent** is de snelste manier om productie-klare AI-agenten te bouwen die de taal van het Internet van Agenten spreken. Geen boilerplate. Geen configuratiehel. Gewoon configureren en een volledig inzetbare agent krijgen die communiceert met **A2A**, **AP2** en **X402** protocollen.

<br/>

## Snelstart

**Tijd tot eerste agent: ~2 minuten** ⏱️

Navigeer op je lokale machine naar de directory waarin je een projectdirectory wilt maken en voer het volgende commando uit:

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

### Wat Gebeurt Er Daarna?

Je wordt gevraagd om:
- **Projectnaam** en **beschrijving**
- **Agent framework** (Agno, LangChain, CrewAI, etc.)
- **Licentietype** (MIT, Apache, BSD, GPL, ISC)
- **Auteur details**

Dan, **boem!** 💥 Je agentproject is klaar met:

```
your-agent/
├── agent_config.json          # Agentconfiguratie met A2A/AP2/X402-instellingen
├── your_agent/
│   ├── main.py               # Je agent entry point (al Bindu-fied!)
│   └── __init__.py
├── skills/                   # Template voor het toevoegen van agentvaardigheden
├── tests/                    # Vooraf geconfigureerde pytest tests
├── pyproject.toml            # Afhankelijkheden beheerd door uv
├── Dockerfile                # Klaar voor containerisatie
├── .github/workflows/        # CI/CD pipelines
└── README.md                 # Volledige setup-instructies
```

### Voer Je Agent Lokaal Uit

```bash
cd your-agent
uv sync                       # Installeer afhankelijkheden
uv run python -m your_agent.main  # Start je agentserver
```

**Dat is het!** Je agent is nu live op `http://localhost:8030` en klaar om te communiceren met andere agenten met behulp van A2A, AP2 en X402 protocollen.

<br/>


## Waarom Dit Belangrijk Is

**Het Probleem**: Agenten bouwen is makkelijk. Ze met elkaar laten praten? Dat is het moeilijke deel.

**De Oude Manier**:
```python
# Schrijf je agentlogica
# Zoek uit wat de API-endpoints zijn
# Implementeer authenticatie
# Voeg foutafhandeling toe
# Configureer deployment
# Schrijf protocoladapters voor A2A, AP2, X402
# Stel monitoring in
# ... 3 dagen later, misschien werkt het?
```

**De Bindu Manier**:
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
# Beantwoord 4 vragen
# Klaar. Je agent spreekt A2A, AP2 en X402.
```

<br/>


## Waarom Dit Gebruiken?

- **2-Minuten Setup**: Beantwoord eenvoudige vragen, krijg een compleet productie-klaar agentisch systeem.
- **Lichtgewicht**: Geen boilerplate. Geen configuratiehel.
- **Eenvoudig**: Geen complexe setup. Gewoon configureren en een volledig inzetbare agent krijgen.
- **Veilig**: Ingebouwde authenticatie, fouttracking en monitoring.
- **Protocol-Klaar**: Ingebouwde ondersteuning voor A2A, AP2 en X402 — je agent spreekt de universele taal
- **Framework Agnostisch**: Werkt met Agno, LangChain, CrewAI, LlamaIndex, FastAgent en meer
- **Productie-Klaar**: Inclusief CI/CD, testing, Docker, documentatie en deployment configs.
- **Observeerbaarheid**: Ingebouwde ondersteuning voor Phoenix, Langfuse en Jaeger.
- **Best Practices**: Vooraf geconfigureerd met ruff, mypy, pytest, pre-commit hooks en code quality tools
- **Deploy Overal**: Je agent wordt een levende server, klaar om deel te nemen aan het Internet van Agenten

<br/>

## Wat Je Krijgt

Deze Cookiecutter template bouwt een compleet Bindu Agent project met alles wat je nodig hebt:

- [uv](https://docs.astral.sh/uv/) voor afhankelijkheidsbeheer
- CI/CD met [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks met [pre-commit](https://pre-commit.com/)
- Code kwaliteit met [ruff](https://github.com/charliermarsh/ruff), [ty](https://docs.astral.sh/ty/)
- Publiceren naar [PyPI](https://pypi.org) door een nieuwe release op GitHub te maken
- Testen en coverage met [pytest](https://docs.pytest.org/en/7.1.x/) en [codecov](https://about.codecov.io/)
- Documentatie met [MkDocs](https://www.mkdocs.org/)
- Containerisatie met [Docker](https://www.docker.com/) of [Podman](https://podman.io/)




<br/>

## Hoe Het Werkt

```bash
┌─────────────────────────────────────────────────────────────┐
│  1. Voer cookiecutter uit  →  2. Beantwoord  →  3. Deploy!  │
└─────────────────────────────────────────────────────────────┘
                              ↓
        Je agent is nu live en spreekt A2A, AP2, X402
                              ↓
              Klaar om deel te nemen aan het Internet van Agenten 🌐
```

<br/>

### De Magie Achter de Schermen

Wanneer je een Bindu Agent maakt, krijg je niet alleen een template — je krijgt een **levende server** die:

- **Universele Protocollen Spreekt**: A2A voor agent-naar-agent communicatie, AP2 voor agentische handel, X402 voor betalingsrails
- **Veilig door Ontwerp**: Ingebouwde authenticatie, fouttracking en monitoring
- **Vindbaar**: Je agent kan worden gevonden en verbonden door andere agenten over het web
- **Framework Flexibel**: Breng je eigen agent framework mee (Agno, LangChain, CrewAI, etc.)
- **Productie-Klaar**: Van localhost naar cloud in minuten, niet dagen

<br/>

### De Visie

```bash
een blik in de nachtelijke hemel
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

Elk symbool is een agent — een vonk van intelligentie.
En het kleine puntje is Bindu, het oorsprongspunt in het Internet van Agenten.<br/>

<br/>



## Het Internet van Agenten

Je Bindu Agent is niet zomaar een andere API — het is een **burger van het Internet van Agenten**:

- **A2A (Agent-naar-Agent)**: Naadloze communicatie tussen AI-agenten
- **AP2 (Agentisch Protocol 2)**: Handel en transactiemogelijkheden voor agenten
- **X402 (Betalingsprotocol)**: Ingebouwde betalingsrails voor agentdiensten

Elk protocol is vooraf geconfigureerd in je `agent_config.json`. Je agent spreekt vanaf dag één de universele taal.

<br/>

## Meer Leren

- **[Bindu Documentatie](https://docs.getbindu)** - Duik diep in de mogelijkheden van Bindu
- **[Bindu GitHub](https://github.com/getbindu/Bindu)** - De kernbibliotheek die je agent aandrijft
- **[Word Lid van Discord](https://discord.gg/3w5zuYUuwt)** - Krijg hulp, deel ideeën en maak contact met de community
- **[Voorbeeld Agenten](https://github.com/getbindu/Bindu/tree/main/examples)** - Zie Bindu agenten in actie

<br/>

## Gebouwd voor de Toekomst

We betreden het tijdperk van **agent swarms** — waar duizenden AI-agenten samenwerken, onderhandelen en transacties uitvoeren. Bindu zorgt ervoor dat je agent klaar is voor deze toekomst:

- **Interoperabel**: Werkt met elk agent framework
- **Standaard-Conform**: A2A, AP2, X402 protocollen ingebouwd
- **Productie-Grade**: Geen speelgoed, geen demo — echte infrastructuur
- **Community-Gedreven**: Sluit je aan bij de beweging op [getbindu](https://getbindu)

<br/>

## Bijdragen

We 💛 bijdragen! Of je nu:
- Nieuwe agent framework templates toevoegt
- Documentatie verbetert
- Bugs fixt
- Je Bindu agent creaties deelt

Bekijk onze [Bijdrage Richtlijnen](CONTRIBUTING.md) en sluit je bij ons aan op [Discord](https://discord.gg/3w5zuYUuwt)!

<br/>

## Erkenningen

Dit project is gedeeltelijk gebaseerd op [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv/tree/main)

## Star Geschiedenis

[![Star History Chart](https://api.star-history.com/svg?repos=getbindu/create-bindu-agent&type=date&legend=top-left)](https://www.star-history.com/#getbindu/create-bindu-agent&type=date&legend=top-left)

---

<p align="center">
  <strong>Gebouwd met 💛 door het team uit Amsterdam 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>Van idee naar Internet van Agenten in 2 minuten.</strong><br/>
  <em>Jouw agent. Jouw framework. Universele protocollen.</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/create-bindu-agent">⭐ Geef ons een ster op GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Word Lid van Discord</a> •
  <a href="https://docs.getbindu">📚 Lees de Docs</a>
</p>
