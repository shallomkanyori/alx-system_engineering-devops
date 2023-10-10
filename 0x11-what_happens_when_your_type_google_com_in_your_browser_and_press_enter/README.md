## What happens when you type google.com in your browser and press Enter

Being a Full-Stack Software Engineer means you’re comfortable interacting with any layer of the stack.

A way to easily assess this is to simply ask an engineer to explain how a software system works. They can have a general overview of the flow or can choose to dig deep in a certain area.

#### Task 0
[0-blog_post](0-blog_post) contains a link to a blog post explaining what happens when you type https://www.google.com in your browser and press Enter.
Requirements, the post covers:
- DNS request
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Web server
- Application server
- Database

#### Task 1
[1-what_happen_when_diagram](1-what_happen_when_diagram) contains a link to a schema of the flow of the request created when you type https://www.google.com in your browser and press Enter.
The diagram shows
- DNS resolution
- that the request hitting server IP on the appropriate port
- that the traffic is encrypted
- that the traffic goes through a firewall
- that the request is distributed via a load balancer
- that the web server answers the request by serving a web page
- that the application server generates the web page
- that the application server request data from the database
