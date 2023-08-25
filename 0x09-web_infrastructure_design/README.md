## Web infrastructure design

#### Task 0: Simple web stack
[0-simple_web_stack](0-simple_web_stack) contains link to the design of a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`.
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

#### Task 1: Distibuted web infrastructure
[1-distributed_web_infrastructure](1-distributed_web_infrastructure) contains the link to the design of a three server web infrastructure that hosts the website `www.foobar.com`.
Requirements:
- The following components are added:
	- 2 servers
	- 1 web server (Nginx)
	- 1 application server
	- 1 load-balancer (HAproxy)
	- 1 set of application files (the code base)
	- 1 database (MySQL)
- Some specifics about this infrastructure:
	- For every additional element, why you are adding it: The additional server provides redundancy and backup. Should any of the web servers, app servers, databases, servers or code bases fail, the application can continue to operate using the other one.
	- What distribution algorithm your load balancer is configured with and how it works: The load balancer uses the Round Robin algorithm that distributes requests to all available servers in circular order. In this case, a request is sent to server 1 then the next request is sent to server 2, the next to server 1 and so on.
	- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both: The load balancer enables an Active-Active setup. Both servers are actively serving traffic. If one fails, the other continues to operate. In an Active-Passive setup, one server remains idle while the other serves traffic. If the active server fails, the passive server becomes active and takes over serving traffic.
	- How a database Primary-Replica (Master-Slave) cluster works: In this architecture, there is one primary node and one or more replica nodes. The primary node is the source of authority for the data. All write operations are initially performed on this node and it maintains the state of the database. The replica nodes are copies of the primary node's data. They serve only read requests and replicate data changes in the primary node. If the primary node fails, one of the replica nodes is promoted to the new primary node.
	- What is the difference between the Primary node and the Replica node in regard to the application: The replica node only serves read requests. All write requests are handled by the primary node.
- Issues with this infrastructure:
	- Where are SPOF: There is no redundancy for the load balancer. Should it fail, the application will fail as well.
	- Security issues (no firewall, no HTTPS): The servers, including the load balancer, do not have firewalls and are thus exposed to attacks. As the design does not include HTTPS, the user's data is not encrypted and is open to anyone who manages to break the connection between the user's computer and the application.
	- No monitoring: There is no monitoring at all for any of the components. Therefore, there will not be any alert if any component fails or if there are any other issues. This delays responding to and consequently resolving the issues.

#### Task 2: Secured and monitored web infrastructure
[2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure) contains the link to the design of a three server web infrastructure that hosts the website www.foobar.com that is secured, serves encrypted traffic, and is monitored.
Requirements:
- The following components are added:
	- 3 firewalls
	- 1 SSL certificate to serve www.foobar.com  over HTTPS
	- 3 monitoring clients (data collector for Sumologic or other monitoring services)
- Specifics about this infrastructure:
	- For every additional element, why you are adding it: The firewalls guard against attacks on the servers by managing the traffic passing into the servers.
	- What are firewalls for: A firewall is a division between a private network and an outer network that manages traffic passing between the two networks. They analyze data packets that request entry into the network and allow, limit, and block network traffic based on preconfigured rules in the hardware or software.
	- Why is the traffic served over HTTPS: HTTPS provides secure communication by encrypting all data that is sent. Thus, it is useful for handling sensitive user data as no one can decrypt the data even if the manage to get it.
	- What monitoring is used for: Through monitoring, you can be aware of what is going on in your application. You can detect and respond to issues with the component as well as obtain metrics that help you improve your application.
	- How the monitoring tool is collecting data: The monitoring tool loads the web application into a web browser, and using an automation script, it performs the user interactions and reports on the app’s performance and sends alerts in the event of an error
	- Explain what to do if you want to monitor your web server QPS: Integrate your web server with the monitoring tool by installing agents, exporters, or using APIs provided by the monitoring tool. These agents collect data about server performance, including QPS. Specify the metrics you want track QPS (Queries per second). The monitoring tool will regularly collect data about your web server's performance including request counts, and response times, which are necessary to calculate QPS.
- Issues with this infrastructure:
	- Why terminating SSL at the load balancer level is an issue: Communication between the load balancer and servers will not be encrypted exposing the data to hackers.
	- Why having only one MySQL server capable of accepting writes is an issue: While the replicas serve as backups in the case the primary server fails, during normal operation, that one primary server shoulders all write requests and this reduces scalability.
	- Why having servers with all the same components (database, web server and application server) might be a problem: Here are some issues with the application's current configuration. If one of a server's components fails, it may affect the entire server. As the application scales, it becomes more challenging and complex to manage and coordinate identical servers. Troubleshooting issues can be challenging as well because the servers are identical.
