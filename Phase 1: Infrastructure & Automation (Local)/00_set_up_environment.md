# Setting the Environment

## Intro

I will be doing the following setup on a Lenovo Pro 9 laptop running the linux distribution Fedora 42.

I am using the Hypervisor called "Virtual Machine Manager". To get VMM to run, I need to connect a session.

My configuration for virtualization will use QEMU/KVM, which requires that I enable libvirt in Fedora 42.

I used [this reddit post](https://www.reddit.com/r/linuxquestions/comments/9duxao/kvm_qemu_libvirt_virtmanager_how_do_these_all/) (the top comment) to understand how all of the technologies work together.

>KVM is the technology in the Linux kernel for using accelerated virtualization.

>QEMU is an CLI and userspace program to manage emulation and virtualization and can use KVM when it creates vitual machines.

>Libvirt provides an abstracted api for storage, network, computer, and virtualization. so other programs or people can managed it by one interface instead of manually.

I configured Libvirt by first enabling it, so that the service will run at start up
```
sudo systemctl enable libvirtd
```
Then, I just started the service to be able to run it in my session
```
sudo systemctl start libvirtd
```
## CentOS Stream
I created a new VM with CentOS Stream 10, using 4096 MiB for Memory and 4 CPUs. I allocated 40 GiB of drive space.

I created one basic User, not added to the privledges wheel. I also enabled a root account to be seperately available.

