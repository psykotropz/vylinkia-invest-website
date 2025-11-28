# Vylinkia Invest Website

Site vitrine pour l'application mobile Vylinkia Invest.

## Déploiement

Ce site est hébergé sur GitHub Pages.

### Prérequis

- Un compte GitHub
- Git installé sur votre machine

### Instructions de déploiement

1. Initialiser le dépôt git (si ce n'est pas déjà fait) :
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Créer un dépôt sur GitHub nommé `vylinkia-invest-website`.

3. Lier le dépôt local au dépôt distant :
   ```bash
   git remote add origin https://github.com/VOTRE_USERNAME/vylinkia-invest-website.git
   git branch -M main
   git push -u origin main
   ```

4. Activer GitHub Pages :
   - Allez dans les paramètres du dépôt sur GitHub.
   - Section "Pages".
   - Source : `main` branch.
   - Save.

5. Domaine personnalisé (Optionnel) :
   - Le fichier `CNAME` est déjà présent avec le domaine `vylinkia-invest.com`.
   - Configurez vos enregistrements DNS chez votre registrar pour pointer vers GitHub Pages.
Cela créera automatiquement un fichier `CNAME` ici.
