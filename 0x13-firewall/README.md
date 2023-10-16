## Firewall

#### Task 0
[0-block_all_incoming_traffic_but](0-block_all_incoming_traffic_but) contains the `ufw` commands that configure `ufw` to block all incoming traffic except the following TCP ports:
- `22` (SSH)
- `443` (HTTPS SSL)
- `80` (HTTP)

#### Task 1
[100-port_forwarding](100-port_forwarding) is a copy of the `ufw` configuration file that enables the firewall to redirect connections to `8080/tcp` to `80/tcp`.
