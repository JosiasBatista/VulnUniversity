# IP ADDRESS
`10.10.95.55`

# OPEN PORTS - NMAP

```
21: ftp,
22: ssh (Possible takeover attempt),
139: netbios-ssn Samba,
445: netbios-ssn Samba,
3128: http,
3333: http-(server running)
```

# HIDDEN DIRECTORIES FOUND - GOBUSTER

```
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.95.55:3333
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Expanded:       true
[+] Timeout:        10s
===============================================================
2020/07/21 22:29:47 Starting gobuster
===============================================================
http://10.10.95.55:3333/.htaccess (Status: 403)
http://10.10.95.55:3333/.hta (Status: 403)
http://10.10.95.55:3333/.htpasswd (Status: 403)
http://10.10.95.55:3333/css (Status: 301)
http://10.10.95.55:3333/fonts (Status: 301)
http://10.10.95.55:3333/images (Status: 301)
http://10.10.95.55:3333/index.html (Status: 200)
http://10.10.95.55:3333/internal (Status: 301)
http://10.10.95.55:3333/js (Status: 301)
http://10.10.95.55:3333/server-status (Status: 403)
===============================================================
2020/07/21 22:32:53 Finished
```

# PRIVILEGE ESCALATION
`Use SUID for cat the root/root.txt and put the result on a file in /tmp so we can read this`

# FLAG FOUND AFTER PRIVILEGE ESCALATION
`a58ff8579f0a9270368d33a9966c7fd5`

# STEP BY STEP
`Found open ports: NMAP`
`Found hidden directories: GOBUSTER`
`Write script in python to find acceptable files: discover.py`
`Use reverse shell to enter the machine: reverse shell`
`Got the privilege escalation using SUID: SUID from linux`
`Pick the flag`
