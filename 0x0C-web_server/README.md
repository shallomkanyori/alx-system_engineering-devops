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
