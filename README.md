# MCP Servers

Este repositorio contiene configuraciones y scripts para varios servidores MCP (Model Context Protocol) que permiten integrar herramientas externas con modelos de lenguaje como Claude en Cursor.

## 📋 Contenido

- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Servidores MCP](#servidores-mcp)
- [Firecrawl MCP](#firecrawl-mcp)
- [Uso](#uso)
- [Contribuir](#contribuir)

## 🔍 Descripción

MCP (Model Context Protocol) es un estándar que permite a los modelos de lenguaje interactuar con herramientas y servicios externos. Este repositorio centraliza diversos servidores MCP para facilitar su uso en Cursor y otros clientes compatibles.

## 📁 Estructura del Proyecto

```
MCP_servers/
├── .gitignore                # Configuración de exclusiones para Git
├── markdown_docs/            # Documentos extraídos con Firecrawl
├── scripts/                  # Scripts organizados por característica
│   └── firecrawl/            # Scripts relacionados con Firecrawl
│       └── scraper.py        # Script para extracción de contenido web
└── mcp.json                  # Configuración de servidores MCP para Cursor
```

## 🖥️ Servidores MCP

Este repositorio incluye configuraciones para varios servidores MCP:

- **Firecrawl**: Extracción de contenido web y scraping
- **Browser Tools**: Herramientas para interactuar con el navegador
- **Supabase**: Acceso a bases de datos PostgreSQL
- **Git**: Operaciones con repositorios Git
- **Filesystem**: Acceso al sistema de archivos
- **N8N Workflow Creator**: Creación de flujos de trabajo
- **Sequential Thinking**: Mejora de capacidades de razonamiento
- **Perplexity**: Búsqueda de información
- **Archon**: Servidor MCP adicional

## 🔥 Firecrawl MCP

Firecrawl es una herramienta potente para extraer contenido web que se integra con Cursor a través de MCP.

### Instalación

```bash
npm install -g firecrawl-mcp
```

### Configuración en Cursor

En Cursor, dirígete a:
1. Configuración > Características > Servidores MCP
2. Agregar nuevo servidor MCP:
   - Nombre: "firecrawl"
   - Tipo: "command"
   - Comando: `firecrawl-mcp`
   - Variables de entorno: `FIRECRAWL_API_KEY=tu-api-key`

### Uso desde Python

```python
from firecrawl import FirecrawlApp

# Inicializar con tu API key
app = FirecrawlApp(api_key='tu-api-key')

# Extraer contenido de una URL
result = app.scrape_url('https://ejemplo.com')

# Guardar el resultado
with open('resultado.md', 'w') as f:
    f.write(result['markdown'])
```

## ⚙️ Uso

Para utilizar cualquiera de los servidores MCP configurados:

1. Asegúrate de que Cursor esté configurado con el archivo `mcp.json`
2. Los servidores MCP deben estar funcionando para que Cursor pueda utilizarlos
3. Para Firecrawl, asegúrate de tener una API key válida

## 👥 Contribuir

Para contribuir a este proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu característica
3. Realiza tus cambios siguiendo las guías de estilo
4. Envía un pull request

---

Desarrollado con ❤️ para potenciar la integración de herramientas con IA 