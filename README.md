# ✦ Les Archives des Veilles ✦

### Bibliothèque numérique des explorations

**Les Archives des Veilles** est une bibliothèque documentaire et visuelle réunissant des infographies créées à partir de séances d'hypnose.

Chaque archive présente les perceptions, récits et hypothèses abordés au cours d'une exploration, sous forme de résumés, d'illustrations et de synthèses visuelles.

Les contenus reflètent des expériences et interprétations subjectives et ne constituent pas des faits établis.

## 🌐 Accéder à la bibliothèque

**Bibliothèque :** https://lesarchivesdesveilles.fr/

Chaque exploration dispose de sa propre fiche documentaire, accessible depuis la bibliothèque.

## ✨ Fonctionnalités

- Bibliothèque visuelle présentant les explorations sous forme de couvertures illustrées.
- Recherche instantanée par titre, sous-titre et numéro d'archive.
- Pagination automatique des archives, avec 24 couvertures par page.
- Pages documentaires individuelles générées dynamiquement à partir du fichier `archives.json`.
- Présentation des résumés avec possibilité de déplier le récit complet.
- Prise en charge de deux formats : archives à plusieurs planches et archives à synthèse unique.
- Affichage de trois infographies d'aperçu pour les archives documentaires.
- Visionneuse interactive permettant de parcourir l'ensemble des planches.
- Agrandissement et zoom des illustrations.
- Affichage des infographies de synthèse.
- Chargement des illustrations complètes depuis Google Drive.
- Interface responsive adaptée aux ordinateurs, tablettes et smartphones.

## 📚 Organisation des archives

Chaque exploration est identifiée par un numéro unique.

La bibliothèque utilise le fichier `archives.json` pour associer à chaque numéro :

- Un titre et, éventuellement, un sous-titre.
- Un résumé documentaire.
- Une couverture et un bandeau illustrés.
- Un format de présentation adapté à l'exploration.
- Un lien vers la visionneuse lorsque celle-ci est nécessaire.
- Des informations complémentaires et des sources éventuelles.

Les couvertures et miniatures optimisées sont hébergées sur GitHub Pages.

Les infographies complètes et les synthèses sont hébergées sur Google Drive, dans des dossiers propres à chaque exploration.

## 🐍 Assistant de publication

Un assistant local développé en **Python**, utilisant Tkinter et Pillow, facilite la préparation des nouvelles archives.

Il permet notamment :

- De sélectionner le format de publication : planches et synthèse, ou synthèse seule.
- De convertir automatiquement les illustrations au format WebP.
- De préparer les couvertures, bandeaux et miniatures optimisées.
- De générer les fragments JSON nécessaires au site et à la visionneuse.
- De contrôler la présentation des paragraphes du résumé avant publication.
- De préparer des dossiers distincts pour GitHub et Google Drive.

L'assistant ne publie pas directement les fichiers en ligne : leur mise en ligne reste effectuée manuellement.

## 🛠️ Technologies

**HTML5 · CSS3 · JavaScript · JSON · Python · Pillow · Tkinter · GitHub Pages · Google Drive API**

Le site fonctionne sans serveur applicatif ni base de données traditionnelle.

## 🎨 Identité visuelle

Une interface sombre aux nuances prune, accompagnée de teintes dorées et de typographies élégantes, conçue pour offrir une lecture confortable et une expérience immersive.

Chaque exploration conserve sa propre direction artistique dans les illustrations qui l'accompagnent.

## 🔮 Évolutions envisagées

- Enrichissement progressif de la bibliothèque.
- Intégration des premières explorations au format synthèse unique.
- Classement thématique des archives.
- Amélioration progressive des outils de publication et de gestion documentaire.

---

© 2026 Les Archives des Veilles.
