![[Pasted image 20260207144643.png|300]]
- ASCII characters
- header and footer
	- this indicates it is likely a TLS certificate
	- CER
		- just a file extension
		- **.cer file could contain PEN or DER data**
		- on windows , .cer means DER
		- on linux , .cer could be PEM
	- DER (Distinguished Encoding Rules)
		- binary format (not text)
		- no headers or footers
		- is not legible in text editor
		- common format, used for Windows/Java applications
	- PEM (privacy-enhanced mail)
		- a very common format
		- has the header/footers
		- **BASE 64 encoded DER certificate**
		- stores DER certificate in a ASCII format
		- common across linux/unix/apache systems
	- X.509 
		- standard defining the structure and fields of a digital certificate
		- Almost all SSL/TLS certificates follow the X.509 standard
		- Specifies what information must be included: subject, issuer, public key, validity period, serial number, signature, etc.

What is a P12 certificate?
- **P12 (also called PFX or PKCS #12)** is a **certificate archive format** that bundles multiple items together into a single encrypted file.
- **PEM/DER** = certificate only (public key), no private key
- **P12/PFX** = certificate + private key bundled together
- **Why it exists:** It's designed for **portability and backup**. When you need to move a certificate and its private key to another server or backup your SSL certificate, you export it as a P12 file. The password protects the private key during transfer.
