# Formation Usine Logicielle

## procédure de lancement de vm avec vagrant/virtualbox

* installer vagrant et reboot
* dans un powershell: `vagrant box add mlamamra/myusine`
* dans le dossier contenant le **Vagrantfile**: 
  - création / lancement : `vagrant up`
  - connexion sur la vm : `vagrant ssh`
  - arrêt de la vm : `vagrant halt`
  - destruciton de la vm : `vagrant destroy`

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

## customisations

* `git config --global core.editor`: utiliser un éditeur par défaut autre que Vi pour les non linuxiens
* `git config --global alias.xx yyyy`: remplacer yyyy par xx comme commade git
* édition du fichier `~/.bash_profile` pour charger auto. le .bashrc
* édition du fichier `~/.bashrc` pour créer des alias au niveau du git bash
   - ex: `alias gst='git status'` + `source ~/.bashrc` pour charger les alias

## les commandes d'inversion

* `git checkout [HEAD~n] -- file(s)` : plaquer l'état du dépôt pour un ou plusieurs fichier dans la copie de travail
   - inverser des modifs en cours
* `git rm [-r]`: suppression de la copie de travail + demande de suppresion du dépôt (au prochain commit).
   - `git rm --cached` pour demander la suppression sans supprimer de la copie
* `git reset -- file(s)`: pour désindéxer
* `git reset [HEAD~n] [--soft | | --hard]`: 
   - déplacement de head vers le commit en paramètre
   - suppression de l'historique des commits précédemment devant le nouveau HEAD
   - selon l'option, conservation ou écrasement de la copie et de l'index
   - attention: ne pas reset un commit déjà poussé
   - annuler un reset: regarder dans le reflog et git reset HEAD@{n}
* `git revert [HEAD~n] [--no-edit]`: inversion de commit par création du commit inverse
   - inversion d'un revert en conflit: `git reset HEAD --hard` pour virer les ajouts à l'index   

## les commandes d'inversion

* `git checkout [HEAD~n] -- file(s)` : plaquer l'état du dépôt pour un ou plusieurs fichier dans la copie de travail
   - inverser des modifs en cours
* `git rm [-r]`: suppression de la copie de travail + demande de suppresion du dépôt (au prochain commit).
   - `git rm --cached` pour demander la suppression sans supprimer de la copie
* `git reset -- file(s)`: pour désindéxer
* `git reset [HEAD~n] [--soft | | --hard]`: 
   - déplacement de head vers le commit en paramètre
   - suppression de l'historique des commits précédemment devant le nouveau HEAD
   - selon l'option, conservation ou écrasement de la copie et de l'index
   - attention: ne pas reset un commit déjà poussé
   - annuler un reset: regarder dans le reflog et git reset HEAD@{n}
* `git revert [HEAD~n] [--no-edit]`: inversion de commit par création du commit inverse
   - inversion d'un revert en conflit: `git reset HEAD --hard` pour virer les ajouts à l'index   


## dépôts distants

### commandes de base

* git clone <address>: copie d'un dépôt distant
* git remote add <repo> <address>: ajout d'un dépôt distant en local

### procédure de synchronisation

1. synchronisation ssh:
   - `ssh-jkeygen`
   - upload de la clé publique sur gitlab
   - config de la clé privé côté client
2. ajout dépôt: `git remote add <repo_name> <repo_address>`
3. pousser: `git push <repo_name> <branch_name>`
   - fixer le dépôt et la branche par défaut pour la branche locale avec **-u**


