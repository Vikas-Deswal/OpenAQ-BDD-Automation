Vagrant.configure("2") do |config|
  config.vm.box = "spox/ubuntu-arm"
  config.vm.box_version = "1.0.0"
  config.vm.network "private_network", ip: "192.168.56.11"

  config.vm.provider "vmware_desktop" do |vmware|
    vmware.memory = "2048"
    vmware.cpus = 2
  end

  # Provisioning
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update -y
    sudo apt-get install -y git python3 python3-pip python3-behave

    # Clone your repo
    # --- Clone the repo if not already cloned ---
    if [ ! -d "/home/vagrant/openaq" ]; then
      echo "Cloning Repository OpenAQ"
      git clone https://github.com/Vikas-Deswal/OpenAQ-BDD-Automation.git /home/vagrant/openaq
    else
      echo "Repository already exists, skipping clone"
    fi

  # --- Navigate and install requirements ---
  cd /home/vagrant/openaq || exit 1
  echo "Installing Python dependencies"
  pip3 install -r requirements.txt
  SHELL
end