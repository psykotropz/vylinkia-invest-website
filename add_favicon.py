"""
Script pour ajouter le favicon à toutes les pages HTML du site
"""

import os
import re

BASE_DIR = r"c:\Users\vpabs\TYTO\vylinkia-invest-website"

def add_favicon_to_html(filepath):
    """Ajoute le favicon à un fichier HTML"""
    print(f"Traitement de {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si le favicon existe déjà
    if 'favicon' in content.lower():
        print(f"  ⚠️  Favicon déjà présent, ignoré\n")
        return
    
    # Déterminer le chemin relatif vers le favicon
    # Compter le nombre de niveaux de profondeur
    relative_path = os.path.relpath(filepath, BASE_DIR)
    depth = relative_path.count(os.sep)
    
    if depth == 0:
        # Fichier à la racine
        favicon_path = "assets/images/favicon.png"
    else:
        # Fichier dans un sous-dossier
        favicon_path = "../" * depth + "assets/images/favicon.png"
    
    # Créer les balises favicon
    favicon_tags = f'''    <link rel="icon" type="image/png" href="{favicon_path}">
    <link rel="apple-touch-icon" href="{favicon_path}">'''
    
    # Insérer après la balise <head>
    pattern = r'(<head>)'
    replacement = r'\1\n' + favicon_tags
    
    content = re.sub(pattern, replacement, content, count=1)
    
    # Écrire le fichier modifié
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Favicon ajouté\n")


def main():
    print("=" * 60)
    print("AJOUT DU FAVICON À TOUTES LES PAGES")
    print("=" * 60)
    print()
    
    # Liste de tous les fichiers HTML
    html_files = []
    
    # Fichiers à la racine
    for file in ['index.html', 'account.html', 'privacy.html', 'terms.html']:
        filepath = os.path.join(BASE_DIR, file)
        if os.path.exists(filepath):
            html_files.append(filepath)
    
    # Fichiers dans les sous-dossiers de langue
    for lang in ['de', 'en', 'es', 'it']:
        lang_dir = os.path.join(BASE_DIR, lang)
        if os.path.exists(lang_dir):
            for file in ['index.html', 'account.html', 'privacy.html', 'terms.html']:
                filepath = os.path.join(lang_dir, file)
                if os.path.exists(filepath):
                    html_files.append(filepath)
    
    # Traiter chaque fichier
    for filepath in html_files:
        try:
            add_favicon_to_html(filepath)
        except Exception as e:
            print(f"  ❌ Erreur: {e}\n")
    
    print("=" * 60)
    print(f"TERMINÉ! {len(html_files)} fichiers traités")
    print("=" * 60)


if __name__ == '__main__':
    main()
