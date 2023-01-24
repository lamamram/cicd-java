# Formation Usine Logicielle

## procédure de lancement de vm avec vagrant/virtualbox

* installer vagrant et reboot
* dans un powershell: `vagrant box add mlamamra/myusine`
* dans le dossier contenant le **Vagrantfile**: 
  - création / lancement : `vagrant up`
  - connexion sur la vm : `vagrant ssh`
  - arrêt de la vm : `vagrant halt`
  - destruciton de la vm : `vagrant destroy`