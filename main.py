# Point d’entrée du projet
from tools.pdf_reader import PDFReaderTool

def main():
    # Spécifie le chemin vers ton fichier PDF
    pdf_path = "documents/test.pdf"  # Assure-toi que ce fichier existe

    # Initialise l'outil
    pdf_reader = PDFReaderTool()

    # Exécute l'outil avec le chemin du fichier
    print("📄 Lecture du PDF en cours...")
    result = pdf_reader._run(pdf_path)

    # Affiche le résultat
    print("\n🧾 Contenu extrait :\n")
    print(result[:2000])  # Affiche seulement les 2000 premiers caractères pour ne pas surcharger le terminal

if __name__ == "__main__":
    main()
