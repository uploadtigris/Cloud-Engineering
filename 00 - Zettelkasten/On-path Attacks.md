**attacker sits between two devices**
man in the middle attack

ARP poisoning (spoofing)
- client asks who is 192.168.1.1
- router sends MAC back to client
- client saves MAC in ARP cache
- *the attacker will send an ARP message to the client saying "I am 192.168.1.1 and THIS is my MAC address". ARP does not have security for this and will update the ARP Cache with this new address.*