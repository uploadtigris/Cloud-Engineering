[Download the .deb file](https://www.netacad.com/resources/lab-downloads?courseLang=en-US)
Move the file to somewhere sensible
```bash
sudo mkdir -p /opt/packettracer
sudo mv CiscoPacketTracer_*.AppImage /opt/packettracer/packettracer.AppImage
```
Make executable
```bash
sudo chmod +x /opt/packettracer/packettracer.AppImage
```
Create launcher command
```bash
sudo ln -s /opt/packettracer/packettracer.AppImage /usr/bin/packettracer
```
```bash
packettracer
```
Fix the launcher
If the login window is broken
```bash
packettracer --no-sandbox
```
If working, make permanent
```bash
sudo nano /usr/bin/packettracer
```
```bash
sudo chmod +x /usr/bin/packettracer
```

*ABOVE process was not working with CachyOS --> pivoted to using Virtual Machine Manager running QEMU/KVM*

# VMware troubleshooting

[VMware:  "error starting domain: network not found: no network with matching name 'default'"](https://blog.programster.org/kvm-missing-default-network)
```bash
# this showed up empty
sudo virsh net-list --all
```
```bash
sudo nano /etc/libvirt/qemu/networks/default.xml
```
copy and paste the below text
```xml
<network>
  <name>default</name>
  <uuid>PUT-A-UUID-HERE</uuid>
  <forward mode='nat'/>
  <bridge name='virbr0' stp='on' delay='0'/>
  <mac address='52:54:00:12:34:56'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
```
replace _ with a UUID using `uuidgen`

To manually start the network run:
```bash
sudo virsh net-start default
```
To have the network automatically start up in future run:
```bash
sudo virsh net-autostart --network default
```

Ubuntu VM will not start up, deep issues with CachyOS that are in the works

# Running packet tracer via Docker

```bash
sudo pacman -S docker
sudo systemctl enable --now docker
```

```bash
sudo pacman -S xorg-xhost
```

add user to the docker group

```bash
sudo usermod -aG docker $USER
```

```bash
xhost +local:docker
# output: non-network local connections being added to access control list
```

reboot computer to make sure user is added to docker group

```bash
# run docker
docker run -it \
  --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  somatorio/packet-tracer:latest
```

this process is illustrating to be that I just need to use packet tracer on my Ubuntu desktop instead of on CachyOS. That is what I will do.


