## Web stack debugging #1

#### Task 0
[0-nginx_likes_port_80](0-nginx_likes_port_80) is a Bash script thatautomates fixing an Ubuntu container whose Nginx installation is not listening on port `80`
Requirements:
- Nginx must be running, and listening on port `80` of all the server’s active IPv4 IPs

#### Task 1
[1-debugging_made_short](1-debugging_made_short) is Bash script that does the same thing as [0-nginx_likes_port_80](0-nginx_likes_port_80) but shorter.
Requirements:
- Is 5 lines long or less
- Does not use `;`, `&&` or `wget`
- Does not execute the previous answer file
- `service` (init) must say that nginx is not running
