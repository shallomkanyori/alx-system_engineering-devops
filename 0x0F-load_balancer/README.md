## Load balancer

#### Task 0
[0-custom_http_response_header](0-custom_http_response_header) is a Bash script that configures a new Ubuntu machine by building on [0x0C:Web Server/4-not_found_page_404](https://github.com/shallomkanyori/alx-system_engineering-devops/blob/master/0x0C-web_server/4-not_found_page_404) and adding the following:
- Configures Nginx so that its HTTP response contains a custom header.
	- The name of the custom HTTP header is `X-Served-By`
	- The value of the custom HTTP header is the hostname of the server Nginx is running on

#### Task 1
[1-install_load_balancer](1-install_load_balancer) is a Bash script that installs and configures a HAprroxy load balancer.
- Configures HAproxy so that it sends traffic to `web-01` and `web-02` servers
- Distributes requests using a roundrobin algorithm
- Ensures that HAproxy can be managed via an init script


#### Task 3
[2-puppet_custom_http_response_header.pp](2-puppet_custom_http_response_header.pp) is a Puppet manifest that configures an Nginx server with a custom HTTP response header on a new Ubuntu machine.
- The name of the custom HTTP header is `X-Served-By`
- The value of the custom HTTP header is the hostname of the server Nginx is running on
