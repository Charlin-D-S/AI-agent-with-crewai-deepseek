from crewai_tools import BaseTool
import pdfplumber
import os

class PDFReaderTool(BaseTool):
    name = "PDF Reader"
    description = "Lit un fichier PDF local et retourne son contenu texte brut"

    def _run(self, file_path: str) -> str:
        if not os.path.isfile(file_path):
            return f"Le fichier PDF '{file_path}' est introuvable."

        try:
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text.strip() if text else "Aucun texte lisible trouvé dans le PDF."
        except Exception as e:
            return f"Erreur lors de la lecture du PDF : {str(e)}"
