# Formation Usine Logicielle

## procédure de lancement de vm avec vagrant/virtualbox

* installer vagrant et reboot
* dans un powershell: `vagrant box add mlamamra/myusine`
* dans le dossier contenant le **Vagrantfile**: 
  - création / lancement : `vagrant up`
  - connexion sur la vm : `vagrant ssh`
  - arrêt de la vm : `vagrant halt`
  - destruction de la vm : `vagrant destroy`

## points théoriques sur l'agilité

* réflexion sur le process de développement
* developpemet itératif, incrémental, et adaptatif
* cycles courts fixes + relation client quotidienne + collabaration quotidienne
* préservation de la qualité, orienté résultats
* auto-organisation

## points théoriques sur le DevOps

* mur de la confusion: stéréotypes dev vs stéréotypes ops
* Devops: extension de l'agilité au delà du développement
* aspect humain / social hérité de l'agilité
* aspect technique lié à l'automatisation, le monitoring et le LEAN management
  - CALMS
* design d'un pipeline de création de valeur à l'echelle de l'entreprise

## git: intro

1. `git init`:création dépôt
2. `git config --glbal user.name|email`: ajout métadonnées
3. `git add`: ajout index
4. `git commit`: validation dans le dépôt

## git: analyser l'historique

* `git log [-n] [-p] [--oneline]`: afficher l'historique
* `git show`: voir un commit
* pointeur HEAD: désigne le commit courant et/ou la branche
* pointeur de branche: désigne le commit courant 



