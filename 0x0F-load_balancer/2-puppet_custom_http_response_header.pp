# Installs and configures a Nginx server with custom header

# Install Nginx
package {'nginx':
  ensure   => installed,
  provider => 'apt',
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

  add_header X-Served-By $(hostname);
	
	location / {
		try_files \$uri \$uri/ =404;
	}
}
EOF
'

exec {'conf':
  command => $config_cmd,
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['nginx'],
}

# Nginx service
exec {'nginx_restart':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
  after   =>  Exec['conf'],
}
