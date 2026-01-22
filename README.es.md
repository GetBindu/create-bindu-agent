<p align="center">
  <img src="assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> Create Bindu Agent 🌻</h1>

<p align="center">
  <em>"Imaginamos un mundo de agentes donde puedan comunicarse entre sí sin problemas.<br/>
  Y Bindu convierte tu agente en un servidor vivo, el punto (Bindu) en el Internet de Agentes."</em>
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
    <img src="https://img.youtube.com/vi/obY1bGOoWG8/maxresdefault.jpg" alt="Ver Video Tutorial"/>
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


## De Cero a Agente Listo para Producción en 2 Minutos

**Create Bindu Agent** es la forma más rápida de construir agentes de IA listos para producción que hablan el lenguaje del Internet de Agentes. Sin código repetitivo. Sin infierno de configuración. Solo configura y obtén un agente completamente desplegable que se comunica usando los protocolos **A2A**, **AP2** y **X402**.

<br/>

## Inicio Rápido

**Tiempo hasta el primer agente: ~2 minutos** ⏱️

En tu máquina local, navega al directorio donde deseas crear un directorio de proyecto y ejecuta el siguiente comando:

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

### ¿Qué Sucede Después?

Se te pedirá:
- **Nombre del proyecto** y **descripción**
- **Framework del agente** (Agno, LangChain, CrewAI, etc.)
- **Tipo de licencia** (MIT, Apache, BSD, GPL, ISC)
- **Detalles del autor**

Luego, **¡boom!** 💥 Tu proyecto de agente está listo con:

```
your-agent/
├── agent_config.json          # Configuración del agente con ajustes A2A/AP2/X402
├── your_agent/
│   ├── main.py               # Punto de entrada de tu agente (¡ya Bindu-ficado!)
│   └── __init__.py
├── skills/                   # Plantilla para agregar habilidades del agente
├── tests/                    # Pruebas pytest preconfiguradas
├── pyproject.toml            # Dependencias gestionadas por uv
├── Dockerfile                # Listo para contenedorización
├── .github/workflows/        # Pipelines CI/CD
└── README.md                 # Instrucciones completas de configuración
```

### Ejecuta Tu Agente Localmente

```bash
cd your-agent
uv sync                       # Instalar dependencias
uv run python -m your_agent.main  # Iniciar servidor del agente
```

**¡Eso es todo!** Tu agente ahora está en vivo en `http://localhost:8030` y listo para comunicarse con otros agentes usando los protocolos A2A, AP2 y X402.

<br/>


## Por Qué Esto Importa

**El Problema**: Construir agentes es fácil. ¿Hacer que hablen entre sí? Esa es la parte difícil.

**La Forma Antigua**:
```python
# Escribe la lógica de tu agente
# Descubre los endpoints de la API
# Implementa autenticación
# Agrega manejo de errores
# Configura el despliegue
# Escribe adaptadores de protocolo para A2A, AP2, X402
# Configura monitoreo
# ... 3 días después, ¿tal vez funciona?
```

**La Forma Bindu**:
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
# Responde 4 preguntas
# Listo. Tu agente habla A2A, AP2 y X402.
```

<br/>


## ¿Por Qué Usar Esto?

- **Configuración de 2 Minutos**: Responde preguntas simples, obtén un sistema agéntico completo listo para producción.
- **Ligero**: Sin código repetitivo. Sin infierno de configuración.
- **Simple**: Sin configuración compleja. Solo configura y obtén un agente completamente desplegable.
- **Seguro**: Autenticación integrada, seguimiento de errores y monitoreo.
- **Listo para Protocolos**: Soporte integrado para A2A, AP2 y X402 — tu agente habla el lenguaje universal
- **Agnóstico de Framework**: Funciona con Agno, LangChain, CrewAI, LlamaIndex, FastAgent y más
- **Listo para Producción**: Incluye CI/CD, pruebas, Docker, documentación y configuraciones de despliegue.
- **Observabilidad**: Soporte integrado para Phoenix, Langfuse y Jaeger.
- **Mejores Prácticas**: Preconfigurado con ruff, mypy, pytest, hooks de pre-commit y herramientas de calidad de código
- **Despliega en Cualquier Lugar**: Tu agente se convierte en un servidor vivo, listo para unirse al Internet de Agentes

<br/>

## Lo Que Obtienes

Esta plantilla Cookiecutter construye un proyecto completo de Bindu Agent con todo lo que necesitas:

- [uv](https://docs.astral.sh/uv/) para gestión de dependencias
- CI/CD con [GitHub Actions](https://github.com/features/actions)
- Hooks de pre-commit con [pre-commit](https://pre-commit.com/)
- Calidad de código con [ruff](https://github.com/charliermarsh/ruff), [ty](https://docs.astral.sh/ty/)
- Publicación en [PyPI](https://pypi.org) creando un nuevo lanzamiento en GitHub
- Pruebas y cobertura con [pytest](https://docs.pytest.org/en/7.1.x/) y [codecov](https://about.codecov.io/)
- Documentación con [MkDocs](https://www.mkdocs.org/)
- Contenedorización con [Docker](https://www.docker.com/) o [Podman](https://podman.io/)




<br/>

## Cómo Funciona

```bash
┌─────────────────────────────────────────────────────────────┐
│  1. Ejecuta cookiecutter  →  2. Responde  →  3. ¡Despliega! │
└─────────────────────────────────────────────────────────────┘
                              ↓
        Tu agente ahora está en vivo y hablando A2A, AP2, X402
                              ↓
              Listo para unirse al Internet de Agentes 🌐
```

<br/>

### La Magia Detrás de Escena

Cuando creas un Bindu Agent, no solo obtienes una plantilla — obtienes un **servidor vivo** que:

- **Habla Protocolos Universales**: A2A para comunicación agente-a-agente, AP2 para comercio agéntico, X402 para rieles de pago
- **Seguro por Diseño**: Autenticación integrada, seguimiento de errores y monitoreo
- **Descubrible**: Tu agente puede ser encontrado y conectado por otros agentes en la web
- **Flexible en Framework**: Trae tu propio framework de agente (Agno, LangChain, CrewAI, etc.)
- **Listo para Producción**: De localhost a la nube en minutos, no días

<br/>

### La Visión

```bash
un vistazo al cielo nocturno
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

Cada símbolo es un agente — una chispa de inteligencia.
Y el pequeño punto es Bindu, el punto de origen en el Internet de Agentes.<br/>

<br/>



## El Internet de Agentes

Tu Bindu Agent no es solo otra API — es un **ciudadano del Internet de Agentes**:

- **A2A (Agente-a-Agente)**: Comunicación sin problemas entre agentes de IA
- **AP2 (Protocolo Agéntico 2)**: Capacidades de comercio y transacción para agentes
- **X402 (Protocolo de Pago)**: Rieles de pago integrados para servicios de agentes

Cada protocolo está preconfigurado en tu `agent_config.json`. Tu agente habla el lenguaje universal desde el primer día.

<br/>

## Aprende Más

- **[Documentación de Bindu](https://docs.getbindu)** - Profundiza en las capacidades de Bindu
- **[Bindu GitHub](https://github.com/getbindu/Bindu)** - La biblioteca central que impulsa tu agente
- **[Únete a Discord](https://discord.gg/3w5zuYUuwt)** - Obtén ayuda, comparte ideas y conéctate con la comunidad
- **[Agentes de Ejemplo](https://github.com/getbindu/Bindu/tree/main/examples)** - Ve agentes Bindu en acción

<br/>

## Construido para el Futuro

Estamos entrando en la era de los **enjambres de agentes** — donde miles de agentes de IA colaboran, negocian y realizan transacciones. Bindu asegura que tu agente esté listo para este futuro:

- **Interoperable**: Funciona con cualquier framework de agentes
- **Conforme a Estándares**: Protocolos A2A, AP2, X402 integrados
- **Grado de Producción**: No es un juguete, no es una demo — infraestructura real
- **Impulsado por la Comunidad**: Únete al movimiento en [getbindu](https://getbindu)

<br/>

## Contribuir

¡Nos encantan 💛 las contribuciones! Ya sea que estés:
- Agregando nuevas plantillas de framework de agentes
- Mejorando la documentación
- Corrigiendo errores
- Compartiendo tus creaciones de agentes Bindu

¡Consulta nuestras [Pautas de Contribución](CONTRIBUTING.md) y únete a nosotros en [Discord](https://discord.gg/3w5zuYUuwt)!

<br/>

## Agradecimientos

Este proyecto se basa parcialmente en [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv/tree/main)

## Historial de Estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=getbindu/create-bindu-agent&type=date&legend=top-left)](https://www.star-history.com/#getbindu/create-bindu-agent&type=date&legend=top-left)

---

<p align="center">
  <strong>Construido con 💛 por el equipo de Ámsterdam 🌷</strong><br/>
  <em>¡Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>De la idea al Internet de Agentes en 2 minutos.</strong><br/>
  <em>Tu agente. Tu framework. Protocolos universales.</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/create-bindu-agent">⭐ Danos una estrella en GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Únete a Discord</a> •
  <a href="https://docs.getbindu">📚 Lee la Documentación</a>
</p>
