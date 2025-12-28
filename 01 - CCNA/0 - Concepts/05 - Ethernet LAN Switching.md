**Ethernet Frame**

![[Pasted image 20251226134854.png]]

Frame Check Sequence (FCS)
- 4 bytes (32 bits) in length
- detects corrupted data by running CRC algo over received data
- CRC = 'Cyclic Redundancy Check'

Sections of the Ethernet Frame
- Preamble
	- 7-byte sequence of alternating 1s and 0s used to **synchronize the receiver's clock with the sender**.
- Start Frame Delimiter (SFD)
	- 1-byte pattern (10101011) that **marks the exact start** of the Ethernet frame
- Destination Address
	- A 6-byte MAC address identifying the intended recipient of the frame
- Source Address
	- A 6-byte MAC address identifying the sender of the frame
- Length type
	- A 2-byte field that either indicates the **size of the payload** or the upper-layer protocol type
- Data
	- actual bits of the ethernet frame (header + payload) used as input to the CRC calculation
- Padding variable
	- extra bytes added if the data field is too small, ensuring the frame meets the min. ethernet frame size (64 bytes)
- Frame Check Sequence, CRC
	- 4-byte cyclic redundancy check value used by the receiver to detect transmission errors.

MAC Addresses
- 6-byte / 48-bit physical address assigned to the device when it is made
- Switches learn where devices are on the network by look at the source MAC address of received frames.
- **Unknown Unicast Frame** 
	- *a Ethernet frame sent to a specific destination MAC address that is not in a switch's MAC address table*
	- switch sends frames to all clients --> clients with MACs that do NOT match the frame's "Destination Address" simply ignore the packet
		- Called "MAC Flooding" == forwarding the frame out of ALL interfaces (except the one it received the packet on)
- **Dynamically learned MAC Address / Dynamic MAC address**
	- automatically discovered by network switches by examining the source address of incoming traffic, populating the CAM table to map devices to ports
- **OUI (Organizationally Unique Identifier)**
	- 1st half (24 bits) of a MAC address. It is a unique value assigned to the maker of the device.

![[Pasted image 20251226174155.png]]

