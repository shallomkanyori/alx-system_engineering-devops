## Web server

#### Task 0
[0-transfer_file](0-transfer_file) is a script that transfers a local file to a server.
Requirements:
- Accepts 4 parameters
	1. The path to the file to be transferred
	2. The IP of the server to transfer the file to
	3. The username `scp` connects with
	4. The path to the SSH private key that `scp` uses
- Displays `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 4 parameters passed
- `scp` transfers the file to the user home directory `~/`
- Strict host key checking is disabled when using `scp`

#### Task 1
[1-install_nginx_web_server](1-install_nginx_web_server) is a script that installs and configures a web server to respect the requirements below.
Requirements:
- Install nginx on your `web-01` server
- Nginx listening on port 80
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it returns a page that contains the string `Hello World!`
- Does not use `systemctl` for restarting `nginx`

#### Task 2
[2-setup_a_domain_name](2-setup_a_domain_name) contains the domain name provided by .TECH Domains
Requirements:
- Contains only the domain name
- DNS records configure with an A entry pointing the root domain to the server's IP address

#### Task 3
[3-redirection](3-redirection) builds on [1-install_nginx_web_server](1-install_nginx_web_server) by configuring the Nginx server so that `/redirect_me` is redirecting to another page.
Requirements:
- The redirection must be a “301 Moved Permanently”

#### Task 4
[4-not_found_page_404](4-not_found_page_404) builds on [3-redirection](3-redirection) by congifuering the Nginx server to have a custom 404 page.
Requirements:
- The page returns an HTTP 404 error code
- The page contains the string `Ceci n'est pas une page`

#### Task 5
[7-puppet_install_nginx_web_server.pp](7-puppet_install_nginx_web_server.pp) is a Puppet manifest that installs and configures an Nginx server.
Requirements:
- Nginx is configured to listen on port `80`
- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it returns a page that contains the string `Hello World!`
- Querying `/redirect_me` performs a “301 Moved Permanently” redirect
