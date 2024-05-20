## Toute commande doit-ere exécution dans le répertoire contenant le Dockerfile
# vagrant up
# vagrant halt
# vagrant destroy
# vagrant global-config
#----------------------
# vagrant ssh [NAME|ID]
# access-token: myusine xYph6TpAt1yJ1hJiS3QN
Vagrant.configure(2) do |config|

  [
    ["gitlab.myusine.fr", "8192", "4", "mlamamra/myusine"],
  ].each do |vmname,mem,cpu,os|
    config.vm.define "#{vmname}" do |machine|

      machine.vm.provider "virtualbox" do |v|
        v.memory = "#{mem}"
        v.cpus = "#{cpu}"
        v.name = "#{vmname}"
       
      end
      machine.vm.box = "#{os}"
      machine.vm.hostname = "#{vmname}"
      machine.vm.network "public_network"
      machine.ssh.insert_key = false
    end
  end
end

