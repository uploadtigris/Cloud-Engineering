This section covers:
- maximum number of hosts
- network address
- broadcast address
- first usable address
- last usable address of a particular network

**192.168.1.0 --> network address (Host portion all 0s)**
**192.168.1.255 --> broadcast address (Host portion all 1s)**

Max hosts per network = 2^n - 2 --> n = number of host bits

CLI
- Status column --> Layer 1 status
	- is the cable connected
	- is the device powered on
- Protocol --> Layer 2 status
	- i.e. is ethernet functioning properly

**netmask == subnet mask**

configuring IP addresses
```bash
R!(config-if)#ip add 192.168.0.254 255.255.255.0
```

On Cisco devices the **shutdown command** is applied to them by default
- `R1(config-if)#no shutdown` --> `no shut`

```bash
# do show ip interaces brief
R1(config-f)#do sh ip int br
```

```bash
# do show interfaces description
R1(config-if)#do sh int desc
```