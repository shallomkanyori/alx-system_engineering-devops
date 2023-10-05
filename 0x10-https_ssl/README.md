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
