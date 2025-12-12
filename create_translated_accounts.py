"""
Script pour créer les pages account.html traduites dans toutes les langues
"""

import os
import shutil

BASE_DIR = r"c:\Users\vpabs\TYTO\vylinkia-invest-website"

# Traductions pour chaque langue
TRANSLATIONS = {
    'de': {
        'title': 'Mein Konto - Vylinkia Invest',
        'heading': 'Mein Konto',
        'subtitle': 'Melden Sie sich an, um auf Ihr Profil zuzugreifen',
        'email_label': 'E-Mail',
        'password_label': 'Passwort',
        'login_button': 'Anmelden',
        'logout_button': 'Abmelden',
        'member_since': 'Mitglied seit',
        'signals_available': 'Verfügbare Signale',
        'premium_signals': 'Premium-Signale',
        'days_seniority': 'Tage Mitgliedschaft',
        'account_management': 'Kontoverwaltung',
        'change_password': 'Passwort ändern',
        'upgrade_premium': '⭐ Auf Premium upgraden',
        'manage_subscription': 'Abonnement verwalten',
        'premium_benefits': 'Premium-Vorteile',
        'unlimited_signals': 'Unbegrenzte Signale',
        'unlimited_signals_desc': 'Zugriff auf alle Kauf- und Verkaufssignale',
        'detailed_analysis': 'Detaillierte Analysen',
        'detailed_analysis_desc': 'Konfidenzscore, Stop Loss und Take Profit',
        'push_notifications': 'Push-Benachrichtigungen',
        'push_notifications_desc': 'Echtzeit-Benachrichtigungen auf Ihrem Handy',
        'priority_support': 'Prioritäts-Support',
        'priority_support_desc': 'Schnelle Antwort auf Ihre Fragen',
        'price_per_month': 'pro Monat • 7 Tage kostenlos',
        'password_modal_title': 'Passwort ändern',
        'current_password': 'Aktuelles Passwort',
        'new_password': 'Neues Passwort',
        'confirm_password': 'Neues Passwort bestätigen',
        'min_characters': 'Mindestens 6 Zeichen',
        'cancel': 'Abbrechen',
        'confirm': 'Bestätigen',
        'passwords_no_match': 'Die Passwörter stimmen nicht überein',
        'password_min_length': 'Das Passwort muss mindestens 6 Zeichen lang sein',
        'password_changed': 'Passwort erfolgreich geändert!',
        'wrong_password': 'Aktuelles Passwort falsch',
        'error_invalid_credential': 'E-Mail oder Passwort falsch',
        'error_invalid_email': 'Ungültige E-Mail-Adresse',
        'error_user_disabled': 'Dieses Konto wurde deaktiviert',
        'error_too_many_requests': 'Zu viele Versuche. Bitte versuchen Sie es später erneut',
        'error_network': 'Netzwerkfehler. Überprüfen Sie Ihre Internetverbindung',
        'error_default': 'Verbindungsfehler. Bitte versuchen Sie es erneut',
        'no_account_title': 'Noch kein Konto?',
        'no_account_text': 'Konten werden direkt in der mobilen App erstellt.',
        'download_app': 'App herunterladen',
        'no_account_cta': 'um mit der Vylinkia Vision zu investieren.',
        'back_home': 'Zurück zur Startseite',
    },
    'en': {
        'title': 'My Account - Vylinkia Invest',
        'heading': 'My Account',
        'subtitle': 'Sign in to access your profile',
        'email_label': 'Email',
        'password_label': 'Password',
        'login_button': 'Sign In',
        'logout_button': 'Sign Out',
        'member_since': 'Member since',
        'signals_available': 'Available Signals',
        'premium_signals': 'Premium Signals',
        'days_seniority': 'Days of Membership',
        'account_management': 'Account Management',
        'change_password': 'Change Password',
        'upgrade_premium': '⭐ Upgrade to Premium',
        'manage_subscription': 'Manage Subscription',
        'premium_benefits': 'Premium Benefits',
        'unlimited_signals': 'Unlimited Signals',
        'unlimited_signals_desc': 'Access to all buy and sell signals',
        'detailed_analysis': 'Detailed Analysis',
        'detailed_analysis_desc': 'Confidence score, Stop Loss and Take Profit',
        'push_notifications': 'Push Notifications',
        'push_notifications_desc': 'Real-time alerts on your mobile',
        'priority_support': 'Priority Support',
        'priority_support_desc': 'Quick response to your questions',
        'price_per_month': 'per month • 7 days free',
        'password_modal_title': 'Change Password',
        'current_password': 'Current Password',
        'new_password': 'New Password',
        'confirm_password': 'Confirm New Password',
        'min_characters': 'Minimum 6 characters',
        'cancel': 'Cancel',
        'confirm': 'Confirm',
        'passwords_no_match': 'Passwords do not match',
        'password_min_length': 'Password must be at least 6 characters',
        'password_changed': 'Password changed successfully!',
        'wrong_password': 'Current password incorrect',
        'error_invalid_credential': 'Email or password incorrect',
        'error_invalid_email': 'Invalid email address',
        'error_user_disabled': 'This account has been disabled',
        'error_too_many_requests': 'Too many attempts. Please try again later',
        'error_network': 'Network error. Check your internet connection',
        'error_default': 'Connection error. Please try again',
        'no_account_title': 'No account yet?',
        'no_account_text': 'Accounts are created directly in the mobile app.',
        'download_app': 'Download the app',
        'no_account_cta': 'to start investing with Vylinkia Vision.',
        'back_home': 'Back to Home',
    },
    'es': {
        'title': 'Mi Cuenta - Vylinkia Invest',
        'heading': 'Mi Cuenta',
        'subtitle': 'Inicia sesión para acceder a tu perfil',
        'email_label': 'Correo electrónico',
        'password_label': 'Contraseña',
        'login_button': 'Iniciar sesión',
        'logout_button': 'Cerrar sesión',
        'member_since': 'Miembro desde',
        'signals_available': 'Señales Disponibles',
        'premium_signals': 'Señales Premium',
        'days_seniority': 'Días de Antigüedad',
        'account_management': 'Gestión de Cuenta',
        'change_password': 'Cambiar Contraseña',
        'upgrade_premium': '⭐ Actualizar a Premium',
        'manage_subscription': 'Gestionar Suscripción',
        'premium_benefits': 'Beneficios Premium',
        'unlimited_signals': 'Señales Ilimitadas',
        'unlimited_signals_desc': 'Acceso a todas las señales de compra y venta',
        'detailed_analysis': 'Análisis Detallado',
        'detailed_analysis_desc': 'Puntuación de confianza, Stop Loss y Take Profit',
        'push_notifications': 'Notificaciones Push',
        'push_notifications_desc': 'Alertas en tiempo real en tu móvil',
        'priority_support': 'Soporte Prioritario',
        'priority_support_desc': 'Respuesta rápida a tus preguntas',
        'price_per_month': 'por mes • 7 días gratis',
        'password_modal_title': 'Cambiar Contraseña',
        'current_password': 'Contraseña Actual',
        'new_password': 'Nueva Contraseña',
        'confirm_password': 'Confirmar Nueva Contraseña',
        'min_characters': 'Mínimo 6 caracteres',
        'cancel': 'Cancelar',
        'confirm': 'Confirmar',
        'passwords_no_match': 'Las contraseñas no coinciden',
        'password_min_length': 'La contraseña debe tener al menos 6 caracteres',
        'password_changed': '¡Contraseña cambiada con éxito!',
        'wrong_password': 'Contraseña actual incorrecta',
        'error_invalid_credential': 'Correo o contraseña incorrectos',
        'error_invalid_email': 'Dirección de correo inválida',
        'error_user_disabled': 'Esta cuenta ha sido desactivada',
        'error_too_many_requests': 'Demasiados intentos. Inténtalo más tarde',
        'error_network': 'Error de red. Verifica tu conexión a internet',
        'error_default': 'Error de conexión. Inténtalo de nuevo',
        'no_account_title': '¿Aún no tienes cuenta?',
        'no_account_text': 'Las cuentas se crean directamente en la aplicación móvil.',
        'download_app': 'Descarga la app',
        'no_account_cta': 'para empezar a invertir con la Visión Vylinkia.',
        'back_home': 'Volver al Inicio',
    },
    'it': {
        'title': 'Il Mio Account - Vylinkia Invest',
        'heading': 'Il Mio Account',
        'subtitle': 'Accedi per accedere al tuo profilo',
        'email_label': 'Email',
        'password_label': 'Password',
        'login_button': 'Accedi',
        'logout_button': 'Esci',
        'member_since': 'Membro dal',
        'signals_available': 'Segnali Disponibili',
        'premium_signals': 'Segnali Premium',
        'days_seniority': 'Giorni di Anzianità',
        'account_management': 'Gestione Account',
        'change_password': 'Cambia Password',
        'upgrade_premium': '⭐ Passa a Premium',
        'manage_subscription': 'Gestisci Abbonamento',
        'premium_benefits': 'Vantaggi Premium',
        'unlimited_signals': 'Segnali Illimitati',
        'unlimited_signals_desc': 'Accesso a tutti i segnali di acquisto e vendita',
        'detailed_analysis': 'Analisi Dettagliata',
        'detailed_analysis_desc': 'Punteggio di confidenza, Stop Loss e Take Profit',
        'push_notifications': 'Notifiche Push',
        'push_notifications_desc': 'Avvisi in tempo reale sul tuo cellulare',
        'priority_support': 'Supporto Prioritario',
        'priority_support_desc': 'Risposta rapida alle tue domande',
        'price_per_month': 'al mese • 7 giorni gratis',
        'password_modal_title': 'Cambia Password',
        'current_password': 'Password Attuale',
        'new_password': 'Nuova Password',
        'confirm_password': 'Conferma Nuova Password',
        'min_characters': 'Minimo 6 caratteri',
        'cancel': 'Annulla',
        'confirm': 'Conferma',
        'passwords_no_match': 'Le password non corrispondono',
        'password_min_length': 'La password deve essere di almeno 6 caratteri',
        'password_changed': 'Password cambiata con successo!',
        'wrong_password': 'Password attuale errata',
        'error_invalid_credential': 'Email o password errati',
        'error_invalid_email': 'Indirizzo email non valido',
        'error_user_disabled': 'Questo account è stato disattivato',
        'error_too_many_requests': 'Troppi tentativi. Riprova più tardi',
        'error_network': 'Errore di rete. Controlla la tua connessione internet',
        'error_default': 'Errore di connessione. Riprova',
        'no_account_title': 'Non hai ancora un account?',
        'no_account_text': 'Gli account vengono creati direttamente nell\'app mobile.',
        'download_app': 'Scarica l\'app',
        'no_account_cta': 'per iniziare a investire con la Visione Vylinkia.',
        'back_home': 'Torna alla Home',
    }
}

def translate_account_page(lang_code, translations):
    """Crée une version traduite de account.html"""
    
    # Lire le fichier source (français)
    source_file = os.path.join(BASE_DIR, 'account.html')
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Appliquer les traductions
    content = content.replace('<html lang="fr">', f'<html lang="{lang_code}">')
    content = content.replace('<title>Mon Compte - Vylinkia Invest</title>', f'<title>{translations["title"]}</title>')
    content = content.replace('<h1 class="text-3xl font-bold mb-2 text-center">Mon Compte</h1>', 
                            f'<h1 class="text-3xl font-bold mb-2 text-center">{translations["heading"]}</h1>')
    content = content.replace('Connectez-vous pour accéder à votre profil', translations['subtitle'])
    content = content.replace('<label for="email" class="block text-sm font-medium text-slate-300 mb-2">Email</label>',
                            f'<label for="email" class="block text-sm font-medium text-slate-300 mb-2">{translations["email_label"]}</label>')
    content = content.replace('<label for="password" class="block text-sm font-medium text-slate-300 mb-2">Mot de passe</label>',
                            f'<label for="password" class="block text-sm font-medium text-slate-300 mb-2">{translations["password_label"]}</label>')
    content = content.replace('>Se connecter<', f'>{translations["login_button"]}<')
    content = content.replace('>Déconnexion<', f'>{translations["logout_button"]}<')
    content = content.replace('Membre depuis', translations['member_since'])
    content = content.replace('Signaux disponibles', translations['signals_available'])
    content = content.replace('Signaux premium', translations['premium_signals'])
    content = content.replace('Jours d\'ancienneté', translations['days_seniority'])
    content = content.replace('Gestion du compte', translations['account_management'])
    content = content.replace('>Changer le mot de passe<', f'>{translations["change_password"]}<')
    content = content.replace('>⭐ Passer à Premium<', f'>{translations["upgrade_premium"]}<')
    content = content.replace('>Gérer mon abonnement<', f'>{translations["manage_subscription"]}<')
    content = content.replace('Avantages Premium', translations['premium_benefits'])
    content = content.replace('Signaux illimités', translations['unlimited_signals'])
    content = content.replace('Accès à tous les signaux d\'achat et de vente', translations['unlimited_signals_desc'])
    content = content.replace('Analyses détaillées', translations['detailed_analysis'])
    content = content.replace('Score de confiance, Stop Loss et Take Profit', translations['detailed_analysis_desc'])
    content = content.replace('Notifications push', translations['push_notifications'])
    content = content.replace('Alertes en temps réel sur votre mobile', translations['push_notifications_desc'])
    content = content.replace('Support prioritaire', translations['priority_support'])
    content = content.replace('Réponse rapide à vos questions', translations['priority_support_desc'])
    content = content.replace('par mois • 7 jours gratuits', translations['price_per_month'])
    content = content.replace('<h2 class="text-2xl font-bold mb-6">Changer le mot de passe</h2>',
                            f'<h2 class="text-2xl font-bold mb-6">{translations["password_modal_title"]}</h2>')
    content = content.replace('Mot de passe actuel', translations['current_password'])
    content = content.replace('Nouveau mot de passe', translations['new_password'])
    content = content.replace('Confirmer le nouveau mot de passe', translations['confirm_password'])
    content = content.replace('Minimum 6 caractères', translations['min_characters'])
    content = content.replace('>Annuler<', f'>{translations["cancel"]}<')
    content = content.replace('>Confirmer<', f'>{translations["confirm"]}<')
    content = content.replace('Les mots de passe ne correspondent pas', translations['passwords_no_match'])
    content = content.replace('Le mot de passe doit contenir au moins 6 caractères', translations['password_min_length'])
    content = content.replace('Mot de passe modifié avec succès !', translations['password_changed'])
    content = content.replace('Mot de passe actuel incorrect', translations['wrong_password'])
    content = content.replace('Email ou mot de passe incorrect', translations['error_invalid_credential'])
    content = content.replace('Adresse email invalide', translations['error_invalid_email'])
    content = content.replace('Ce compte a été désactivé', translations['error_user_disabled'])
    content = content.replace('Trop de tentatives. Veuillez réessayer plus tard', translations['error_too_many_requests'])
    content = content.replace('Erreur de connexion réseau. Vérifiez votre connexion internet', translations['error_network'])
    content = content.replace('Erreur de connexion. Veuillez réessayer', translations['error_default'])
    content = content.replace('Pas encore de compte ?', translations['no_account_title'])
    content = content.replace('Les comptes se créent directement dans l\'application mobile.', translations['no_account_text'])
    content = content.replace('>Téléchargez l\'app<', f'>{translations["download_app"]}<')
    content = content.replace('pour commencer à investir avec la Vision Vylinkia.', translations['no_account_cta'])
    content = content.replace('Retour à l\'accueil', translations['back_home'])
    
    # Ajuster les liens
    content = content.replace('href="index.html', f'href="../index.html')
    content = content.replace('href="privacy.html', f'href="../privacy.html')
    
    # Créer le répertoire de langue s'il n'existe pas
    lang_dir = os.path.join(BASE_DIR, lang_code)
    os.makedirs(lang_dir, exist_ok=True)
    
    # Écrire le fichier traduit
    output_file = os.path.join(lang_dir, 'account.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {lang_code}/account.html créé")

def main():
    print("=" * 60)
    print("CRÉATION DES PAGES ACCOUNT TRADUITES")
    print("=" * 60)
    print()
    
    for lang_code, translations in TRANSLATIONS.items():
        try:
            translate_account_page(lang_code, translations)
        except Exception as e:
            print(f"❌ Erreur pour {lang_code}: {e}")
    
    print()
    print("=" * 60)
    print("TERMINÉ!")
    print("=" * 60)

if __name__ == '__main__':
    main()
