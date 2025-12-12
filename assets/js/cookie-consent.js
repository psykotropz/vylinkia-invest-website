// Cookie Consent Management for Vylinkia Invest
// GDPR Compliant Cookie Banner with Google Analytics 4 Integration

// Load Google Analytics 4 if consent is given
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

// Accept cookies
function acceptCookies() {
    localStorage.setItem('cookieConsent', 'accepted');
    hideCookieBanner();
    loadGoogleAnalytics();
    // Reload to ensure GA4 starts tracking
    window.location.reload();
}

// Decline cookies
function declineCookies() {
    localStorage.setItem('cookieConsent', 'declined');
    hideCookieBanner();
}

// Hide cookie banner with animation
function hideCookieBanner() {
    const banner = document.getElementById('cookieConsent');
    if (banner) {
        banner.classList.remove('show');
        setTimeout(() => {
            banner.classList.add('hidden');
        }, 400);
    }
}

// Show cookie banner with animation
function showCookieBanner() {
    const banner = document.getElementById('cookieConsent');
    if (banner) {
        banner.classList.remove('hidden');
        setTimeout(() => {
            banner.classList.add('show');
        }, 100);
    }
}

// Initialize cookie consent on page load
document.addEventListener('DOMContentLoaded', function () {
    const consent = localStorage.getItem('cookieConsent');
    if (!consent) {
        showCookieBanner();
    }
});

// Load GA4 immediately if consent already given
loadGoogleAnalytics();
