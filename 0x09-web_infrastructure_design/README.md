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
	- 1 domain name foobar.com configured with a www record that points to the server IP 8.8.8.8
- Specifics about this infrastructure:
	- What is a server: A server is a computer program or device that provides resources, data, services, or programs to other computers, known as clients, over a network. 
	- What is the role of the domain name: The domain name provides an easier way to navigate to the web application without memorizing its IP address.
	- What type of DNS record `www` is in `www.foobar.com`: An A record
	- What is the role of the web server: The web server handles client side interactions and serves static web pages. It also generates dynamic pages using templates. It may make API calls to the app server for specific data or functionality.
	- What is the role of the application server: The app server handles the application's business logic, processes data, and manages the application's core functionality by interacting with the database and performing data processing.
	- What is the role of the database: The database stores and manages the application's data.
	- What is the server using to communicate with the computer of the user requesting the website: HTTP
- Issues with this infrastructure:
	- SPOF: The design does not include any redundancy for the server, web server, app server, code base or database. So if any of these were to fail, the entire application would fail.
	- Downtime when maintenance needed: The design does not include any backups or replicas for the application. So the downtime when maintenance is being performed on the system will be equivalent to the total time the maintenance takes.
	- Cannot scale if too much incoming traffic: The design only includes one server therefore the application is limited to the traffic that one server can handle.
