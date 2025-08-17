"""
Fisiocalendario Bot — skeleton (with /orario + external exercises)
=================================================================

Stack:
- Python 3.10+
- python-telegram-bot >= 20.7
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

Run locally:
  pip install python-telegram-bot==20.7 pytz pyyaml
  export TELEGRAM_BOT_TOKEN=8469888896:AAExFxTlx2YEKNPZJd20Pn15tEcF54rRbBU
  export PAYMENTS_PROVIDER_TOKEN=284685063:TEST:12345
  python main.py

Notes:
- Educational skeleton: review medical content; add disclaimers consistent with your practice.
- Replace/expand exercises in exercises.yaml referencing reputable public libraries.
"""
[... codice invariato ...]

# -----------------------------------------------
#  exercises.yaml (save next to main.py)
# -----------------------------------------------
# Linee guida: contenuti generici, adatti a adulti sani. Non sostituiscono il parere clinico.
# Adatta testi/dosaggi al tuo target e alle linee guida locali.

stretching:
  - title: "Stretching cervicale laterale"
    description: "Siediti eretto. Inclina la testa verso la spalla destra fino a lieve tensione, senza ruotare. Ripeti a sinistra."
    dosage: "2×30s per lato"
  - title: "Flessione laterale del tronco in piedi"
    description: "Piedi alla larghezza delle spalle. Scivola con la mano lungo la coscia destra inclinando il busto, poi a sinistra."
    dosage: "2×10 ripetizioni per lato"
  - title: "Allungamento trapezio superiore (auto)"
    description: "Siediti. Con la mano destra afferra delicatamente la testa e inclina verso destra. Spalle rilassate."
    dosage: "2×30s per lato"
  - title: "Apertura toracica alla porta"
    description: "Avambraccio su stipite, gomito a 90°. Avanza con il corpo fino a sentire allungamento pettorale."
    dosage: "2×30s per lato"
  - title: "Ischiocrurali in piedi"
    description: "Tallone sul gradino, ginocchio esteso ma non in blocco. Inclina leggermente il busto in avanti."
    dosage: "2×30s per lato"
  - title: "Polpacci al muro"
    description: "Punta del piede contro il muro, ginocchio esteso. Avanza con il corpo fino a sentire il polpaccio."
    dosage: "2×30s per lato"
  - title: "Mobilità caviglia in affondo"
    description: "Piede anteriore a 10–15 cm dal muro, spingi il ginocchio verso il muro senza sollevare il tallone."
    dosage: "2×10 ripetizioni per lato"
  - title: "Rotazioni colonna da seduto"
    description: "Schiena lunga, mani sulle spalle. Ruota il busto a destra e a sinistra con movimento lento e controllato."
    dosage: "2×10 ripetizioni per lato"
  - title: "Cat–Camel (mobilità spinale)"
    description: "In quadrupedia, alterna incurvare e inarcare dolcemente la schiena coordinando il respiro."
    dosage: "2×10 cicli"
  - title: "Quadricipite in piedi"
    description: "In piedi, afferra la caviglia e porta il tallone verso i glutei mantenendo le ginocchia vicine."
    dosage: "2×30s per lato"

equilibrio:
  - title: "Equilibrio monopodalico"
    description: "In piedi vicino a un supporto, solleva un piede e mantieni la posizione. Mantieni sguardo fisso."
    dosage: "3×20–30s per lato"
  - title: "Tandem stance (piedi in linea)"
    description: "Piede anteriore davanti all'altro sulla stessa linea. Mantieni la posizione senza oscillare."
    dosage: "3×30s (inverte i piedi)"
  - title: "Camminata tallone–punta"
    description: "Cammina su una linea immaginaria appoggiando tallone su punta del piede precedente."
    dosage: "2×10 passi avanti e indietro"
  - title: "Step-over lento su linea"
    description: "Posiziona una corda o linea bassa. Superala lentamente alternando i piedi, guardando avanti."
    dosage: "2×12 passaggi"
  - title: "Sit-to-Stand controllato"
    description: "Da sedia, alzati e siediti senza usare le mani. Controlla discesa e appoggio."
    dosage: "3×10 ripetizioni"
  - title: "Weight shift laterale"
    description: "In piedi, sposta il peso da una gamba all'altra senza sollevare i piedi, mantenendo postura diritta."
    dosage: "3×12 spostamenti"
  - title: "Monopodalico occhi chiusi (avanzato)"
    description: "Come il monopodalico, ma con occhi chiusi e vicino a supporto per sicurezza."
    dosage: "3×10–20s per lato"
  - title: "Semi-squat con reach avanti"
    description: "Mezzo squat leggero, porta le braccia in avanti come a toccare un oggetto lontano, poi ritorna."
    dosage: "3×8–10 ripetizioni"
  - title: "Camminata su talloni e punte"
    description: "Percorri alcuni metri camminando prima sui talloni, poi sulle punte, mantenendo equilibrio."
    dosage: "2×10 metri per variante"
  - title: "Clock reach"
    description: "In monopodalico tocca con il piede libero le posizioni di un orologio (12–3–6–9)."
    dosage: "2 giri per lato"

respirazione:
  - title: "Respirazione diaframmatica"
    description: "Mano sull'addome. Inspira dal naso gonfiando la pancia, espira lentamente dalla bocca."
    dosage: "10–12 respiri lenti"
  - title: "Box breathing 4–4–4–4"
    description: "Inspira 4s, trattieni 4s, espira 4s, pausa 4s. Mantieni un ritmo confortevole."
    dosage: "4–6 cicli"
  - title: "Tecnica 4–7–8"
    description: "Inspira 4s, trattieni 7s, espira 8s. Siediti comodo. Interrompi se avverti capogiri."
    dosage: "4 cicli"
  - title: "Coerenza cardiaca (6 cpm)"
    description: "Respira a ritmo regolare: inspira 5s, espira 5s, per 5 minuti."
    dosage: "1 sessione da 5 minuti"
  - title: "Labbra socchiuse (pursed-lip)"
    description: "Inspira dal naso 2s, espira dalla bocca a labbra socchiuse 4s (espirazione più lunga)."
    dosage: "10 respiri"
  - title: "Respiro quadrato 3–3–3–3"
    description: "Versione dolce: inspira 3s, trattieni 3s, espira 3s, pausa 3s."
    dosage: "6–8 cicli"
  - title: "Respirazione latero-costale"
    description: "Mani ai lati del torace. Espandi i lati durante l'inspirazione, senti le costole muoversi."
    dosage: "2×8 respiri"
  - title: "Rapporto 1:2 (espirazione prolungata)"
    description: "Stabilisci un conteggio comodo (es. 3:6). Inspira 3, espira 6 mantenendo fluidità."
    dosage: "10 cicli"
  - title: "Naso–naso lenta"
    description: "Respira solo dal naso a ritmo lento e confortevole, seduto rilassato."
    dosage: "2 minuti continui"
  - title: "Respiro + body scan"
    description: "Respira lentamente mentre sposti l'attenzione progressivamente su spalle, torace, addome e gambe."
    dosage: "2–3 minuti"


# =============================
# Repo skeleton for GitHub
# =============================

# File: requirements.txt
# ----------------------
# Pin stable versions
python-telegram-bot==20.7
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
# Copy to .env and fill values
TELEGRAM_BOT_TOKEN=123456:ABCDEF
PAYMENTS_PROVIDER_TOKEN=284685063:TEST:12345
DB_PATH=fisiocalendario.db
EXERCISES_PATH=exercises.yaml


# File: Procfile  (Heroku/Railway)
# --------------------------------
worker: python main.py


# File: render.yaml  (Render.com optional)
# ---------------------------------------
services:
  - type: worker
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


# File: Dockerfile (opzionale)
# ----------------------------
# Usa solo se vuoi containerizzare
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
2. Su Render → New + Worker → collega repo.
3. Build: `pip install -r requirements.txt` — Start: `python main.py`.
4. Inserisci env vars: `TELEGRAM_BOT_TOKEN`, `PAYMENTS_PROVIDER_TOKEN`, `DB_PATH`, `EXERCISES_PATH`.
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
