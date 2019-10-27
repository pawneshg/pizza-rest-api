# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false
  config.vm.box_version = "~> 20190314.0.0"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer

    sudo apt-get update
    sudo locale-gen en_US.UTF-8
    sudo update-locale LANG=en_US.UTF-8
    sudo apt-get install -y python3-venv zip python-pip python-dev libpq-dev
    # sudo apt-get install -y  postgresql postgresql-contrib
    # # Create the user to access the db. (vagrant sample)
    # sudo -u postgres psql -c "CREATE USER vagrant WITH SUPERUSER CREATEDB ENCRYPTED PASSWORD 'vagrant'"
    # # Change the port
    # sudo sed -i "s/port = 5433/port = 5432/" /etc/postgresql/10/main/postgresql.conf
    # # Restart de DB
    # sudo /etc/init.d/postgresql restart
    ## If you get a locale error follow those instructions

    # error message: PG::InvalidParameterValue: ERROR: encoding "UTF8" does not match locale "en_US"

    # generate the locales
    # sudo locale-gen en_US.UTF-8
    # sudo update-locale LANG=en_US.UTF-8
    #
    # # drop and recreate the default cluster
    # sudo pg_dropcluster --stop 10 main
    # sudo pg_createcluster --start -e UTF-8 10 main

    # recreate our database user
    #sudo -u postgres psql -c "CREATE USER vagrant WITH SUPERUSER CREATEDB ENCRYPTED PASSWORD 'vagrant'"
    # sleep 5
    # psql postgres -c "CREATE DATABASE ORDERS WITH ENCODING 'UTF8'"



    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
    # source /home/vagrant/.bash_aliases
    # cd /vagrant
    # python -m venv ~/env
    # source ~/env/bin/activate
    # pip install wheel
    # pip install -r requirements.txt
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py runserver 0.0.0.0:8000
    SHELL
end
