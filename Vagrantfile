Vagrant.configure("2") do |config|
  config.vm.box = "spox/ubuntu-arm"
  config.vm.box_version = "1.0.0"
  config.vm.network "private_network", ip: "192.168.56.11"

  config.vm.provider "vmware_desktop" do |vmware|
    vmware.memory = "2048"
    vmware.cpus = 2
  end

    # Sync allure-report folder to access reports on macOS
  config.vm.synced_folder "./reports", "/home/vagrant/openaq/allure-report",
  create: true,
  owner: "vagrant",
  group: "vagrant"

  # Provisioning
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update -y
    sudo apt-get install -y git python3 python3-pip python3-venv curl default-jre

    # Clone your repo
    # --- Clone the repo if not already cloned ---
    if [ ! -d "/home/vagrant/openaq" ]; then
      echo "Cloning Repository OpenAQ"
      git clone https://github.com/Vikas-Deswal/OpenAQ-BDD-Automation.git /home/vagrant/openaq
    else
      echo "Repository already exists, skipping clone"
    fi
    echo "=== Installing Allure CLI ==="
    # Install Allure for test reporting
    curl -o allure-2.24.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
    sudo tar -zxvf allure-2.24.0.tgz -C /opt/
    sudo ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure
    rm allure-2.24.0.tgz

    echo "-- Setting up Python environment --"
    # --- Navigate and install requirements ---
    cd /home/vagrant/openaq || exit 1
    echo "Installing Python dependencies"
    sudo -u vagrant pip3 install -r requirements.txt
    sudo chown -R vagrant:vagrant /home/vagrant/openaq  

    echo "-- Setting up environment configuration --"
    echo "Please run the following commands to set up environment variables:"
     # Add environment variables to .bashrc if not already present
    if ! grep -q "OPENAQ_BASE_URL" /home/vagrant/.bashrc; then
      echo "" >> /home/vagrant/.bashrc
      echo "# OpenAQ API Configuration" >> /home/vagrant/.bashrc
      echo "export OPENAQ_API_KEY=your_api_key" >> /home/vagrant/.bashrc
      echo "export OPENAQ_BASE_URL=https://api.openaq.org/v3" >> /home/vagrant/.bashrc
      echo "source /home/vagrant/.bashrc"
    fi

    echo "== Running the tests =="
    echo "Please run the following commands to run the tests after you have set the environment variables:"
    echo "cd /home/vagrant/openaq"
    echo "behave -f allure_behave.formatter:AllureFormatter -o allure-results"
    echo "allure generate allure-results -o allure-report --clean"
  SHELL
end