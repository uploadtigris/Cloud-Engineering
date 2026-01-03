Switches have MAC address tables, Routers have **Routing tables** 
- (very important to know how to read)
- Two types: **Connected** and **Local** routes
	- **Connected routes** --> routes to networks that are *directly attached to an interface.*
		- "That network is over there"
		- Tells the system "entire subnet is reachable via this interface"
		- Created when you assign an IP address + subnet mask to an interface
		- Example
			- Given eth0 has 192.168.1.10/24 (subnet 255.255.255.0)
			- Any traffic destined for subnet 192.168.1.X is *sent to* eth0, which will send the traffic to the destination with an address on the subnet.
	- **Local routes** --> Routes to the exact IP address assigned to the device itself.
		- "That address is me"
		- tell the system "this IP belongs to me"
		- Created when an IP is assigned to an interface
		- Traffic never forwarded onto the network.
			- Loopback or local network stack
			- 192.168.1.10/32 (subnet mask 255.255.255.255)

| Aspect      | Connected Route        | Local Route             |
| ----------- | ---------------------- | ----------------------- |
| Scope       | Entire subnet          | Single IP               |
| Destination | Other hosts            | This device             |
| Interface   | Physical / virtual NIC | Loopback or local stack |
| Used for    | Forwarding traffic     | Receiving traffic       |
| Example     | `192.168.1.0/24`       | `192.168.1.10/32`       |

What is routing?
- **Routing** --> Process that routers use to determine path IP packets take over network to reach their destination
- **Dynamic Routing** --> dynamic routing protocols (ie. OSPF) used to share info w/ other routers automatically & build routing tables
- **Static Routing** --> network engineer / admin manually configures routes on the router
- **Route** --> tells the router "to send to destination X, send the packet to *next-hop* Y"
	- or if the IP address if device's own, receive the packet & do not forward

> A route **matches** a packet's destination if the packet's destination IP address is part of the network specified in the route.

- Most specific matching route = the matching route with the longest prefix length

Switches **flood frames** if they do not know where the destination is.
Routers **drop packets** if they cannot find a route to the packets destination.