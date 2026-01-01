**IPv4 packet structure**

L3 header

![[Pasted image 20251231154049.png]]

version --> identifies version of IP used
- ipv4 - 4 (0100)
- ipv6 - 6 (0110)

IHL
- shows the length of the header
- min val is 5 --> 20 bytes
- max val is 15 --> would be 15 * 4 bytes = 60 bytes

DSCP
- Differentiated Services Code Point
- Length: 6 bits
- used for QoS (Quality of Service) 
- Used to prioritize delay-sensitive data (streaming voice, video, etc.)

ECN
- Explicit Congestion Notification
- Length: 2 bits
- provides end-to-end network congestion without dropping packets

Total Length
- Length: 16 bits
- Indicates the total length of the packet (L3 header + L4 segment)
- Measured in bytes (not 4-byte increments like IHL)

Identification Field
- all fragments of the same packet will have their own IPv4 header with the same value in this field
- Packets are *fragmented* **if larger than the MTU** (Maximum Transmission Unit) ~ 1500 bytes
	- Fragments are reassembled by the receiving host

Flags
- Bit 0: reserved, always set to 0
- Bit 1: Don't Fragment (DF bit) --> indicate do not frag packet
- Bit 2: More Fragments (MF bit) --> set to 1 if more fragments in packet, 0 for last fragment

Fragment Offset
- indicates the position of the fragment in the original, un-fragmented IP packet
- allows fragmented packets to be reassembled even if the fragments arrive out of order

Time to Live
- A router will drop a packet with a TTL of 0 to prevent network congestion or failure
	- in practice it indicates a 'hop count': each time the packet reaches a router, decreases by one.
	- **current recommended TTL is 64**

Protocol
- Indicates if TCP or UDP of the encapsulated L4PDU
	- *Value of 6 --> TCP*
	- *Value of 17 --> UDP*
	- *Value of 1 --> ICMP*
	- *Value of 89 --> OSPF (dynamic routing protocol)*

Header Checksum
- calculated checksum used to check for errors in the IPv4 header
- router calculates the checksum of header and compares it to this field 
	- if they d/n match, router drops the packet
	- both TCP and UDP

Source IP Address
Destination IP Address
- 32 bits each

Options
- rarely used
- length: 0 - 320 bits

**Fields of the IPv4 header**