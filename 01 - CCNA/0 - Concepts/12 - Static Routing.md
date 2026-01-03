There will be a connected route and a local route for each interface

**Connected** --> route to the network the interface is connected to (w/ actual netmask)
**Local** --> route to the actual IP address configured on the interface (w/ /32 netmask)

| Aspect      | Connected Route        | Local Route             |
| ----------- | ---------------------- | ----------------------- |
| Scope       | Entire subnet          | Single IP               |
| Destination | Other hosts            | This device             |
| Interface   | Physical / virtual NIC | Loopback or local stack |
| Used for    | Forwarding traffic     | Receiving traffic       |
| Example     | `192.168.1.0/24`       | `192.168.1.10/32`       |
> A router knows how to reach its own IP addresses and destination in its connected networks, but it doesn't know how to reach destinations in remote networks.

To send packets outside the LAN --> must send packets to **default gateway** (== router)
- *default gateway* configuration is also called a *default route*
- *default route* 
	- 0.0.0.0/0 = all netmask bits set to 0
	- the *least specific* route possible, because it includes **all**  IP addresses
	- On the contrary, /32 route only has ONE IP
	- "if there are not any more specific routes for this packet, do not drop it, send it to the *default route* instead."

**Two-way Reach-ability**
- Each router in the path needs two routes

Static Route Configuration with exit-interface
``` bash
# everything after "ip route" with the real thing
R2(config)# *ip route ip-address netmask exit-interface*
R2(config)# *ip route ip-address netmask exit-interface next-hop*
```

- Static routes in which you specify only the exit-interface rely on a feature called **Proxy ARP** to function.
	- generally not a problem
	- Neither is **better** just use which you prefer

Default route (aka default gateway)
- 0.0.0.0/0 --> least specific route possible --> includes every destination IP address
	- /0 == netmask 0.0.0.0
- If router d/n have more specific routes that match a packet's destination IP, sends to default route/gateway --> which is often used to send packet to internet
	- usually more specific routes are used for destinations in the internal corporate world