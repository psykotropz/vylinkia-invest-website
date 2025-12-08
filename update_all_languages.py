"""
Update all language versions of the website with new sections
"""
import re

def insert_section_after_header(content, new_section):
    """Insert new section after </header> tag"""
    pattern = r'(</header>\s*)'
    replacement = r'\1\n' + new_section + '\n'
    return re.sub(pattern, replacement, content, count=1)

def insert_section_before_contact(content, new_section):
    """Insert new section before Contact Section"""
    pattern = r'(\s*<!-- Contact Section -->)'
    replacement = '\n' + new_section + r'\1'
    return re.sub(pattern, replacement, content, count=1)

# Process each language
languages = {
    'en': {
        'how_title': 'How does it work?',
        'how_subtitle': 'Start investing smartly in 4 simple steps',
        'step1_title': 'Download & Create your account',
        'step1_desc': 'Download the app on Android (iOS coming soon) and create your account in 30 seconds',
        'step2_title': 'Discover your Alerts',
        'step2_desc': 'Check the daily alerts feed with the Vylinkia Confidence Score (0-100%) and Market Pulse',
        'step3_title': 'Analyze in detail',
        'step3_desc': 'Click on a signal to see the full analysis: trigger, market context, Stop Loss and Take Profit',
        'step4_title': 'Add to your Watchlist',
        'step4_desc': 'Mark your favorite signals and track them in your personal Watchlist with push notifications',
        'faq_title': 'Frequently Asked Questions',
        'faq_subtitle': 'Everything you need to know about Vylinkia Invest',
        'q1': 'Is it suitable for beginners?',
        'a1': 'Absolutely! Vylinkia Invest is designed to be simple and accessible. Our Confidence Score guides you in every decision, and the intuitive interface allows you to quickly understand the signals.',
        'q2': 'What assets are covered?',
        'a2': 'We cover European stocks (CAC40, DAX), American stocks (S&P 500, NASDAQ), as well as ETFs and major cryptocurrencies. Our focus is on assets accessible via PEA for European investors.',
        'q3': 'Can I cancel anytime?',
        'a3': 'Yes, the subscription is commitment-free. You can cancel anytime from the app settings. Enjoy a 7-day free trial to test the service.',
        'q4': 'How does the Confidence Score work?',
        'a4': "The Vylinkia Confidence Score (0-100%) evaluates the probability of success of a signal by analyzing thousands of data points: technical indicators, market context, volatility, and historical trends. The higher the score, the stronger the AI's conviction.",
    },
    'es': {
        'how_title': '¿Cómo funciona?',
        'how_subtitle': 'Comienza a invertir inteligentemente en 4 sencillos pasos',
        'step1_title': 'Descarga y Crea tu cuenta',
        'step1_desc': 'Descarga la app en Android (próximamente iOS) y crea tu cuenta en 30 segundos',
        'step2_title': 'Descubre tus Alertas',
        'step2_desc': 'Consulta el flujo de alertas diarias con el Puntaje de Confianza Vylinkia (0-100%) y el Market Pulse',
        'step3_title': 'Analiza en detalle',
        'step3_desc': 'Haz clic en una señal para ver el análisis completo: desencadenante, contexto de mercado, Stop Loss y Take Profit',
        'step4_title': 'Añade a tu Watchlist',
        'step4_desc': 'Marca tus señales favoritas y síguelas en tu Watchlist personal con notificaciones push',
        'faq_title': 'Preguntas Frecuentes',
        'faq_subtitle': 'Todo lo que necesitas saber sobre Vylinkia Invest',
        'q1': '¿Es adecuado para principiantes?',
        'a1': '¡Absolutamente! Vylinkia Invest está diseñado para ser simple y accesible. Nuestro Puntaje de Confianza te guía en cada decisión, y la interfaz intuitiva te permite comprender rápidamente las señales.',
        'q2': '¿Qué activos están cubiertos?',
        'a2': 'Cubrimos acciones europeas (CAC40, DAX), acciones americanas (S&P 500, NASDAQ), así como ETFs y criptomonedas principales. Nuestro enfoque está en activos accesibles a través de PEA para inversores europeos.',
        'q3': '¿Puedo cancelar en cualquier momento?',
        'a3': 'Sí, la suscripción es sin compromiso. Puedes cancelar en cualquier momento desde la configuración de la aplicación. Disfruta de 7 días de prueba gratuita para probar el servicio.',
        'q4': '¿Cómo funciona el Puntaje de Confianza?',
        'a4': 'El Puntaje de Confianza Vylinkia (0-100%) evalúa la probabilidad de éxito de una señal analizando miles de puntos de datos: indicadores técnicos, contexto de mercado, volatilidad y tendencias históricas. Cuanto mayor sea el puntaje, mayor será la convicción de la IA.',
    },
    'de': {
        'how_title': 'Wie funktioniert es?',
        'how_subtitle': 'Beginnen Sie in 4 einfachen Schritten intelligent zu investieren',
        'step1_title': 'Herunterladen & Konto erstellen',
        'step1_desc': 'Laden Sie die App auf Android herunter (iOS demnächst) und erstellen Sie Ihr Konto in 30 Sekunden',
        'step2_title': 'Entdecken Sie Ihre Warnungen',
        'step2_desc': 'Überprüfen Sie den täglichen Warnungs-Feed mit dem Vylinkia Confidence Score (0-100%) und Market Pulse',
        'step3_title': 'Detailliert analysieren',
        'step3_desc': 'Klicken Sie auf ein Signal, um die vollständige Analyse zu sehen: Auslöser, Marktkontext, Stop Loss und Take Profit',
        'step4_title': 'Zur Watchlist hinzufügen',
        'step4_desc': 'Markieren Sie Ihre Lieblingssignale und verfolgen Sie sie in Ihrer persönlichen Watchlist mit Push-Benachrichtigungen',
        'faq_title': 'Häufig gestellte Fragen',
        'faq_subtitle': 'Alles, was Sie über Vylinkia Invest wissen müssen',
        'q1': 'Ist es für Anfänger geeignet?',
        'a1': 'Absolut! Vylinkia Invest ist so konzipiert, dass es einfach und zugänglich ist. Unser Confidence Score führt Sie bei jeder Entscheidung, und die intuitive Benutzeroberfläche ermöglicht es Ihnen, die Signale schnell zu verstehen.',
        'q2': 'Welche Vermögenswerte werden abgedeckt?',
        'a2': 'Wir decken europäische Aktien (CAC40, DAX), amerikanische Aktien (S&P 500, NASDAQ) sowie ETFs und wichtige Kryptowährungen ab. Unser Fokus liegt auf Vermögenswerten, die über PEA für europäische Anleger zugänglich sind.',
        'q3': 'Kann ich jederzeit kündigen?',
        'a3': 'Ja, das Abonnement ist unverbindlich. Sie können jederzeit über die App-Einstellungen kündigen. Genießen Sie eine 7-tägige kostenlose Testversion, um den Service zu testen.',
        'q4': 'Wie funktioniert der Confidence Score?',
        'a4': 'Der Vylinkia Confidence Score (0-100%) bewertet die Erfolgswahrscheinlichkeit eines Signals, indem er Tausende von Datenpunkten analysiert: technische Indikatoren, Marktkontext, Volatilität und historische Trends. Je höher der Score, desto stärker ist die Überzeugung der KI.',
    },
    'it': {
        'how_title': 'Come funziona?',
        'how_subtitle': 'Inizia a investire in modo intelligente in 4 semplici passaggi',
        'step1_title': 'Scarica e Crea il tuo account',
        'step1_desc': "Scarica l'app su Android (iOS in arrivo) e crea il tuo account in 30 secondi",
        'step2_title': 'Scopri i tuoi Avvisi',
        'step2_desc': 'Consulta il feed di avvisi giornalieri con il Punteggio di Confidenza Vylinkia (0-100%) e il Market Pulse',
        'step3_title': 'Analizza in dettaglio',
        'step3_desc': "Fai clic su un segnale per vedere l'analisi completa: trigger, contesto di mercato, Stop Loss e Take Profit",
        'step4_title': 'Aggiungi alla tua Watchlist',
        'step4_desc': 'Segna i tuoi segnali preferiti e seguili nella tua Watchlist personale con notifiche push',
        'faq_title': 'Domande Frequenti',
        'faq_subtitle': 'Tutto ciò che devi sapere su Vylinkia Invest',
        'q1': 'È adatto ai principianti?',
        'a1': "Assolutamente! Vylinkia Invest è progettato per essere semplice e accessibile. Il nostro Punteggio di Confidenza ti guida in ogni decisione e l'interfaccia intuitiva ti permette di comprendere rapidamente i segnali.",
        'q2': 'Quali asset sono coperti?',
        'a2': 'Copriamo azioni europee (CAC40, DAX), azioni americane (S&P 500, NASDAQ), nonché ETF e principali criptovalute. Il nostro focus è sugli asset accessibili tramite PEA per gli investitori europei.',
        'q3': 'Posso cancellare in qualsiasi momento?',
        'a3': "Sì, l'abbonamento è senza impegno. Puoi cancellare in qualsiasi momento dalle impostazioni dell'app. Goditi una prova gratuita di 7 giorni per testare il servizio.",
        'q4': 'Come funziona il Punteggio di Confidenza?',
        'a4': "Il Punteggio di Confidenza Vylinkia (0-100%) valuta la probabilità di successo di un segnale analizzando migliaia di punti dati: indicatori tecnici, contesto di mercato, volatilità e tendenze storiche. Più alto è il punteggio, più forte è la convinzione dell'IA.",
    }
}

def generate_how_it_works_html(lang_data):
    return f'''    <!-- How it Works Section -->
    <section class="py-20">
        <div class="container mx-auto px-6">
            <h2 class="text-3xl font-bold text-center mb-4">{lang_data['how_title']}</h2>
            <p class="text-center text-slate-400 mb-16 max-w-2xl mx-auto">
                {lang_data['how_subtitle']}
            </p>
            <div class="grid md:grid-cols-4 gap-8">
                <!-- Step 1 -->
                <div class="text-center">
                    <div class="bg-slate-800 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 text-4xl border-2 border-green-500">
                        📱
                    </div>
                    <div class="bg-green-500 text-slate-900 text-xs font-bold px-3 py-1 rounded-full inline-block mb-3">
                        STEP 1
                    </div>
                    <h3 class="text-lg font-bold mb-3">{lang_data['step1_title']}</h3>
                    <p class="text-slate-400 text-sm">
                        {lang_data['step1_desc']}
                    </p>
                </div>

                <!-- Step 2 -->
                <div class="text-center">
                    <div class="bg-slate-800 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 text-4xl border-2 border-green-500">
                        🔔
                    </div>
                    <div class="bg-green-500 text-slate-900 text-xs font-bold px-3 py-1 rounded-full inline-block mb-3">
                        STEP 2
                    </div>
                    <h3 class="text-lg font-bold mb-3">{lang_data['step2_title']}</h3>
                    <p class="text-slate-400 text-sm">
                        {lang_data['step2_desc']}
                    </p>
                </div>

                <!-- Step 3 -->
                <div class="text-center">
                    <div class="bg-slate-800 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 text-4xl border-2 border-green-500">
                        🧠
                    </div>
                    <div class="bg-green-500 text-slate-900 text-xs font-bold px-3 py-1 rounded-full inline-block mb-3">
                        STEP 3
                    </div>
                    <h3 class="text-lg font-bold mb-3">{lang_data['step3_title']}</h3>
                    <p class="text-slate-400 text-sm">
                        {lang_data['step3_desc']}
                    </p>
                </div>

                <!-- Step 4 -->
                <div class="text-center">
                    <div class="bg-slate-800 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 text-4xl border-2 border-green-500">
                        ⭐
                    </div>
                    <div class="bg-green-500 text-slate-900 text-xs font-bold px-3 py-1 rounded-full inline-block mb-3">
                        STEP 4
                    </div>
                    <h3 class="text-lg font-bold mb-3">{lang_data['step4_title']}</h3>
                    <p class="text-slate-400 text-sm">
                        {lang_data['step4_desc']}
                    </p>
                </div>
            </div>
        </div>
    </section>

'''

def generate_faq_html(lang_data):
    return f'''    <!-- FAQ Section -->
    <section class="bg-slate-800 py-20">
        <div class="container mx-auto px-6 max-w-3xl">
            <h2 class="text-3xl font-bold text-center mb-4">{lang_data['faq_title']}</h2>
            <p class="text-center text-slate-400 mb-12">{lang_data['faq_subtitle']}</p>
            
            <div class="space-y-4">
                <!-- FAQ 1 -->
                <details class="bg-slate-700 rounded-xl p-6 cursor-pointer group">
                    <summary class="font-bold text-lg flex justify-between items-center">
                        {lang_data['q1']}
                        <span class="text-green-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p class="text-slate-400 mt-4">
                        {lang_data['a1']}
                    </p>
                </details>

                <!-- FAQ 2 -->
                <details class="bg-slate-700 rounded-xl p-6 cursor-pointer group">
                    <summary class="font-bold text-lg flex justify-between items-center">
                        {lang_data['q2']}
                        <span class="text-green-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p class="text-slate-400 mt-4">
                        {lang_data['a2']}
                    </p>
                </details>

                <!-- FAQ 3 -->
                <details class="bg-slate-700 rounded-xl p-6 cursor-pointer group">
                    <summary class="font-bold text-lg flex justify-between items-center">
                        {lang_data['q3']}
                        <span class="text-green-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p class="text-slate-400 mt-4">
                        {lang_data['a3']}
                    </p>
                </details>

                <!-- FAQ 4 -->
                <details class="bg-slate-700 rounded-xl p-6 cursor-pointer group">
                    <summary class="font-bold text-lg flex justify-between items-center">
                        {lang_data['q4']}
                        <span class="text-green-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p class="text-slate-400 mt-4">
                        {lang_data['a4']}
                    </p>
                </details>
            </div>
        </div>
    </section>

'''

# Process each language
for lang_code, lang_data in languages.items():
    print(f"Processing {lang_code.upper()}...")
    
    # Read the original file
    file_path = f'{lang_code}/index.html' if lang_code != 'fr' else 'index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate sections
    how_it_works_html = generate_how_it_works_html(lang_data)
    faq_html = generate_faq_html(lang_data)
    
    # Insert sections
    content = insert_section_after_header(content, how_it_works_html)
    content = insert_section_before_contact(content, faq_html)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {lang_code.upper()} updated successfully")

print("\n✅ All language versions updated!")
