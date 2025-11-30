{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.mysql80
    pkgs.ngrok
  ];

  # https://devenv.sh/scripts/
  scripts.hello.exec = ''
    echo hello from $GREET
  '';

  enterShell = ''
    echo "Flask MySQL Todo App Development Environment"
    echo "Python: $(python3 --version)"
    echo "MySQL: $(mysql --version 2>/dev/null || echo 'MySQL available')"
    echo "ngrok: $(ngrok version 2>/dev/null || echo 'ngrok available')"
    echo ""
    echo "To start MySQL: devenv up"
    echo "To run the app: python app.py"
    echo "To expose with ngrok: ngrok http 5000"
  '';

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.11";
    venv.enable = true;
    venv.requirements = ./requirements.txt;
  };

  # https://devenv.sh/services/
  services.mysql = {
    enable = true;
    package = pkgs.mysql80;
    initialDatabases = [
      { name = "todoapp"; }
    ];
    initialScript = ''
      CREATE USER IF NOT EXISTS 'todoapp'@'localhost' IDENTIFIED BY 'todoapp';
      GRANT ALL PRIVILEGES ON todoapp.* TO 'todoapp'@'localhost';
      FLUSH PRIVILEGES;
    '';
    settings = {
      mysqld = {
        bind-address = "127.0.0.1";
        port = 3306;
      };
    };
  };

  # https://devenv.sh/tasks/
  tasks = {
    setup.exec = ''
      echo "Setting up the development environment..."
      pip install -r requirements.txt
      echo "Setup complete!"
    '';
    run.exec = ''
      python app.py
    '';
    ngrok.exec = ''
      ngrok http 5000
    '';
  };

  # Environment variables
  env.MYSQL_HOST = "127.0.0.1";
  env.MYSQL_PORT = "3306";
  env.MYSQL_USER = "todoapp";
  env.MYSQL_PASSWORD = "todoapp";
  env.MYSQL_DATABASE = "todoapp";
  env.FLASK_APP = "app.py";
  env.FLASK_ENV = "development";
}

