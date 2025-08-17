"""
Fisiocalendario Bot — skeleton (with /orario + external exercises)
=================================================================

Stack:
- Python 3.10+
- python-telegram-bot[webhooks] >= 20.7
- PyYAML
- SQLite (via sqlite3)

Features in this version:
- FREE: /oggi sends one random exercise from all categories.
- PREMIUM (€1/month): in-bot payment (Telegram Payments). Premium users
  receive 2 exercises/day from a chosen category and can access /storico.
- PERSONALIZED PLAN (€5 one-off): /personalizzato -> payment -> mini
  questionnaire -> 7-day plan (text-based) and daily delivery.
- Daily scheduler per-user with preferred time via **/orario** (default 08:00 Europe/Rome).
- Exercises moved to **exercises.yaml** (loaded at startup). Fallback to a minimal
  built-in corpus if the file is missing.

ENV required (or hardcode for tests):
- TELEGRAM_BOT_TOKEN
- PAYMENTS_PROVIDER_TOKEN
- DB_PATH (optional)
- EXERCISES_PATH (optional, default: exercises.yaml)
- WEBHOOK_URL (solo in modalità webhook; es. https://tuo-servizio.onrender.com/telegram)

Run locally (polling):
  pip install python-telegram-bot[webhooks]==20.7 pytz pyyaml
  export TELEGRAM_BOT_TOKEN=123:ABC
  export PAYMENTS_PROVIDER_TOKEN=284685063:TEST:12345
  python main.py

Run on Render (webhook):
  set WEBHOOK_URL=https://<tuo-servizio>.onrender.com/telegram
  set PORT=10000 (Render la imposta automaticamente)

Notes:
- Educational skeleton: review medical content; add disclaimers consistent with your practice.
- Replace/expand exercises in exercises.yaml referencing reputable public libraries.
"""

[... codice invariato ...]

if __name__ == "__main__":
    # Modalità: webhook se WEBHOOK_URL è definita, altrimenti polling
    application = build_app()

    WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
    if WEBHOOK_URL:
        # --- Webhook mode (Render Web Service free) ---
        from aiohttp import web

        async def health(_request):
            return web.Response(text="ok")

        web_app = web.Application()
        web_app.router.add_get("/", health)

        listen = "0.0.0.0"
        port = int(os.environ.get("PORT", "10000"))
        url_path = os.environ.get("WEBHOOK_PATH", "telegram")
        full_webhook = WEBHOOK_URL.rstrip("/")

        application.run_webhook(
            listen=listen,
            port=port,
            url_path=url_path,
            webhook_url=full_webhook,
            web_app=web_app,
            allowed_updates=Update.ALL_TYPES,
        )
    else:
        # --- Polling mode (sviluppo locale) ---
        application.run_polling(allowed_updates=Update.ALL_TYPES)


# =============================
# Repo skeleton for GitHub
# =============================

# File: requirements.txt
# ----------------------
python-telegram-bot[webhooks]==20.7
pytz==2024.1
PyYAML==6.0.2


# File: .gitignore
# ----------------
__pycache__/
*.pyc
*.pyo
*.db
.env
.venv/
venv/


# File: .env.example
# ------------------
TELEGRAM_BOT_TOKEN=123456:ABCDEF
PAYMENTS_PROVIDER_TOKEN=284685063:TEST:12345
DB_PATH=fisiocalendario.db
EXERCISES_PATH=exercises.yaml
WEBHOOK_URL=https://your-service.onrender.com/telegram


# File: Procfile  (Heroku/Railway)
# --------------------------------
worker: python main.py


# File: render.yaml  (Render.com — Web Service con webhook)
# --------------------------------------------------------
services:
  - type: web
    name: fisiocalendario-bot
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: TELEGRAM_BOT_TOKEN
        sync: false
      - key: PAYMENTS_PROVIDER_TOKEN
        sync: false
      - key: DB_PATH
        value: fisiocalendario.db
      - key: EXERCISES_PATH
        value: exercises.yaml
      - key: WEBHOOK_URL
        value: https://your-service.onrender.com/telegram
    healthCheckPath: /
    autoDeploy: true


# File: Dockerfile (opzionale)
# ----------------------------
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]


# File: README.md
# ---------------
# Fisiocalendario Bot

Bot Telegram per esercizi giornalieri (stretching, equilibrio, respirazione) con:
- Gratis: 1 esercizio casuale al giorno (/oggi)
- Premium (1€/mese): 2 esercizi/dì, scelta categoria, /storico
- Piano personalizzato (5€): calendario 7 giorni
- /orario per scegliere l’ora del promemoria (Europe/Rome)

## Requisiti
- Python ≥3.10
- Token Telegram del bot (da @BotFather)
- Token provider pagamenti (Telegram Payments 2.0)

## Setup locale
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # poi compila i token
python main.py
```
Apri Telegram, cerca il tuo bot e invia `/start`.

> Modalità polling: il bot funziona finché il processo è attivo.

## Deploy su Render (consigliato)
1. Crea repo GitHub con questi file.
2. Su Render → New + Web Service → collega repo.
3. Build: `pip install -r requirements.txt` — Start: `python main.py`.
4. Inserisci env vars: `TELEGRAM_BOT_TOKEN`, `PAYMENTS_PROVIDER_TOKEN`, `DB_PATH`, `EXERCISES_PATH`, `WEBHOOK_URL`.
5. Deploy. Il bot resta attivo h24.

## Pagamenti (Premium e Personalizzato)
- Attiva i pagamenti con @BotFather → `/mybots` → Payments → collega provider (Stripe, ecc.).
- Metti il token in `PAYMENTS_PROVIDER_TOKEN`.
- In test, usa credenziali *sandbox* del provider.

## Esercizi
- Modifica `exercises.yaml` per aggiungere/aggiornare contenuti.
- Formato: `title`, `description`, `dosage` per ciascuna categoria (`stretching`, `equilibrio`, `respirazione`).

## Note cliniche
- Contenuti informativi e generici, non sostituiscono consulenza sanitaria.
- Interrompere in caso di dolore o sintomi anomali.

## Licenza
MIT (o quella che preferisci).
