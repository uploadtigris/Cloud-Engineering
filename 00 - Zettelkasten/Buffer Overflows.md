- overwriting data spills over into other memory areas
- developers need to perform bounds checking
- not a simple exploit
- attacker is looking for a repeatable buffer overflow

![[Pasted image 20260201172033.png]]

Here, the last "e" turns the Hex Value to 65, which changes the Value of section B.
This gives the attacker the read/write permissions of an administrator