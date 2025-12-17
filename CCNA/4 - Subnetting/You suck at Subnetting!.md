[you suck at Subnetting](https://www.youtube.com/playlist?list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF)

# The IP Address

**IPv4:** ***192.168.1**.204
- the first 3 octets are determined by the sub-net mask
- how **many** IP addresses?
	- bc of the subnet mask's last octet = 0, last octet of IPv4 can be between 0 and 255
	- This means 256... right? 
		- the FIRST IP == `Network Address` --> 192.168.1.0
		- the LAST IP == `Broadcast Address` --> 192.168.1.255
			- if you send something here, it will sent it to everyone on the network!
		- the Default Gateway -->192.168.1.1
	- SO! we only have 253 IP addresses available to be assigned

**Subnet Mask:** 255.255.255.0
- 255 in the octet means the corresponding IPv4 octet will always stay the same
- 0 means the corresponding octet can be any number between 0 and 255

**Default Gateway:** 192.168.1.1
- Ex: `3.255.92.8` --> Netflix
- Say a client is looking for Netflix's IPv4 addr. 
	- Client looks to it's OWN network portion of it's IPv4, noting that the network portion is different than the Netflix IPv4.
	- The Client will then look to the Subnet Mask and see the set of three 255 octet, showing the network octets to the client.
	- From here, the Client will ask the `Default Gateway` == **the Router**
- Helps you to get OUTSIDE of your network

# we ran OUT of IP Addresses!

NOTE: Cisco only subtracts Network Address and the Broadcast Address **NOT the following**:
- Default gateway
- Routers
- Switches
- Servers
- Firewalls
- “Infrastructure devices”

2 ** host bits = result - (network + broadcast) = total IPs

```
| 8 bits | 8 bits | 8 bits | 8 bits |
|--------|--------|--------|--------|
|  1st   |  2nd   |  3rd   |  4th   |
```

1) Host bits = 32 − prefix length
2) Total addresses = 2^(host bits)
3) Usable hosts = 2^(host bits) − 2 (net & broad)

ex1)
***/24***
Network bits = 24
Host bits = **32** − 24 = 8
Total = 2^8 = 256
Usable = 256 − 2 = **254**

### Subnet mask calculation

each octet has 8 bits: 128, 64, 32, 16, 8, 4, 2, 1
if bit = 1 --> network
if bit = 0 --> host
*/27 mask example*
11111111.11111111.11111111.**111**00000 = 27 ttl 1s
decimal form --> 255.255.255.(**128+64+32**) = 255.255.255.224

----------------------------------

### Network Classes

Taking a classed network and cutting it up using a different subnet mask than its default is called a **classless network** (what we use today)
![[Pasted image 20251217111230.png]]
*chart represents the classes built by IANA*

**IPv4 Classful Addressing (A vs B vs C)**

| Class | Leading Bits | First Octet Range | Default Subnet Mask | CIDR | Networks  | Hosts per Network | Private Range  |
| ----- | ------------ | ----------------- | ------------------- | ---- | --------- | ----------------- | -------------- |
| A     | 0xxxxxxx     | 1 – 126           | 255.0.0.0           | /8   | 126       | 16,777,214        | 10.0.0.0/8     |
| B     | 10xxxxxx     | 128 – 191         | 255.255.0.0         | /16  | 16,384    | 65,534            | 172.16.0.0/12  |
| C     | 110xxxxx     | 192 – 223         | 255.255.255.0       | /24  | 2,097,152 | 254               | 192.168.0.0/16 |


D --> Multi-cast
E --> Experimental
Note the gap between A and B
- 127.0.0.0 w/ SN Mask of 255.0.0.0
- these are for LOOP BACK devices
- 2 ** 24 = 16,777,216 devices available 
	- why so virtual IP address ready to respond to itself on our devices?
- **Remember! 127.x.x.x are LOOP BACK devices**

