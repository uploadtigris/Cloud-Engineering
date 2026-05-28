CNAME vs Alias
- CNAME
	- points a hostname to any other hostname
	- ONLY works for non-root domain (resources.google.com)
-  Alias
	- points a hostname to an AWS resource
	- Works for ROOT domain & non root (google.com)
- free of charge 

Routing Policies
- define how to respond to DNS queries
- DON't get confused by the word "routing"
	- d/n 'route' like a load balancer
	- DNS d/n route traffic, only responds to the DNS queries
- Route 53 supports the following routing policies
	- simple
		- traffic goes to a single resource
	- weighted
		- % of requests go to each specific resource
	- failover
	- latency based
	- geolocation
	- multi-value answer
	- geoproximity