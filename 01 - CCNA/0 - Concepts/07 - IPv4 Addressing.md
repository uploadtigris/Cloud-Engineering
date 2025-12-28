We will be exploring how data travels BETWEEN LANs (Network Layer)
- (Inside of LANs is the Data Link Layer)
- Network Layer
	- *uses logical addressing (IP Addresses)*
	- provides **path selection between source and destination**
	- Routers operate at **Layer 3**

Binary
- 1 0 1 0 1 0 0 0
- **128 64 32 16 8 4 2 1**
- 1 x 128 + 1 x 32 + 1 x 8 
- *complete the summation of each produce across the columns above to find the octet*

Decimal
- 1 0 1 0 1 0 0 0
- 128 64 32 16 8 4 2 1
- 128 + 32 + 8 = 143
- *complete the summation where if the number's column is paired with a 1, add the number to the summation

Decimal to Binary
- 221 convert to binary
- 128 64 32 16 8 4 2 
- -
- 221 - 128 = 93 --> place a 1 under 128
- 93 - 64 = 28 --> place 1
- 32 --> cannot subtract 32 from 28 & get a positive number
- 28 - 16 = 12 --> place 1
- 12 - 8 = 4 --> place 1
- 4 - 4 = 0 --> place 1
- 0
- 0
- -
- *1 1 0 1 1 1 0 0*

Loop Back Addresses
- Address range 127.0.0.0 - 127.255.255.255
- Used to test the 'network stack' on the local device
	- When device send traffic to this address, the device will receive traffic as if it is coming from an outside device.
- pinging this range of addresses has latency of 0ms

![[Pasted image 20251228111348.png]]

Netmask

![[Pasted image 20251228111548.png]]
- similar to /8, /16, /24 (juniper devices) except for Cisco devices

The **host** portion of the network address CANNOT be assigned to a host.
**Host** portion of the address is all 1's = **Broadcast Address**
- used to send traffic to all hosts on the network 


