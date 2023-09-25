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
