**Interface speed and duplex**

Status: down & Protocol: down != Status: administratively down & Protocol: down
- down down --> not connected to another device
	- bc of `shutdown` command , which **Routers** have applied by default they will be *administratively down/down* 
	- **Switch** interfaces do NOT have the `shutdown` command applied by default
		- will be in up/up state is connected to another device
		- OR in the down/down state if not

**Speed and duplex auto negotiation**

Duplex / Speed is `auto` by default --> will auto negotiate with neighboring device
- *a-full* means that the device auto negotiated for full duplex with the neighboring device
-  `speed`: *auto* means device negotiated with neighbor for the fastest speeds that each device is capable of

Half duplex
- device CANNOT send AND receive data at the same time
- In the modern day used almost no where
- This was used in **Hubs**

Full duplex 
- CAN send / receive at same time
- This is most modern devices

CSMA/CD
- **Carrier Sense Multiple Access w/ Collision Detection**
	- device 'listens' to the collision domain until detect other devices not sending
- if collision does occur, device sends a jamming signal to inform other devices that a collision happened
- device waits a random period of time before sending 
- BUT hubs are simple and operate at Layer 1, simple repeated

Switches operate at Layer 2 and send Frames to specific hosts using MAC addressing

**Interface status**

Shutting down interfaces on a switch
```bash
SW1(config)#interface range f0/5 - 12

SW1(config-if-range)#description ## not in use ##

# change the interfaces in the range to "administratively down"
SW1(config-if-range)#shutdown
```

**Interface counters & errors**

**Runts**: frames that are smaller than the minimum frame size (64 bytes)
**Giants**: frames that are larger than the max frame size (1518 bytes)
**CRC**: frames that *failed* the CRC check (in the Ethernet FCS trailer)
**Frame**: frames that have an incorrect format (due to an error)
**Input errors**: Total of various counters, such as the above 4 types
**Outputs errors**: frames the switch tried to send, but failed due to an error

