# 🎙️ IA Speech-to-Text + Résumeur local

Ce projet permet de :
1. Transcrire un fichier audio (voix → texte)
2. Générer un résumé automatique du texte obtenu

Le tout **en local**, sans connexion externe ni hébergement.

---

## 🚀 Installation

### 1️⃣ Cloner le projet
```bash
git clone <repo>
cd DeezNutz
```

### 2️⃣ Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## 🎧 Utilisation

**Pour tester le `main.py`**

1. Mets ton fichier audio dans le dossier `audio/` (ex: `exemple.wav`)
2. Dans `src/main.py`, modifie la ligne :
```python
AUDIO_FILE = "audio/exemple.wav"
```
3. Lance le script :
```bash
python src/main.py
```

4. Résultats :
   - Transcription → `output/transcription.txt`
   - Résumé → `output/summary.txt`

**Pour tester via `streamlit`**

1. Lance dans le terminal la commande
```bash
streamlit run src/app.py
```
2. Suis le lien que le server `streamlit` projète et upload un des fichier audio
3. Enjoy :) 

---

## 💡 Conseils

- Les fichiers `.wav` (16 kHz) fonctionnent mieux.
- Tu peux convertir ton audio avec :
```bash
ffmpeg -i tonfichier.mp3 -ar 16000 audio/exemple.wav
```

---

## 🧠 Modèles utilisés

- **Transcription** : [`openai/whisper-small`](https://huggingface.co/openai/whisper-small)
- **Résumé** : [`csebuetnlp/mT5_multilingual_XLSum`](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum)

---

## 🪄 Bonus

Si tu veux une interface simple avec **Streamlit** :
```bash
pip install streamlit
streamlit run app.py
```
