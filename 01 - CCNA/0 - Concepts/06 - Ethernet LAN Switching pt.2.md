Ethernet frame (again)
- Preamble & SFD are not considered part of the Ethernet header, even though they are included in it. 
- ----------
- Eth. header
	- Destination addr
	- source addr
	- Type
- Eth. trailer
	- FCS
- ----------
- min size for ethernet frame (Header + Payload (Packet) + Trailer) is 64 bytes
- 64 byt - 18 byt (head + trailer) = 46 byt
- **min payload (packet) size is 46 byt**

ARP
- **Used to discover the layer 2 address (MAC Address) from a known layer 3 address (IP Address)**
- Two messages
	- ARP request
		- is a **broadcast** = sent to all hosts on the network
		- network interfaces will match destination **IP Addresses** with their own IP
	- ARP Reply
		- is **uni-cast** = sent only to one host (the host that sent the request)
		- if the MAC & interface is in the MAC address table this is a **known uni-cast frame** = forward (not flood)
- Following the ARP Reply --> PC that sent ARP Request will *add the MAC address corresponding to the inquired IP Address to it's "ARP Table"*

```
# cross platform (all 3)
arp -a
```

- Definitions
	- Internet Address 
		- IP Addr
		- Layer 3
	- Physical Address
		- MAC Addr
		- Layer 2
	- Type static = default entry
		- not learned through an arp request
	- Type dynamic = learned via ARP

Ping
- network utility that is **used to test reach-ability**
- Measures round-trip time
- The two messages
	- ICMP Echo Request
		- uni-cast message used to test the reach-ability of another specific host
	- ICMP Echo Reply
- metrics
	- . --> failed ping
	- ! --> successful ping
- in Cisco IOS --> "show arp"
- `show mac address-table`
	- *Ports = Interfaces*

Aging
- If the switch does not get any traffic from that MAC address for five minutes, it will remove that address from the MAC address table
- clear out the mac address table
	- `clear mac address-table dynamic`
	- `clear mac address-table dynamic address {mac-address}`
	- `clear mac address-table dynamic interface {interface-id \ port}`



