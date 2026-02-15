## 🧠 Memory Framework: **SPICE** (Security Protocols I Can't Escape)

### **S - Secure Transport Protocols**

**Story**: "SSH transfers files securely, not FTP with SSL"

- **SFTP** = SSH (port 22), NOT FTP+SSL
- **FTPS** = FTP + SSL/TLS (the imposter)
- **SSH** = Secure remote login
- **SRTP** = Secure audio/video (like Zoom encryption)
- **S/MIME** = Secure email (graphics, audio, video)

**Mnemonic**: "_Sarah's Fancy Telephone Plays Secure Music_"

- Sarah = SSH/SFTP
- Fancy = FTPS (the fancy FTP)
- Telephone = SRTP (real-time calls)
- Secure Music = S/MIME (email multimedia)

---

### **P - Protocols & Their Parts**

**Story**: "IPsec's ESP does EVERYTHING, AH does almost nothing"

**IPsec Suite** (network layer protection):

- **ESP** = **E**verything: **E**ncryption + Authentication + Integrity
- **AH** = Authentication & Integrity only (no **E**ncryption)
- **IKE** = **I** set up **K**eys for ips**E**c VPNs

**Wi-Fi Encryption Timeline**:

```
WEP (broken) → TKIP (patch) → CCMP (AES-based, WPA2) ✅
```

**Mnemonic**: "_We Try Cool Crypto_"

---

### **I - Insecure = OLD**

**Rule**: If it's from the 1900s, it's **deprecated**

**The "Hall of Shame"** (never use):

- **DES** (1977) - 56-bit = too small
- **RC4** (1987) - broken stream cipher
- **MD5** (1991) - collision attacks
- **SSL** (1995) - replaced by TLS
- **SHA-1** (1995) - Google broke it in 2017

**Mnemonic**: "_During Reagan's Messy Presidency, Society Struggled_"

- D = DES, R = RC4, M = MD5, (P skip), S = SSL, S = SHA-1

**Modern alternatives**:

- DES → **AES** ✅
- RC4 → **AES** ✅
- MD5 → **SHA-256** ✅
- SSL → **TLS** ✅
- SHA-1 → **SHA-256** ✅

---

### **C - Crypto Types: Count the Keys**

**Symmetric** = **S**ame = **S**ecret key = **1 key**

- **AES**, **DES**, **3DES**, **RC4**, **IDEA**
- **Pattern**: 3-letter acronyms or single words

**Asymmetric** = **A**lways **2 keys** = public + private

- **RSA**, **ECC**, **DHE**, **DSA**
- **Pattern**: Named after people or math (Diffie-Hellman, Elliptic Curve)

**Memory trick**:

- Symmetric algorithms sound like **robot names** (AES, DES, RC4)
- Asymmetric algorithms sound like **people's initials** (RSA, DSA) or **math terms** (ECC, DHE)

---

### **E - Efficiency & Keys**

**Key Management Hierarchy**:

```
KEK (Key Encryption Key) 
  ↓ encrypts
DEK (Data Encryption Key)
  ↓ encrypts
Your actual data
```

**Story**: "The key that encrypts keys needs a key"

**Key Exchange Protocols** (all have "E" = Exchange):

- **DHE** - Diffie-Hellman Ephemeral
- **ECDHE** - EC Diffie-Hellman Ephemeral (ECC version)
- **IKE** - Internet Key Exchange (IPsec)

**PFS** = **P**rotects **F**uture & past **S**essions

- Each session gets unique keys
- Compromise one ≠ compromise all

**IoT/Low Power** = **ECC** (small keys, big security)

- **RSA** 3072-bit = **ECC** 256-bit (same security!)

---

## 🎯 Quick Drill Flash Cards

**Create mental associations**:

1. **SFTP vs FTPS**
    
    - "**SFTP** = **S**SH **F**ile **T**ransfer (port 22)"
    - "**FTPS** = **F**TP + **S**SL (port 21/990)"
2. **ESP vs AH**
    
    - "**ESP** has the **E** for **E**ncryption"
    - "**AH** is **A**lmost useless (no encryption)"
3. **Symmetric vs Asymmetric**
    
    - Hold up 1 finger = Symmetric
    - Hold up 2 fingers = Asymmetric
4. **Deprecated algorithms**
    
    - "If it existed when I was born (1900s) = dead"
5. **ECC for IoT**
    
    - "**E**CC = **E**fficient, **C**ompact, **C**heap (power)"
6. **RSA does it all**
    
    - "**R**SA = **R**eally does **S**ignatures **A**nd encryption"
7. **PFS**
    
    - "New session = New keys = **P**erfect **F**orward **S**ecrecy"

---

## 📝 One-Page Cheat Sheet Format

Create a physical card with:

**LEFT SIDE** (Secure/Modern):

```
✅ SFTP (SSH)
✅ AES
✅ SHA-256
✅ TLS
✅ ESP (IPsec)
✅ ECC (IoT)
✅ RSA (all-purpose)
✅ PFS (ECDHE/DHE)
```

**RIGHT SIDE** (Insecure/Deprecated):

```
❌ FTPS (not SSH)
❌ DES/3DES/RC4
❌ MD5/SHA-1
❌ SSL
❌ AH alone (no encryption)
❌ RSA for IoT (too big)
```

---

## 🧪 Test Yourself (Active Recall)

Before the exam, quiz yourself:

1. "Port 22 = ?" → SFTP/SSH
2. "IPsec encryption = ?" → ESP
3. "Key for keys = ?" → KEK
4. "IoT crypto = ?" → ECC
5. "Most secure cipher = ?" → AES
6. "Protects future sessions = ?" → PFS
7. "Wi-Fi WPA2 = ?" → CCMP

---

Does this framework help? The key is **active recall** + **spaced repetition** - review this in 1 day, 3 days, then 1 week!