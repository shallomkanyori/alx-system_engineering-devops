## HTTPS SSL

#### Task 0
[0-world_wide_web](0-world_wide_web) is a Bash script that will display information about subdomains.
- Accepts 2 arguments:
	1. `domain`:
		- type: string
		- what: domain name to audit
		- mandatory: yes
	2. `subdomain`:
		- type: string
		- what: specific subdomain to audit
		- mandatory: no
- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter `domain` is provided, displays information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
- Uses:
	- `awk`
	- at least one Bash function
- Does not handle edge cases such as:
	- Empty parameters
	- Nonexistent domain names
	- Nonexistent subdomains

#### Task 1
[1-haproxy_ssl_termination](1-haproxy_ssl_termination) is a copy of the HAproxy config file that configures HAproxy to accept encrypted traffic for the subdomain `www`.
Requirements:
- HAproxy is listening on port TCP `443`
- HAproxy is accepting SSL traffic
- HAproxy serves encrypted traffic that will return the `/` of the web server

#### Task 2
[100-redirect_http_to_https](100-redirect_http_to_https) is a copy of the HAproxy config file that configures HAproxy to automatically redirect HTTP traffic to HTTPS.
Requirements:
- This is transparent to the user
- HAproxy returns a 301
- HAproxy redirects HTTP traffic to HTTPS
