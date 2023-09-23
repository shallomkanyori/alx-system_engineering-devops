## SSH

#### Task 1
[0-use_a_private_key](0-use_a_private_key) is a Bash script that uses `ssh` to connect to the ALX server `52.3.241.19` using the private key `~/.ssh/school` with the user `ubuntu`.
Requirements:
- Only uses `ssh` single-character flags
- Does not use `-l`
- Does not handle the case of a private key protected by a passphrase

#### Task 2
[1-create_ssh_key_pair](1-create_ssh_key_pair) is a Bash script that creates an RSA key pair.
Requirements:
- Name of the created private key is `school`
- Number of bits in the created key is 4096
- The created key is protected by the passphrase `betty`
