# Change OS open file limit configuration for the user holberton
exec {'change-os-configuration-for-holberton-user':
  command  => 'sudo sed -i "s/\(holberton[^0-9]*\)[0-9]*/\11000/" /etc/security/limits.conf && sysctl -p',
  provider => shell,
}
