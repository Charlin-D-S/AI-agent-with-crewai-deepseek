import os

# Dossier racine du projet
project_root = ""#"deepseek-agent-lab"

# Arborescence à créer
folders = [
    "agents",
    "tools",
    "tasks",
    "reports"
]

files = {
    "agents/researcher.py": "",
    "tools/pdf_reader.py": "",
    "tools/web_search.py": "",
    "tools/web_scraper.py": "",
    "tasks/summarization.py": "",
    "reports/summary.md": "# Résumé généré par l’agent AI\n\n",
    "main.py": "# Point d’entrée du projet\n",
    #"requirements.txt": "# Voir l’assistant pour le contenu\n",
    #".gitignore": "venv/\n__pycache__/\n.env\nreports/\n",
    #".env": "# Ajouter vos clés API ici\n",
    #"README.md": "# DeepSeek Agent Lab\n\nCe projet contient un agent IA autonome utilisant CrewAI et DeepSeek.\n"
}

# Création des dossiers
#os.makedirs(project_root, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(project_root, folder), exist_ok=True)

# Création des fichiers
for filepath, content in files.items():
    full_path = os.path.join(project_root, filepath)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Projet '{project_root}' initialisé avec succès.")
