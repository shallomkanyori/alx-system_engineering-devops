# Installs and configures a Nginx server with custom header

# Install Nginx
package {'nginx':
  ensure   => installed,
  provider => 'apt',
}

# Landing page
file {'/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
  mode    => '0755',
}

# Nginx service
service {'nginx':
  ensure    => running,
  subscribe => Exec['default.conf'],
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
	
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=-BE6GyHcASE;
	}
	
	location / {
		try_files \$uri \$uri/ =404;
	}
}
EOF
'

exec {'default.conf':
  command => $config_cmd,
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['nginx'],
}
