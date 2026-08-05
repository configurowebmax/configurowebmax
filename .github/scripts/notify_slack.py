#!/usr/bin/env python3
"""
notify_slack.py — Notificación segura a Slack desde GitHub Actions.

SEGURIDAD
---------
- No contiene credenciales en el código.
- Lee el Webhook de Slack desde la variable de entorno `SLACK_WEBHOOK_URL`
  (configurada por el usuario en GitHub -> Settings -> Secrets -> Actions,
  y mapeada a `env:` en el workflow).
- No imprime jamás el valor del secreto; solo reporta si está ausente.
- Usa exclusivamente la librería estándar (urllib) => cero dependencias externas.
"""

import json
import os
import sys
import urllib.request
import urllib.error


def build_message(repo: str, run_id: str, actor: str) -> dict:
    """Construye el payload de Slack con datos públicos del workflow."""
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}"
    return {
        "text": f":rocket: *Despliegue del portafolio completado* por `{actor}`.\n"
                f"Repositorio: `{repo}`\n"
                f"Ver ejecución: {run_url}",
        "unfurl_links": False,
    }


def send_slack_message(webhook_url: str, payload: dict) -> None:
    """Envía el mensaje a Slack vía HTTP POST."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            # Slack responde "ok" cuando todo sale bien.
            if resp.status != 200 or body.strip() != "ok":
                print(f"[WARN] Respuesta inesperada de Slack (HTTP {resp.status}): {body}")
                sys.exit(1)
            print("[OK] Notificación enviada a Slack correctamente.")
    except urllib.error.HTTPError as e:
        print(f"[ERROR] Slack devolvió HTTP {e.code}: {e.reason}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] No se pudo contactar a Slack: {e.reason}")
        sys.exit(1)


def main() -> None:
    # --- Lectura segura de variables de entorno ---
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    repo = os.environ.get("GH_REPO", "repo-desconocido")
    run_id = os.environ.get("GH_RUN_ID", "0")
    actor = os.environ.get("GH_ACTOR", "unknown")

    # Validación defensiva: nunca se imprime el valor del secreto.
    if not webhook_url:
        print("[ERROR] La variable de entorno SLACK_WEBHOOK_URL no está definida.")
        print("        Configúrala como Repository Secret en GitHub y mapeala en el workflow.")
        sys.exit(1)

    if not webhook_url.startswith("https://"):
        print("[ERROR] SLACK_WEBHOOK_URL debe ser una URL HTTPS válida.")
        sys.exit(1)

    payload = build_message(repo, run_id, actor)
    send_slack_message(webhook_url, payload)


if __name__ == "__main__":
    main()