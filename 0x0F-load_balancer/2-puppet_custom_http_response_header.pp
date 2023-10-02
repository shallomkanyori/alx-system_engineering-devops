# Installs and configures a Nginx server with custom header

# Update
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['nginx'],
}

# Install Nginx
exec {'nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['conf'],
}

# Configure server
$config_cmd = 'cat << EOF > /etc/nginx/sites-available/default
# Defualt server configuration
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	
	server_name _;

  add_header X-Served-By $HOSTNAME;
	
	location / {
		try_files \$uri \$uri/ =404;
	}
}
EOF
'

exec {'conf':
  command  => $config_cmd,
  provider => shell,
  before   => Exec['nginx_restart'],
}

# Nginx service
exec {'nginx_restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
