import os
import re

# Source Content (French) to Target Content (Languages)
translations = {
    'en': {
        'lang': 'en',
        'title': 'How does Market Pulse work? - Vylinkia Transparency',
        'desc_meta': 'Discover how our \'Market Pulse\' algorithm analyzes 13 macro-economic indicators in real-time to determine the market regime (Risk-On/Off). No magic, just math.',
        'nav_home': 'Home',
        'nav_features': 'Features',
        'nav_pricing': 'Pricing',
        'nav_contact': 'Contact',
        'download_btn': 'Download App',
        'hero_title': 'It\'s not magic.<br>\n            It\'s <span class="gradient-text">Data Processing</span>.',
        'hero_desc': 'The "Market Pulse" is not a hunch. It is a deterministic algorithm that scans\n            <strong>13 asset baskets</strong> in real-time to decide if the light is Green (Buy) or Red\n            (Protect).',
        'sec1_title': '1. The Sensors (Input)',
        'sec1_desc': 'Our algorithm doesn\'t just look at the S&P 500. It monitors the overall health of the economy across 13\n                key sectors over a 7-day window.',
        'group_risk_on': '⚠️ "Risk" Assets',
        'group_risk_off': '🛡️ "Safe Haven" Assets',
        'group_global': '🌍 Global Context',
        'sec2_title': '2. The Logic (Algorithm)',
        'step1_title': 'The Weighted Sentiment Score',
        'step1_desc': 'The AI first calculates a raw score based on the performance (7 days) of each sector.',
        'step1_sub': 'If score > 5, usually good. If < -5, caution.',
        'step2_title': 'The "Smart Alerts" (Priority Exceptions)',
        'step2_desc': 'Before listening to the score, the algorithm checks critical scenarios that override everything else.\n                            It is our safety net.',
        'alert_bubble': '🎈 Bubble',
        'alert_bubble_desc': 'If Tech is up big (>2%) but the rest of economy is down. = <strong>Danger</strong>.',
        'alert_forex': '💨 Forex',
        'alert_forex_desc': 'If US market is up but Dollar crashes vs Euro. = <strong>Gains erased for you</strong>.',
        'alert_luxury': '🇨🇳 Luxury',
        'alert_luxury_desc': 'If Asia crashes hard. = <strong>Alert on LVMH/Kering</strong>.',
        'faq_title': 'Total Transparency',
        'q1': 'Is it an automated "Trading Bot"?',
        'a1': '<strong>No.</strong> Vylinkia is a decision support tool. The AI does the analysis work\n                        (which would take a human 4 hours/day) in milliseconds, but <strong>you</strong>\n                        validate and place the order. We do not manage your money.',
        'q2': 'Where does the data come from?',
        'a2': 'We use professional stock market data feeds (Twelve Data & Yahoo Finance APIs)\n                        aggregated in real-time. Our servers in the Netherlands recalculate the Market Pulse every 4\n                        hours.',
        'q3': 'Why "7 days"?',
        'a3': 'We specialize in <strong>Swing Trading</strong>. The weekly trend is the most relevant\n                        to filter out daily "noise" while being reactive enough not to miss\n                        opportunities.',
        'cta_btn': 'Download Assistant',
        'footer_back': '← Back to Home',
        'footer_privacy': 'Privacy Policy',
        'footer_terms': 'Terms of Use',
        'footer_transparency': 'Algo Transparency' 
    },
    'es': {
        'lang': 'es',
        'title': '¿Cómo funciona Market Pulse? - Transparencia Vylinkia',
        'desc_meta': 'Descubre cómo nuestro algoritmo \'Market Pulse\' analiza 13 indicadores macroeconómicos en tiempo real para determinar el régimen de mercado. Sin magia, solo matemáticas.',
        'nav_home': 'Inicio',
        'nav_features': 'Funcionalidades',
        'nav_pricing': 'Precios',
        'nav_contact': 'Contacto',
        'download_btn': 'Descargar App',
        'hero_title': 'No es magia.<br>\n            Es <span class="gradient-text">Procesamiento de Datos</span>.',
        'hero_desc': 'El "Market Pulse" no es una intuición. Es un algoritmo determinista que escanea\n            <strong>13 cestas de activos</strong> en tiempo real para decidir si la luz es Verde (Comprar) o Roja\n            (Proteger).',
        'sec1_title': '1. Los Sensores (Input)',
        'sec1_desc': 'Nuestro algoritmo no solo mira el S&P 500. Monitorea la salud general de la economía a través de 13\n                sectores clave en una ventana de 7 días.',
        'group_risk_on': '⚠️ Activos de "Riesgo"',
        'group_risk_off': '🛡️ Activos "Refugio"',
        'group_global': '🌍 Contexto Global',
        'sec2_title': '2. La Lógica (Algoritmo)',
        'step1_title': 'Puntaje de Sentimiento Ponderado',
        'step1_desc': 'La IA calcula primero un puntaje bruto basado en el rendimiento (7 días) de cada sector.',
        'step1_sub': 'Si score > 5, generalmente bueno. Si < -5, precaución.',
        'step2_title': 'Las "Smart Alerts" (Excepciones Prioritarias)',
        'step2_desc': 'Antes de escuchar el puntaje, el algoritmo verifica escenarios críticos que anulan todo lo demás.\n                            Es nuestra red de seguridad.',
        'alert_bubble': '🎈 Burbuja',
        'alert_bubble_desc': 'Si Tech sube mucho (>2%) pero el resto baja. = <strong>Peligro</strong>.',
        'alert_forex': '💨 Divisa',
        'alert_forex_desc': 'Si mercado US sube pero Dólar cae vs Euro. = <strong>Ganancias borradas para ti</strong>.',
        'alert_luxury': '🇨🇳 Lujo',
        'alert_luxury_desc': 'Si Asia cae fuerte. = <strong>Alerta sobre LVMH/Kering</strong>.',
        'faq_title': 'Transparencia Total',
        'q1': '¿Es un "Bot de Trading" automatizado?',
        'a1': '<strong>No.</strong> Vylinkia es una herramienta de apoyo a la decisión. La IA hace el trabajo de análisis\n                        (que tomaría 4h/día a un humano) en milisegundos, pero <strong>tú</strong>\n                        validas y colocas la orden. No gestionamos tu dinero.',
        'q2': '¿De dónde vienen los datos?',
        'a2': 'Usamos feeds de datos bursátiles profesionales (APIs Twelve Data & Yahoo Finance)\n                        agregados en tiempo real. Nuestros servidores en Países Bajos recalculan el Market Pulse cada 4\n                        horas.',
        'q3': '¿Por qué "7 días"?',
        'a3': 'Nos especializamos en <strong>Swing Trading</strong>. La tendencia semanal es la más relevante\n                        para filtrar el "ruido" diario siendo lo suficientemente reactiva para no perder\n                        oportunidades.',
        'cta_btn': 'Descargar Asistente',
        'footer_back': '← Volver al Inicio',
        'footer_privacy': 'Política de Privacidad',
        'footer_terms': 'Términos de Uso',
        'footer_transparency': 'Transparencia Algo'
    },
    'de': {
        'lang': 'de',
        'title': 'Wie funktioniert Market Pulse? - Vylinkia Transparenz',
        'desc_meta': 'Entdecken Sie, wie unser \'Market Pulse\'-Algorithmus 13 makroökonomische Indikatoren in Echtzeit analysiert. Keine Magie, nur Mathematik.',
        'nav_home': 'Startseite',
        'nav_features': 'Funktionen',
        'nav_pricing': 'Preise',
        'nav_contact': 'Kontakt',
        'download_btn': 'App herunterladen',
        'hero_title': 'Es ist keine Magie.<br>\n            Es ist <span class="gradient-text">Datenverarbeitung</span>.',
        'hero_desc': 'Der "Market Pulse" ist keine Ahnung. Es ist ein deterministischer Algorithmus, der\n            <strong>13 Anlagekörbe</strong> in Echtzeit scannt, um zu entscheiden, ob das Licht Grün (Kaufen) oder Rot\n            (Schützen) ist.',
        'sec1_title': '1. Die Sensoren (Input)',
        'sec1_desc': 'Unser Algorithmus schaut nicht nur auf den S&P 500. Er überwacht die allgemeine Gesundheit der Wirtschaft über 13\n                Schlüsselsektoren in einem 7-Tage-Fenster.',
        'group_risk_on': '⚠️ "Risiko"-Anlagen',
        'group_risk_off': '🛡️ "Sichere Hafen"-Anlagen',
        'group_global': '🌍 Globaler Kontext',
        'sec2_title': '2. Die Logik (Algorithmus)',
        'step1_title': 'Der gewichtete Stimmungs-Score',
        'step1_desc': 'Die KI berechnet zunächst einen Roh-Score basierend auf der Leistung (7 Tage) jedes Sektors.',
        'step1_sub': 'Wenn Score > 5, meistens gut. Wenn < -5, Vorsicht.',
        'step2_title': 'Die "Smart Alerts" (Prioritätsausnahmen)',
        'step2_desc': 'Bevor er auf den Score hört, prüft der Algorithmus kritische Szenarien, die alles andere annullieren.\n                            Das ist unser Sicherheitsnetz.',
        'alert_bubble': '🎈 Blase',
        'alert_bubble_desc': 'Wenn Tech stark steigt (>2%), aber der Rest fällt. = <strong>Gefahr</strong>.',
        'alert_forex': '💨 Währung',
        'alert_forex_desc': 'Wenn US-Markt steigt, aber Dollar gegen Euro abstürzt. = <strong>Gewinne für Sie gelöscht</strong>.',
        'alert_luxury': '🇨🇳 Luxus',
        'alert_luxury_desc': 'Wenn Asien hart abstürzt. = <strong>Alarm für LVMH/Kering</strong>.',
        'faq_title': 'Totale Transparenz',
        'q1': 'Ist es ein automatisierter "Trading Bot"?',
        'a1': '<strong>Nein.</strong> Vylinkia ist ein Entscheidungshilfetool. Die KI erledigt die Analysearbeit\n                        (die einen Menschen 4 Stunden/Tag kosten würde) in Millisekunden, aber <strong>Sie</strong>\n                        validieren und platzieren die Order. Wir verwalten Ihr Geld nicht.',
        'q2': 'Woher kommen die Daten?',
        'a2': 'Wir nutzen professionelle Börsendaten-Feeds (Twelve Data & Yahoo Finance APIs)\n                        in Echtzeit aggregiert. Unsere Server in den Niederlanden berechnen den Market Pulse alle 4\n                        Stunden neu.',
        'q3': 'Warum "7 Tage"?',
        'a3': 'Wir sind auf <strong>Swing Trading</strong> spezialisiert. Der wöchentliche Trend ist am relevantesten,\n                        um das tägliche "Rauschen" zu filtern, während man reaktiv genug bleibt, um Chancen nicht zu\n                        verpassen.',
        'cta_btn': 'Assistent herunterladen',
        'footer_back': '← Zurück zur Startseite',
        'footer_privacy': 'Datenschutzrichtlinie',
        'footer_terms': 'Nutzungsbedingungen',
        'footer_transparency': 'Algo Transparenz'
    },
    'it': {
        'lang': 'it',
        'title': 'Come funziona Market Pulse? - Trasparenza Vylinkia',
        'desc_meta': 'Scopri come il nostro algoritmo \'Market Pulse\' analizza 13 indicatori macroeconomici in tempo reale. Niente magia, solo matematica.',
        'nav_home': 'Home',
        'nav_features': 'Funzionalità',
        'nav_pricing': 'Prezzi',
        'nav_contact': 'Contatti',
        'download_btn': 'Scarica App',
        'hero_title': 'Non è magia.<br>\n            È <span class="gradient-text">Elaborazione Dati</span>.',
        'hero_desc': 'Il "Market Pulse" non è un\'intuizione. È un algoritmo deterministico che scansiona\n            <strong>13 panieri di asset</strong> in tempo reale per decidere se il semaforo è Verde (Comprare) o Rosso\n            (Proteggere).',
        'sec1_title': '1. I Sensori (Input)',
        'sec1_desc': 'Il nostro algoritmo non guarda solo l\'S&P 500. Monitora la salute generale dell\'economia attraverso 13\n                settori chiave su una finestra di 7 giorni.',
        'group_risk_on': '⚠️ Asset "Rischio"',
        'group_risk_off': '🛡️ Asset "Rifugio"',
        'group_global': '🌍 Contesto Globale',
        'sec2_title': '2. La Logica (Algoritmo)',
        'step1_title': 'Il Punteggio di Sentimento Ponderato',
        'step1_desc': 'L\'IA calcola prima un punteggio grezzo basato sulla performance (7 giorni) di ogni settore.',
        'step1_sub': 'Se score > 5, generalmente buono. Se < -5, attenzione.',
        'step2_title': 'Gli "Smart Alerts" (Eccezioni Prioritarie)',
        'step2_desc': 'Prima di ascoltare il punteggio, l\'algoritmo verifica scenari critici che annullano tutto il resto.\n                            È la nostra rete di sicurezza.',
        'alert_bubble': '🎈 Bolla',
        'alert_bubble_desc': 'Se il Tech sale forte (>2%) ma il resto scende. = <strong>Pericolo</strong>.',
        'alert_forex': '💨 Valuta',
        'alert_forex_desc': 'Se il mercato US sale ma il Dollaro crolla vs Euro. = <strong>Guadagni cancellati per te</strong>.',
        'alert_luxury': '🇨🇳 Lusso',
        'alert_luxury_desc': 'Se l\'Asia crolla duramente. = <strong>Allerta su LVMH/Kering</strong>.',
        'faq_title': 'Trasparenza Totale',
        'q1': 'È un "Trading Bot" automatizzato?',
        'a1': '<strong>No.</strong> Vylinkia è uno strumento di supporto decisionale. L\'IA fa il lavoro di analisi\n                        (che richiederebbe 4h al giorno a un umano) in millisecondi, ma <strong>tu</strong>\n                        validi e inserisci l\'ordine. Non gestiamo i tuoi soldi.',
        'q2': 'Da dove vengono i dati?',
        'a2': 'Usiamo feed di dati borsistici professionali (API Twelve Data & Yahoo Finance)\n                        aggregati in tempo reale. I nostri server nei Paesi Bassi ricalcolano il Market Pulse ogni 4\n                        ore.',
        'q3': 'Perché "7 giorni"?',
        'a3': 'Siamo specializzati nello <strong>Swing Trading</strong>. Il trend settimanale è il più rilevante\n                        per filtrare il "rumore" quotidiano rimanendo abbastanza reattivi per non perdere\n                        opportunità.',
        'cta_btn': 'Scarica Assistente',
        'footer_back': '← Torna alla Home',
        'footer_privacy': 'Privacy Policy',
        'footer_terms': 'Termini d\'Uso',
        'footer_transparency': 'Trasparenza Algo'
    }
}

# Template: Read existing French file to get structure
base_path = r'c:\Users\vpabs\TYTO\vylinkia-invest-website'
fr_file_path = os.path.join(base_path, 'market-pulse.html')

with open(fr_file_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Function to replace text
def generate_file(lang_code, lang_data):
    content = template
    
    # Simple Replacements
    content = content.replace('lang="fr"', f'lang="{lang_code}"')
    content = content.replace('Comment fonctionne le Market Pulse ? - Transparence Vylinkia', lang_data['title'])
    content = re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{lang_data["desc_meta"]}">', content)
    
    # Nav
    content = content.replace('Fonctionnalités', lang_data['nav_features'])
    content = content.replace('Tarifs', lang_data['nav_pricing'])
    content = content.replace('Contact', lang_data['nav_contact']) 
    content = content.replace("Télécharger l'App", lang_data['download_btn'])
    
    # STRICT Multi-line Replacements (Must match source file exactly)
    
    # Hero
    content = content.replace('''Ce n'est pas de la magie.<br>
            C'est du <span class="gradient-text">Traitement de Données</span>.''', lang_data['hero_title'])
            
    content = content.replace('''Le "Market Pulse" n'est pas une intuition. C'est un algorithme déterministe qui scanne
            <strong>13 paniers d'actifs</strong> en temps réel pour décider si le feu est Vert (Acheter) ou Rouge
            (Protéger).''', lang_data['hero_desc'])
            
    # Section 1
    content = content.replace('1. Les Capteurs (Input)', lang_data['sec1_title'])
    
    content = content.replace('''Notre algorithme ne regarde pas que le S&P 500. Il surveille la santé globale de l'économie à travers 13
                secteurs clés sur une fenêtre de 7 jours.''', lang_data['sec1_desc'])
    
    content = content.replace('⚠️ Actifs "Risque"', lang_data['group_risk_on'])
    content = content.replace('🛡️ Actifs "Refuge"', lang_data['group_risk_off'])
    content = content.replace('🌍 Contexte Global', lang_data['group_global'])
    
    # Items (One liners in source file)
    items_map = [
        ('💻 <strong>Tech (S&P/Nasdaq)</strong> : Le moteur de la croissance.', 'item_tech'),
        ('₿ <strong>Crypto</strong> (BTC/ETH) : L\'appétit spéculatif pur.', 'item_crypto'),
        ('🏦 <strong>Finance</strong> : La santé bancaire (Taux d\'intérêt).', 'item_finance'),
        ('🛢️ <strong>Énergie</strong> : L\'activité industrielle réelle.', 'item_energy'),
        ('🌏 <strong>Marchés Émergents</strong> : La croissance mondiale hors US.', 'item_emerging'),
        ('💎 <strong>Or & Métaux</strong> : La protection contre l\'inflation.', 'item_gold'),
        ('📜 <strong>Obligations (Bonds)</strong> : La fuite vers la sécurité (TLT).', 'item_bonds'),
        ('📉 <strong>Volatilité (VIX)</strong> : L\'indice de la peur.', 'item_vix'),
        ('💶 <strong>Euro / Dollar</strong> : Impact de change sur vos gains.', 'item_forex'),
        ('🇪🇺 <strong>Indices Europe</strong> : La santé de la zone Euro.', 'item_eu_indices'),
        ('🇨🇳 <strong>Asie / Chine</strong> : Indicateur avancé pour le Luxe.', 'item_asia'),
        ('🛢️ <strong>Brent Crude</strong> : Référence pétrole Europe.', 'item_brent'),
        ('🎈 <strong>Market Breadth</strong> : Participation (Tout monte ou seulement les géants ?).', 'item_breadth'),
    ]
    for fr, key in items_map:
        if key in lang_data:
            content = content.replace(fr, lang_data[key])
        else:
            # Fallback for items I didn't add to map above but are in lang_data (e.g. items)
            pass

    # Section 2
    content = content.replace('2. La Logique (Algorithme)', lang_data['sec2_title'])
    content = content.replace('Le Score de Sentiment Pondéré', lang_data['step1_title'])
    
    content = content.replace("L'IA calcule d'abord un score brut basé sur la performance (7 jours) de chaque secteur.", lang_data['step1_desc'])
    
    content = content.replace("Si le score est > 5, c'est généralement bon signe. Si < -5, attention.", lang_data['step1_sub'])
    
    content = content.replace('Les "Smart Alerts" (Exceptions Prioritaires)', lang_data['step2_title'])
    
    content = content.replace('''Avant d'écouter le score, l'algorithme vérifie des scénarios critiques qui annulent tout le
                            reste. C'est notre filet de sécurité.''', lang_data['step2_desc'])
    
    # Alerts
    content = content.replace('<span class="bg-red-500/20 text-red-400 p-1 rounded">🎈 Bulle</span>', f'<span class="bg-red-500/20 text-red-400 p-1 rounded">{lang_data["alert_bubble"]}</span>')
    content = content.replace('''Si la Tech monte fort (>2%) mais que le reste de l'économie
                                    baisse. = <strong>Danger</strong>.''', lang_data['alert_bubble_desc'])
    
    content = content.replace('<span class="bg-blue-500/20 text-blue-400 p-1 rounded">💨 Devise</span>', f'<span class="bg-blue-500/20 text-blue-400 p-1 rounded">{lang_data["alert_forex"]}</span>')
    content = content.replace('''Si le marché US monte mais que le Dollar s'effondre face à
                                    l'Euro. = <strong>Gains annulés pour vous</strong>.''', lang_data['alert_forex_desc'])
    
    content = content.replace('<span class="bg-purple-500/20 text-purple-400 p-1 rounded">🇨🇳 Luxe</span>', f'<span class="bg-purple-500/20 text-purple-400 p-1 rounded">{lang_data["alert_luxury"]}</span>')
    content = content.replace('''Si l'Asie décroche brutalement. = <strong>Alerte sur
                                        LVMH/Kering</strong>.''', lang_data['alert_luxury_desc'])
    
    # FAQ
    content = content.replace('Transparence Totale', lang_data['faq_title'])
    
    content = content.replace('Est-ce un "Trading Bot" automatisé ?', lang_data['q1'])
    content = content.replace('''<strong>Non.</strong> Vylinkia est un outil d'aide à la décision. L'IA fait le travail d'analyse
                        (qui prendrait 4h par jour à un humain) en millisecondes, mais c'est <strong>vous</strong> qui
                        validez et passez l'ordre. Nous ne gérons pas votre argent.''', lang_data['a1'])
    
    content = content.replace("D'où viennent les données ?", lang_data['q2'])
    content = content.replace('''Nous utilisons des flux de données boursières professionnels (Twelve Data & Yahoo Finance APIs)
                        agrégés en temps réel. Nos serveurs aux Pays-Bas recalculent le Market Pulse toutes les 4
                        heures.''', lang_data['a2'])
    
    content = content.replace('Pourquoi "7 jours" ?', lang_data['q3'])
    content = content.replace('''Nous sommes spécialisés dans le <strong>Swing Trading</strong>. La tendance hebdomadaire est la
                        plus pertinente pour filtrer le "bruit" quotidien tout en étant assez réactif pour ne pas rater
                        les opportunités.''', lang_data['a3'])
    
    content = content.replace('Télécharger l\'Assistant', lang_data['cta_btn'])
    
    # Footer
    content = content.replace('← Retour à l\'accueil', lang_data['footer_back'])
    content = content.replace('Politique de Confidentialité', lang_data['footer_privacy'])
    content = content.replace('Conditions d\'Utilisation', lang_data['footer_terms'])
    content = content.replace('href="index.html"', f'href="index.html"') 
    
    return content

# Execute
for lang_code, data in translations.items():
    print(f"Generating {lang_code}...")
    try:
        new_content = generate_file(lang_code, data)
        new_content = new_content.replace('href="assets/', 'href="../assets/')
        new_content = new_content.replace('src="assets/', 'src="../assets/')
        if 'href="privacy.html"' in new_content:
            new_content = new_content.replace('href="privacy.html"', 'href="../privacy.html"')
        if 'href="terms.html"' in new_content:
            new_content = new_content.replace('href="terms.html"', 'href="../terms.html"')
            
        target_dir = os.path.join(base_path, lang_code)
        target_file = os.path.join(target_dir, 'market-pulse.html')
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Saved {target_file}")
        
    except Exception as e:
        print(f"Error generating {lang_code}: {e}")

print("Done (v2).")
