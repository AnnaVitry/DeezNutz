# Fiches Projets

## Projet 1 : Whispen

**Contexte :**  
Tu fais partie de l’équipe produit d’une start-up EdTech qui souhaite développer **Whispen**, une application web
permettant de **transcrire et résumer automatiquement des réunions audio**. L’objectif est de faciliter la prise
de notes et le partage des points clés pour les équipes en télétravail.

**MVP :**  
Enregistrement audio en temps réel ou upload d’un fichier → **transcription automatique (speech-to-text)** → **résumé intelligent** + export du texte.  

**Stack :**  
- **Front :** React / Streamlit / Shiny (interface simple et fluide)  
- **IA / NLP :** Whisper / OpenAI / Hugging Face Transformers  
- **API :** FastAPI pour la gestion des fichiers et des requêtes d’analyse  
- **Base de données :** SQLite / Postgres pour l’historique et les utilisateurs  

**Contraintes :**  
- **RGPD :** fichiers audio supprimés après traitement (pas de stockage permanent)  
- **Compatibilité navigateur :** Chrome / Edge  
- **Accessibilité :** interface claire, adaptée à l’usage sur desktop et tablette  

**Succès :**  
Application fluide et précise, transcription fiable >90%, résumé pertinent et partageable, adoption par les premiers
testeurs internes.