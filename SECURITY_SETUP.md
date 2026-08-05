# Configuración Segura del Flujo de Automatización (DevSecOps)

Este proyecto incluye un flujo de GitHub Actions (`.github/workflows/deploy-and-notify.yml`)
que despliega el portafolio en **GitHub Pages** y envía una **notificación a Slack**.
Ninguna credencial se almacena en el código; todo se gestiona mediante **GitHub Secrets**.

---

## 🔧 Cómo configurar el Secret de Slack (paso a paso)

1. Crea un **Incoming Webhook** en tu workspace de Slack:
   - Ve a `Slack -> Administrar apps -> Crear nueva app` o usa la app oficial
     **Incoming Webhooks**.
   - Selecciona el canal donde quieres recibir las notificaciones.
   - Copia la **Webhook URL** (tiene esta forma, es solo un ejemplo y NO es válida):
     `https://hooks.slack.com/services/YOUR_WORKSPACE/YOUR_CHANNEL/YOUR_SECRET_TOKEN`
2. En tu repositorio de GitHub:
   - `Settings` → `Secrets and variables` → `Actions` → `New repository secret`.
   - **Name:** `SLACK_WEBHOOK_URL`
   - **Value:** pega aquí la Webhook URL que copiaste en el paso 1.
   - Guarda. GitHub cifra el valor y nunca lo muestra de nuevo en texto plano.

> ✅ No necesitas crear el `GITHUB_TOKEN`; GitHub lo inyecta automáticamente
> en cada ejecución del workflow.

---

## 🛡️ ¿Por qué NUNCA subir credenciales al control de versiones?

Subir tokens, contraseñas o claves privadas a Git (incluso a repos "privados")
es uno de los errores más peligrosos y comunes. Razones:

| Riesgo | Consecuencia |
|---|---|
| **Historial persistente** | Aunque borres el archivo y hagas commit, el secreto queda en el historial de Git para siempre. |
| **Filtraciones públicas** | Miles de repos "privados" se hacen públicos por error cada año. Los bots escanean GitHub en busca de claves en segundos. |
| **Acceso automatizado** | Un token filtrado permite a un atacante vaciar buckets, enviar spam, cifrar datos o suplantar tu identidad sin interacción humana. |
| **Responsabilidad legal** | Muchas normativas (GDPR, PCI-DSS, ISO 27001) obligan a proteger las credenciales; exponerlas puede implicar multas. |

### Buenas prácticas con GitHub Secrets

1. **Principio de mínimo privilegio:** crea tokens con los *scopes* mínimos
   necesarios y fecha de expiración corta.
2. **Usa Environments:** define el job bajo `environment: github-pages` para
   requerir aprobaciones manuales o restringirlo a ramas protegidas.
3. **Nunca imprimas el secreto:** GitHub enmascara automáticamente en los logs
   los valores inyectados vía `${{ secrets.* }}`, pero evita hacer
   `echo $TOKEN` o incluirlo en mensajes de error.
4. **Rota los secretos:** cámbialos periódicamente y si sospechas una fuga,
   revócalos de inmediato desde el proveedor (Slack, AWS, etc.).
5. **Añade `secret scanning` y `push protection`:** GitHub puede bloquear
   automáticamente un `push` si detecta que contiene una clave real.
6. **.gitignore:** aunque uses secrets, mantén un `.gitignore` que excluya
   archivos locales como `.env`.

---

## 📁 Estructura añadida

```
.github/
├── workflows/
│   └── deploy-and-notify.yml   # Pipeline CI/CD seguro
└── scripts/
    └── notify_slack.py         # Script Python que lee creds del entorno
SECURITY_SETUP.md               # Este documento
```

## 🚀 Cómo probar el script en local (sin exponer el secreto)

Desde tu terminal, define la variable de entorno en la sesión actual y ejecuta:

```bash
# Linux/macOS
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/TU/WEBHOOK/REAL"
export GH_REPO="usuario/repositorio"
export GH_RUN_ID="123"
export GH_ACTOR="$(whoami)"
python .github/scripts/notify_slack.py
```

```cmd
:: Windows (cmd)
set SLACK_WEBHOOK_URL=https://hooks.slack.com/services/TU/WEBHOOK/REAL
set GH_REPO=usuario/repositorio
set GH_RUN_ID=123
set GH_ACTOR=%USERNAME%
python .github/scripts/notify_slack.py
```

> ⚠️ Estos comandos **no** guardan el secreto en disco ni en el historial de
> tu shell. Cómpralo solo si tu equipo está libre de malware y el valor lo
> rotas después de la prueba.