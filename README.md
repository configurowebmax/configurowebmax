<div align="center">
  <h1>¡Hola! Soy Mauricio Sevilla 👋</h1>
  <h3>Ingeniero de TI | Especialista en Web Scraping | Creador de ConfiguroWeb</h3>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F7DF1E&center=true&vCenter=true&width=435&lines=Democratizando+el+software...;%2B300+Aplicaciones+Desarrolladas;Python+%7C+JS+%7C+PHP+%7C+Node.js" alt="Typing SVG" />
</div>

---

### 🚀 Sobre este repositorio

Este es mi **portafolio personal** (`Mauricio Sevilla Britto`), un sitio estático construido con **HTML5 + Bootstrap 5**. Además de servir como carta de presentación, lo uso como **laboratorio práctico de DevSecOps**: incluye un flujo de **GitHub Actions** que despliega automáticamente el sitio en **GitHub Pages** y envía una **notificación a Slack**, todo gestionado de forma **segura** mediante *Secrets*.

> 🎯 **Mi Estrategia 2026:** Tras un reinicio forzado, estoy reconstruyendo mi ecosistema digital. Mi enfoque actual es la **colaboración Open Source** y la creación de herramientas de automatización.

---

### 💻 Stack Tecnológico

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" height="40" alt="php logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" height="40" alt="nodejs logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="40" alt="mysql logo"  />
</div>

---

### 🤖 Automatización Segura (DevSecOps)

Este repositorio implementa un pipeline CI/CD seguro. **Ninguna credencial se almacena en el código.**

| Archivo | Descripción |
|---|---|
| `.github/workflows/deploy-and-notify.yml` | Despliega en GitHub Pages + notifica a Slack. Usa `${{ secrets.* }}` inyectados en `env:`. |
| `.github/scripts/notify_slack.py` | Script Python (solo librería estándar) que lee credenciales de `os.environ`, sin dependencias externas. |
| `SECURITY_SETUP.md` | Guía de configuración de Secrets + recordatorio educativo de seguridad. |

#### 🔧 Configuración rápida del Secret

1. Crea un *Incoming Webhook* en Slack y copia la URL.
2. En GitHub: `Settings → Secrets and variables → Actions → New repository secret`.
   - **Name:** `SLACK_WEBHOOK_URL`
   - **Value:** (pega aquí la URL del webhook).

> 🛡️ **Por qué nunca subir credenciales a Git:** aunque borres el archivo, el secreto queda **permanente en el historial**. Los bots escanean GitHub en busca de claves reales en segundos, y un token filtrado puede permitir acceso automatizado a tu infraestructura. Usa siempre *Repository Secrets*, tokens con *scopes* mínimos, habilita *secret scanning* + *push protection*, y rota las credenciales periódicamente.

---

### 📁 Estructura del proyecto

```
mauricio-sevilla-britto/
├── index.html                      # Portafolio (HTML + Bootstrap)
├── .github/
│   ├── workflows/
│   │   └── deploy-and-notify.yml   # Pipeline CI/CD seguro
│   └── scripts/
│       └── notify_slack.py         # Notificación a Slack (lee creds del entorno)
├── SECURITY_SETUP.md               # Guía de configuración de secrets
└── README.md
```

---

### ▶️ Cómo usarlo

1. Haz `push` a la rama `main` (o ejecuta el workflow manualmente desde la pestaña *Actions*).
2. El sitio se publicará en GitHub Pages.
3. Recibirás una notificación en el canal de Slack configurado.

---

### 📈 Estadísticas de GitHub

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=configurowebmax&show_icons=true&theme=radical&hide_border=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=configurowebmax&layout=compact&theme=radical&hide_border=true" alt="Lenguajes más usados" />
</div>

---

### 🌐 Conéctate conmigo

<div align="center">
  <a href="https://www.configuroweb.com">
    <img src="https://img.shields.io/badge/Website-3b5998?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website" />
  </a>
  <a href="https://www.youtube.com/@yoconfiguroweb">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" />
  </a>
  <a href="https://www.linkedin.com/in/mauricio-sevilla/?locale=en">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
</div>

<br>

<div align="center">
  <em><b>"El código es arte cuando resuelve un problema real."</b></em>
</div>