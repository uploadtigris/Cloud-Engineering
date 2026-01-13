What is a LAN?
- a LAN is a single **broadcast domain**, including all devices in that broadcast domain
- A **broadcast domain** is the group of devices which will *receive* a broadcast frame (destination MAC FFFF.FFFF.FFFF) sent by any one of the members.
- a connection between Router 1 and 2 would *also* be a broadcast domain

**Performance:** Lots of unnecessary broadcast traffic can reduce network performance.

> Although we separate hosts into subnets (Layer 3), they are still in the same broadcast domain (Layer 2). This happens with Unicast frames (sent to MAC: FFFF.FFFF...). *the switch does not recognize the subnets*

*This is where the VLANs come in* --> Even though all devices are in the LAN, we can separate the groups of devices at Layer 2.

For example:
- Subnet 1 --> VLAN10
- Subnet 2 --> VLAN20
- Subnet 3 --> VLAN30

A switch WILL NOT forward traffic between VLANs, including broadcast/unknown uni-cast traffic.
- Uni-cast frames with be sent to the Router which will in-turn be sent to the destination VLAN

The switch does not perform **inter-VLAN routing**. It must send the traffic through the router.

### VLANS
- are configured on switches **on a per-interfaces basis**
- logically separate end hosts at Layer 2
- switches MUST forward traffic to a router

>VLANs 1,1002-1005 exist by default and cannot be deleted.

Switch ports which carry multiple VLANs are called **'trunk ports'**


