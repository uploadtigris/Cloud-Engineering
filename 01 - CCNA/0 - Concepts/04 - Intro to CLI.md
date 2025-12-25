+Connect to Cisco device with **Rollover cable**

Terminal Emulator *PuTTy*

user EXEC mode
- router>

privileged EXEC mode
- Router>enable
- Router#

autocomplete for commands
- Router>e?
	- shows the commands begging with that/those letter(s)
- enable exit

Terminal configuration
- Router# terminal
- .
- Router#conf t 
	- equals Router#configure terminal

password
- Router(config)#enable password?
	- shows the possible commands
- Router(config)#enable password ?
	- (with space) explains the further options
	- if `<cr>` shows up, no furthers options remaining
- beef up the password
	- Router#conf t
	- Router(config)#service password-encryption
		- BUT! running `show running-config`  shows the way the password will be displayed in the configuration file.... with a number in front of the password that explains the type of encryption used to scramble the password.
			- Type 7 password --> Cisco's proprietary password encryption
	- **more secure method**
		- Router(config) #`enable secret Cisco`
		- Router(config) # `do sh run`
			- `do` allows us to run commands at different access levels
			- Type 5 password --> MD5 encryption
- writing `no` in front of a command will have that action / specification NOT selected for the future. 

**Running-config**
- current, active config file on the device. Enter commands in the CLI, you edit the active configuration.

**Startup-config**
- the configuration file that will be loaded upon restart of the device

# Modes Review

```
Router> 
	--> user EXEC mode
Router# 
	--> priviledged EXEC mode
Router(config) \
	--> global configuration mode

Router>enable 
	--> used to enter privileged EXEC mode
Router#configure terminal 
	--> used to enter global configuration mode
Router(config)#enable password password 
	--> configures a password to protect priviledged exec mode
	
Router(config)#service password-encryption
	--> encrypts the enable password (and other password)
Router(config)#enable secret password
	--> configures a more secure, always-encrypted enable password
Router(config)#run privileged-exec-level-command
	--> executes a privileged-exec level command from global configuration mode
```



