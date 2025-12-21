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