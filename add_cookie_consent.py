"""
Script pour ajouter automatiquement le bandeau de consentement des cookies
sur toutes les pages du site Vylinkia Invest
"""

import os
import re

# Définir les chemins
BASE_DIR = r"c:\Users\vpabs\TYTO\vylinkia-invest-website"

# Traductions pour chaque langue
TRANSLATIONS = {
    'fr': {
        'title': '🍪 Gestion des cookies',
        'text': 'Nous utilisons des cookies pour améliorer votre expérience et analyser notre trafic avec Google Analytics.',
        'learn_more': 'En savoir plus',
        'decline': 'Refuser',
        'accept': 'Accepter',
        'privacy_link': 'privacy.html'
    },
    'de': {
        'title': '🍪 Cookie-Verwaltung',
        'text': 'Wir verwenden Cookies, um Ihre Erfahrung zu verbessern und unseren Traffic mit Google Analytics zu analysieren.',
        'learn_more': 'Mehr erfahren',
        'decline': 'Ablehnen',
        'accept': 'Akzeptieren',
        'privacy_link': 'privacy.html'
    },
    'en': {
        'title': '🍪 Cookie Management',
        'text': 'We use cookies to improve your experience and analyze our traffic with Google Analytics.',
        'learn_more': 'Learn more',
        'decline': 'Decline',
        'accept': 'Accept',
        'privacy_link': 'privacy.html'
    },
    'es': {
        'title': '🍪 Gestión de cookies',
        'text': 'Utilizamos cookies para mejorar su experiencia y analizar nuestro tráfico con Google Analytics.',
        'learn_more': 'Más información',
        'decline': 'Rechazar',
        'accept': 'Aceptar',
        'privacy_link': 'privacy.html'
    },
    'it': {
        'title': '🍪 Gestione dei cookie',
        'text': 'Utilizziamo i cookie per migliorare la tua esperienza e analizzare il nostro traffico con Google Analytics.',
        'learn_more': 'Maggiori informazioni',
        'decline': 'Rifiuta',
        'accept': 'Accetta',
        'privacy_link': 'privacy.html'
    }
}

# Template du bandeau de cookies
COOKIE_BANNER_TEMPLATE = '''
    <!-- Cookie Consent Banner -->
    <div id="cookieConsent" class="hidden">
        <div class="container mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                    <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path>
                    </svg>
                    <h3 class="font-bold text-lg">{title}</h3>
                </div>
                <p class="text-sm text-slate-300">
                    {text} 
                    <a href="{privacy_link}" class="text-green-400 hover:underline">{learn_more}</a>
                </p>
            </div>
            <div class="cookie-buttons flex gap-3">
                <button onclick="declineCookies()" class="px-6 py-2 bg-slate-700 hover:bg-slate-600 text-white rounded-lg font-medium">
                    {decline}
                </button>
                <button onclick="acceptCookies()" class="px-6 py-2 bg-green-500 hover:bg-green-600 text-slate-900 rounded-lg font-bold">
                    {accept}
                </button>
            </div>
        </div>
    </div>
'''

# Template GA4 conditionnel
GA4_CONDITIONAL = '''    <!-- Google Analytics 4 - Conditional Loading -->
    <script>
        // Check if user has consented to cookies
        function loadGoogleAnalytics() {
            if (localStorage.getItem('cookieConsent') === 'accepted') {
                const script = document.createElement('script');
                script.async = true;
                script.src = 'https://www.googletagmanager.com/gtag/js?id=G-CQFSK6D87P';
                document.head.appendChild(script);

                window.dataLayer = window.dataLayer || [];
                function gtag() { dataLayer.push(arguments); }
                gtag('js', new Date());
                gtag('config', 'G-CQFSK6D87P', {
                    'anonymize_ip': true,
                    'cookie_flags': 'SameSite=None;Secure'
                });
            }
        }
        // Load GA4 if consent already given
        loadGoogleAnalytics();
    </script>'''

# CSS pour le bandeau
COOKIE_CSS = '''
        /* Cookie Consent Banner */
        #cookieConsent {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(to right, #1e293b, #0f172a);
            border-top: 2px solid #22c55e;
            padding: 1.5rem;
            box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.5);
            z-index: 9999;
            transform: translateY(100%);
            transition: transform 0.4s ease-in-out;
        }

        #cookieConsent.show {
            transform: translateY(0);
        }

        .cookie-buttons button {
            transition: all 0.3s ease;
        }

        .cookie-buttons button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);
        }'''

# JavaScript pour le bandeau
COOKIE_JS = '''
        // Cookie Consent Management
        function acceptCookies() {
            localStorage.setItem('cookieConsent', 'accepted');
            hideCookieBanner();
            loadGoogleAnalytics();
            window.location.reload();
        }

        function declineCookies() {
            localStorage.setItem('cookieConsent', 'declined');
            hideCookieBanner();
        }

        function hideCookieBanner() {
            const banner = document.getElementById('cookieConsent');
            if (banner) {
                banner.classList.remove('show');
                setTimeout(() => {
                    banner.classList.add('hidden');
                }, 400);
            }
        }

        function showCookieBanner() {
            const banner = document.getElementById('cookieConsent');
            if (banner) {
                banner.classList.remove('hidden');
                setTimeout(() => {
                    banner.classList.add('show');
                }, 100);
            }
        }

        // Check consent status on page load
        const consent = localStorage.getItem('cookieConsent');
        if (!consent) {
            showCookieBanner();
        }'''


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


def process_html_file(filepath):
    """Traite un fichier HTML pour ajouter le bandeau de cookies"""
    print(f"Traitement de {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Déterminer la langue
    lang = get_language_from_path(filepath)
    trans = TRANSLATIONS[lang]
    
    # 1. Remplacer le GA4 existant par la version conditionnelle
    ga4_pattern = r'<!-- Google Analytics 4.*?</script>'
    if re.search(ga4_pattern, content, re.DOTALL):
        content = re.sub(ga4_pattern, GA4_CONDITIONAL, content, flags=re.DOTALL)
        print(f"  ✓ GA4 conditionnel ajouté")
    
    # 2. Ajouter le CSS si pas déjà présent
    if '#cookieConsent' not in content:
        # Trouver la balise </style> et ajouter avant
        style_end = content.find('</style>')
        if style_end != -1:
            content = content[:style_end] + COOKIE_CSS + '\n    ' + content[style_end:]
            print(f"  ✓ CSS ajouté")
    
    # 3. Ajouter le bandeau HTML après <body>
    if 'id="cookieConsent"' not in content:
        banner_html = COOKIE_BANNER_TEMPLATE.format(**trans)
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + banner_html + content[insert_pos:]
            print(f"  ✓ Bandeau HTML ajouté")
    
    # 4. Ajouter le JavaScript
    if 'function acceptCookies()' not in content:
        # Trouver le premier <script> dans le body ou avant </body>
        script_pattern = r'<script>[\s\S]*?document\.addEventListener\('
        match = re.search(script_pattern, content)
        if match:
            insert_pos = match.start() + 8  # Après <script>
            content = content[:insert_pos] + COOKIE_JS + '\n\n       ' + content[insert_pos:]
            print(f"  ✓ JavaScript ajouté")
    
    # Sauvegarder
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ {filepath} traité avec succès\n")


def main():
    """Fonction principale"""
    # Liste des fichiers à traiter
    files_to_process = [
        # Pages racine
        os.path.join(BASE_DIR, 'index.html'),
        os.path.join(BASE_DIR, 'account.html'),
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
    print("AJOUT DU BANDEAU DE CONSENTEMENT DES COOKIES")
    print("=" * 60)
    print()
    
    for filepath in files_to_process:
        if os.path.exists(filepath):
            try:
                process_html_file(filepath)
            except Exception as e:
                print(f"  ❌ Erreur lors du traitement de {filepath}: {e}\n")
        else:
            print(f"  ⚠️  Fichier non trouvé: {filepath}\n")
    
    print("=" * 60)
    print("TERMINÉ!")
    print("=" * 60)


if __name__ == '__main__':
    main()
