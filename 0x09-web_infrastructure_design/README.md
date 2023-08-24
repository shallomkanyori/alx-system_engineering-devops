## Web infrastructure design

#### Task 0: Simple web stack
[]() contains the design of a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`.
Requirements:
- Uses:
	- 1 server
	- 1 web server (Nginx)
	- 1 application server
	- 1 application files (your code base)
	- 1 database (MySQL)
	- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
- Explains the following specifics about this infrastructure:
	- What is a server
	- What is the role of the domain name
	- What type of DNS record www is in www.foobar.com
	- What is the role of the web server
	- What is the role of the application server
	- What is the role of the database
	- What is the server using to communicate with the computer of the user requesting the website
- Explains what the issues are with this infrastructure:
	- SPOF
	- Downtime when maintenance needed (like deploying new code web server needs to be restarted)
	- Cannot scale if too much incoming traffic
