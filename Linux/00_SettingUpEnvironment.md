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
sudo usermod -aG kvm $USER
```
Then, I need to log out and back in for the changes to take effect.
