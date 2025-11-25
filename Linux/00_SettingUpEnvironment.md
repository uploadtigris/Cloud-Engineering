# Setting up the Linux environmetn

I need to make sure the libvirt service is running
```
# enabling libvirtd service to run on start
sudo systemctl enable --now libvirtd
```
```
# checking if the service is running
systemctl status libvirtd
```
I then need to add my user to the libvirt and kvm groups
```
sudo usermod -aG libvirt $USER
sudo usermod -aG libvirt-qemu $USER
```
Then, I need to log out and back in for the changes to take effect.

Verify libvirt socket perimissions
```
ls -l /var/run/libvirt/libvirt-sock
```
You should see something like
```
srw-rw---- 1 root libvirt ...
```
The "group" must be "libvirt", if it is NOT then run:
```
sudo chgrp libvirt /var/run/libvirt/libvirt-sock
sudo chmod 660 /var/run/libvirt/libvirt-sock
```
My set is ready to go!
