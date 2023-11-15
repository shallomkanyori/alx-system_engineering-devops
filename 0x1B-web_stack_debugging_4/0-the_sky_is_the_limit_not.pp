# Fix nginx to have no failed requests while stress testing
exec {'fix-for-nginx':
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
