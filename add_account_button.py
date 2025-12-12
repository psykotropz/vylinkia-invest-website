"""
Script pour ajouter le bouton "Mon Compte" sur toutes les pages du site
"""

import os
import re

BASE_DIR = r"c:\Users\vpabs\TYTO\vylinkia-invest-website"

# Traductions du bouton "Mon Compte"
TRANSLATIONS = {
    'fr': 'Mon Compte',
    'de': 'Mein Konto',
    'en': 'My Account',
    'es': 'Mi Cuenta',
    'it': 'Il Mio Account'
}

def get_language_from_path(filepath):
    """Détermine la langue en fonction du chemin du fichier"""
    if '/de/' in filepath or '\\de\\' in filepath:
        return 'de'
    elif '/en/' in filepath or '\\en\\' in filepath:
        return 'en'
    elif '/es/' in filepath or '\\es\\' in filepath:
        return 'es'
    elif '/it/' in filepath or '\\it\\' in filepath:
        return 'it'
    else:
        return 'fr'


def add_account_button(filepath):
    """Ajoute le bouton Mon Compte dans la navbar"""
    print(f"Traitement de {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si le bouton existe déjà
    if 'account.html' in content and 'Mon Compte' in content or 'My Account' in content or 'Mein Konto' in content:
        print(f"  ⚠️  Bouton déjà présent, ignoré\n")
        return
    
    lang = get_language_from_path(filepath)
    account_text = TRANSLATIONS[lang]
    
    # Déterminer le chemin relatif vers account.html
    if lang == 'fr':
        account_link = 'account.html'
    else:
        account_link = '../account.html'
    
    # Pattern pour trouver le bouton Télécharger/Download
    download_patterns = [
        r'(\s+)</div>\s+<a href="#" class="bg-green-500[^>]+>[\s\S]*?Télécharger[\s\S]*?</a>',
        r'(\s+)</div>\s+<a href="#" class="bg-green-500[^>]+>[\s\S]*?Download[\s\S]*?</a>',
        r'(\s+)</div>\s+<a href="#" class="bg-green-500[^>]+>[\s\S]*?Descargar[\s\S]*?</a>',
        r'(\s+)</div>\s+<a href="#" class="bg-green-500[^>]+>[\s\S]*?Herunterladen[\s\S]*?</a>',
        r'(\s+)</div>\s+<a href="#" class="bg-green-500[^>]+>[\s\S]*?Scarica[\s\S]*?</a>',
    ]
    
    button_html = f'''        </div>
        <div class="flex items-center gap-4">
            <a href="{account_link}" class="hidden md:flex items-center gap-2 text-slate-300 hover:text-green-400 transition" title="{account_text}">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                </svg>
                <span class="font-medium">{account_text}</span>
            </a>'''
    
    modified = False
    for pattern in download_patterns:
        if re.search(pattern, content):
            # Remplacer en gardant le bouton download
            content = re.sub(
                pattern,
                lambda m: button_html + '\n' + m.group(0).replace(m.group(1) + '</div>\n        ', '            '),
                content
            )
            modified = True
            break
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Bouton ajouté avec succès\n")
    else:
        print(f"  ❌ Pattern non trouvé\n")


def main():
    files_to_process = [
        # Pages racine
        os.path.join(BASE_DIR, 'index.html'),
        os.path.join(BASE_DIR, 'privacy.html'),
        os.path.join(BASE_DIR, 'terms.html'),
        # Pages DE
        os.path.join(BASE_DIR, 'de', 'index.html'),
        os.path.join(BASE_DIR, 'de', 'privacy.html'),
        os.path.join(BASE_DIR, 'de', 'terms.html'),
        # Pages EN
        os.path.join(BASE_DIR, 'en', 'index.html'),
        os.path.join(BASE_DIR, 'en', 'privacy.html'),
        os.path.join(BASE_DIR, 'en', 'terms.html'),
        # Pages ES
        os.path.join(BASE_DIR, 'es', 'index.html'),
        os.path.join(BASE_DIR, 'es', 'privacy.html'),
        os.path.join(BASE_DIR, 'es', 'terms.html'),
        # Pages IT
        os.path.join(BASE_DIR, 'it', 'index.html'),
        os.path.join(BASE_DIR, 'it', 'privacy.html'),
        os.path.join(BASE_DIR, 'it', 'terms.html'),
    ]
    
    print("=" * 60)
    print("AJOUT DU BOUTON MON COMPTE")
    print("=" * 60)
    print()
    
    for filepath in files_to_process:
        if os.path.exists(filepath):
            try:
                add_account_button(filepath)
            except Exception as e:
                print(f"  ❌ Erreur: {e}\n")
        else:
            print(f"  ⚠️  Fichier non trouvé: {filepath}\n")
    
    print("=" * 60)
    print("TERMINÉ!")
    print("=" * 60)


if __name__ == '__main__':
    main()
