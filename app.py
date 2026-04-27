import turtle as t
import random
import string

#Define the cybersecurity words
words = (
    {
    "Name":"Advanced Persistent Threat",
    "Description":"In an APT attack, a threat actor uses the most sophisticated tactics and technologies to penetrate a high-profile network. APTs aim to stay ‘under the radar’ and explore the network while remaining undetected for weeks, months, and even years. APTs are most often used by nation-state threat actors wishing to cause severe disruption and damage to the economic and political stability of a country. They can be considered the cyber equivalent of espionage ‘sleeper cells’.",
    "Alias":"APT"
    },
    {
    "Name":"Advanced Threat Protection",
    "Description":"Advanced Threat Protection (ATP) are security solutions that defend against sophisticated malware or hacking attacks targeting sensitive data. Advanced Threat Protection includes both software and managed security services.",
    "Alias":"ATP"
    },
    {"Name":"Adware",
    "Description":"Adware bombards users with endless ads and pop-up windows and causes a nuisance to the user experience. Adware can also pose a real danger to devices and the unwanted ads can include malware or redirect user searches to malicious websites that collect personal data about users. Adware programs are often built into freeware or shareware programs, where the adware operator collects an indirect fee for using the program. Adware programs usually do not show themselves in the system in any way. Adware programs seldom include a de-installation procedure, and attempts to remove them manually may cause the original carrier program to malfunction."
    },
    {"Name":"Anti-Botnet",
    "Description":"Anti-Botnet tools automatically generate botnet checks when a user browses a website. If a risk is detected, it sends back a warning message to the device. The most common anti-botnet solution is CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart). Read more on Allot’s solutions for Home Security."
    },
    {"Name":"Anti-Malware",
    "Description":"Anti-Malware is a program designed to protect computers and networks against any threats or attacks from viruses such as adware, spyware, and any such other malicious programs."
    },
    {"Name":"Anti-Phishing",
    "Description":"Anti-Phishing protects users from fraudulent websites, often perfect replicas of legitimate websites, undetectable to the human eye. Protection is enforced by detecting fraudulent emails, and by blocking phishing websites."
    },
    {"Name":"Anti-Virus",
    "Description":"Anti-Virus solutions integrate the latest generation of virus detection technology to protect users from viruses, spyware, trojans, and worms that can infect equipment through email or internet browsing."
    },
    {"Name":"Attack Vector",
    "Description":"An Attack Vector is the collection of all vulnerable points by which an attacker can gain entry into the target system. Attack vectors include vulnerable points in technology as well as human behavior, skillfully exploited by attackers to gain access to networks. The growth of IoT devices and (Work from Home) have greatly increased the attack vector, making networks increasingly difficult to defend."
    },
    {"Name":"Authentication",
    "Description":"Authentication is the process of verifying the identity of a user or piece of information and the veracity of the information provided. In computing, it is the process of identifying a person or system with a userName, password, etc. Authentication helps individuals and systems gain authorization based on their identity and prevent unauthorized access."
    },
    {"Name":"Backdoor",
    "Description":"Attackers use a Backdoor to gain access to a computer or a network. A programmer may bypass security steps and gain access to a computer through trapdoor programs, in the event of an attack on the computer system or networks. Attackers may also use such mechanisms to enter computers or networks without proper permission."
    },
    {"Name":"Banker Trojan",
    "Description":"A Banker Trojan is a malicious computer program that intercepts sensitive personal information and credentials for accessing online bank or payment accounts."
    },
    {"Name":"Blacklist",
    "Description":"A Blacklist, Blocklist, or Denylist is a basic access control mechanism that allows elements such as email addresses, users, passwords, URLs, IP addresses, domain Names, file hashes, etc. through the system, except those explicitly mentioned which are denied access."
    },
    {"Name":"Bot",
    "Description":"A Bot is a program that automates actions on behalf of an agent for some other program or person and is used to carry out routine tasks. Their use for malicious purposes includes spam distribution, credentials harvesting, and the launching of DDoS attacks."
    },
    {"Name":"Botnet",
    "Description":"A Botnet is a collection of compromised computers running malicious programs that are controlled remotely by a C&C (command & control) server operated by a cyber-criminal. Cybercriminals exercise remote control through automated processes (bots) in public IRC channels or websites. (Such websites may either be run directly by the ‘bot herder,’ or they may be legitimate websites that have been subverted for this purpose.)"
    },
    {"Name":"Brute Force Attack",
    "Description":"This is a method for guessing a password (or the key used to encrypt a message) that involves systematically trying a high volume of possible combinations of characters until the correct one is found. One way to reduce the susceptibility to a Brute Force Attack is to limit the number of permitted attempts to enter a password – for example, by allowing only three failed attempts and then permitting further attempts only after 15 minutes."
    },
    {"Name":"Business Continuity Plan",
    "Description":"A Business Continuity Plan is an organization’s playbook for how to operate in an emergency situation, like a massive cyberattack. The business continuity plan provides safeguards against a disaster and outlines the strategies and action plan on how to continue business as usual in the event of any large-scale cyber event. Read more on Allot’s solutions for Business Security."
    },
    {
    "Name":"Business Disruption",
    "Description":"The term Business Disruption refers to any interruption in the usual way that a system, process, or event works. Cyberattacks cause disruption to business operations and the associated risk of losses to the organization. "
    },
    {"Name":"BYOC",
    "Description":"Bring Your Own Computer (BYOC) is a fairly recent enterprise computing trend by which employees are encouraged or allowed to bring and use their own personal computing devices to perform some or part of their job roles, specifically personal laptop computers.",
    "Alias":"Bring Your Own Computer"
    },
    {"Name":"BYOD",
    "Description":"Bring Your Own Device (BYOD) is a policy of the organization allowing, encouraging or requiring its employees to use their personal devices such as smartphones, Tablet PCs, and laptops for official business purposes and accessing enterprise systems and data.",
    "Alias":"Bring Your Own Device"
    },
    {"Name":"BYOL",
    "Description":"Bring Your Own Laptop (BYOL) is a specific type of BYOC by which employees are encouraged or allowed to bring and use their own laptops to perform some or part of their job roles, including possible access to enterprise systems and data.",
    "Alias":"Bring Your Own Laptop"
    },
    {"Name":"CAPTCHA",
    "Description":"A CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a challenge-response test commonly used by websites to verify the user is a real human and not a bot. They can include simple arithmetic and questions about images, that bots have difficulty answering.",
    "Alias":"Completely Automated Public Turing Test to tell Computers and Humans Apart"
    },
    {"Name":"Clickjacking",
    "Description":"Clickjacking involves tricking someone into clicking on one object on a web page while they think they are clicking on another. The attacker loads a transparent page over the legitimate content on the web page so that the victim thinks they are clicking on a legitimate item when they are really clicking on something on the attacker’s invisible page. This way, the attacker can hijack the victim’s click for their own purposes. Clickjacking could be used to install malware, gain access to one of the victim’s online accounts, or enable the victim’s webcam."
    },
    {"Name":"Clientless",
    "Description":"Clientless refers to a program that is run entirely from the network, without requiring any installation of software on the endpoint device running the program."
    },
    {"Name":"Code Injection",
    "Description":"Code Injection is commonly used by malware to evade detection by antivirus and anti-malware programs by injecting malicious code into a legitimate process. This way the legitimate process serves as camouflage so all anti-malware tools can see running is the legitimate process and thus obfuscates the malicious code execution."
    },
    {"Name":"COTS",
    "Description":"Commercial off-the Shelf or Commercially Available off the Shelf (COTS) products are packaged solutions that are then adapted to satisfy the needs of the purchasing organization, rather than the commissioning of custom-made, or bespoke, solutions.",
    "Alias":["Commercial off-the Shelf","Commercially Available off the Shelf(COTS)"]
    },
    {"Name":"Critical Infrastructure",
    "Description":"Critical Infrastructure represents the fundamental systems of an organization that is important for its survival and where any threat to such basic systems would endanger the entire organization."
    },
    {"Name":"Cryptojacking",
    "Description":"Cryptojacking consists of hackers using the computing power of a compromised device to generate or mine cryptocurrency without the owner’s knowledge. Mining can be performed either by installing a malicious program on the target computer or through various kinds of fileless malware. Sometimes attackers take over part of the computer’s processing power when a page containing a special mining script is opened. Cryptojacking has been known to occur when viewing online ads or solving a CAPTCHA."
    },
    {"Name":"Cyberbullying",
    "Description":"Cyberbullying is the use of electronic means, primarily messaging and social media platforms, to bully and harass a victim. Cyberbullying has become a major problem, especially affecting young people, as it allows bullies to magnify their aggressive behavior, publicly ridicule victims on a large scale, and carry out damaging activities in a way that is difficult for parents and teachers to detect."
    },
    {"Name":"Cybersecurity",
    "Description":"Cybersecurity relates to processes employed to safeguard and secure assets used to carry information of an organization from being stolen or attacked. It requires extensive knowledge of possible threats such as viruses or other malicious objects. Identity management, risk management, and incident management form the crux of the cybersecurity strategies of an organization."
    },
    {"Name":"Dark Web",
    "Description":"The Dark Web is encrypted parts of the internet that are not indexed by search engines, most notoriously used by all types of criminals including; pedophiles, illicit human and contraband traffickers, and cyber criminals, to communicate and share information without being detected or identified by law enforcement. Malware of all types can be purchased on the dark web. A subset of the deep web, which can be accessed by anyone with the correct URL, dark web pages need special software (ex. Tor) with the correct decryption key and access rights and knowledge to find content. Users of the dark web remain almost completely anonymous due to its P2P network connections which makes network activity very difficult to trace."
    },
    {"Name":"Data Breach",
    "Description":"A Data Breach is the event of a hacker successfully exploits a network or device vulnerability and gains access to its files and data."
    },
    {"Name":"Data Integrity",
    "Description":"Data Integrity is a broad term that refers to the maintenance and assurance of data quality. This includes the accuracy and consistency of data over its entire lifecycle. Data Integrity is an important part of the design, implementation, and use of any data system that stores, processes, or retrieves information. The term is broad in scope and may have widely different meanings depending on the specific context."
    },
    {"Name":"Data Loss Prevention",
    "Description":"Data Loss Prevention (DLP) is an umbrella term for a collection of security tools, processes, and procedures that aim to prevent sensitive data from falling into unauthorized or malicious hands. DLP aims at preventing such occurrences through various techniques such as strict access controls on resources, blocking or monitoring email attachments, preventing network file exchange to external systems, blocking cut-and-paste, disabling the use of social networks and encrypting stored data.",
    "Alias":"DLP"
    },
    {"Name":"Data Theft",
    "Description":"Data Theft is the deliberate theft of sensitive data by nefarious actors."
    },
    {"Name":"DDoS",
    "Description":"A Denial of Service (DoS) or Distributed Denial of Service (DDoS) attack is when one or more compromised systems launch a flooding attack on a remote target(s), in an attempt to overload network resources and disrupt service. Some DDoS attacks have caused prolonged, complete service shutdowns of major online operators.",
    "Alias":["Denial of Service","DoS","Distributed Denial of Service"]
    },
    {"Name":"Decryption",
    "Description":"Decryption is the process of decoding cipher text to plain text so that it is readable by humans. It is the reverse of encryption, the process of converting plain text to cipher text. Cybercriminals use decryption software and techniques to ‘break’ security encryption and gain access to protected information."
    },
    {"Name":"Detection and Response",
    "Description":"Network Detection and Response is a security solution category used by organizations to detect malicious network activity, perform a forensic investigation to determine the root cause, and then respond and mitigate the threat."
    },
    {"Name":"Digital Forensics",
    "Description":"Digital Forensics is the process of procuring, analyzing, and interpreting electronic data for the purpose of presenting it as legal evidence in a court of law."
    },
    {"Name":"Digital Transformation",
    "Description":"Digital Transformation is the process of using digital technologies to create or modify business processes and customer experiences to keep up-to-date with current business and market requirements."
    },
    {"Name":"Domain Name Systems (DNS) Exfiltration",
    "Description":"Domain Name System (DNS) Exfiltration is a lower-level attack on DNS servers to gain unauthorized access. Such attacks are difficult to detect and can lead to loss of data."
    },
    {"Name":"Drive-By Download Attack",
    "Description":"Drive-by Downloads or attacks are a common method of spreading malware. Cybercriminals look for insecure websites and plant a malicious script into HTTP or PHP code on one of the pages. This script may install malware directly onto the computer of someone who visits the site, or it may take the form of an IFRAME that re-directs the victim to a site controlled by the cybercriminals. Such attacks are called ‘drive-by downloads’ because they require no action on the part of the victim — beyond simply visiting the compromised website: they have infected automatically (and silently) if their computer is vulnerable in some way (e.g., if they have failed to apply a security update to one of their applications).",
    "Alias":"Drive-by Downloads"
    },
    {"Name":"Encryption",
    "Description":"Encryption is a process of maintaining data confidentiality by converting plain data into secret code with the help of an encryption algorithm. Only users with the appropriate decryption key can unscramble and access encrypted data or cipher text."
    },
    {"Name":"Endpoint Protection",
    "Description":"Endpoint Protection refers to a system for network security management that monitors network endpoints, hardware devices such as workstations and mobile devices from which a network is accessed."
    },
    {"Name":"Endpoint Detection and Response",
    "Description":"Endpoint Detection and Response (EDR) are tools for protecting computer endpoints from potential threats. EDR platforms comprise software and networking tools for detecting suspicious endpoint activities, usually via continuous network monitoring.",
    "Alias":"EDR"
    },
    {"Name":"Exploit",
    "Description":"An exploit is taking advantage of a vulnerability or flaw in a network system to penetrate or attack it."
    },
    {"Name":"Fast Identity Online",
    "Description":"Fast Identity Online (FIDO) is a set of open authentication standards that enable a service provider to leverage existing technologies for passwordless authentication.",
    "Alias":"FIDO"
    },
    {"Name":"Fileless Malware",
    "Description":"Fileless Malware (FM), aka non-malware, or fileless infection, is a form of malicious computer attack that exists exclusively within the realm of volatile data storage components such as RAM, in memory processes, and service areas. This differentiates this form of malware from the classic memory-resident virus which requires some contact with non-volatile storage media, such as a hard disk drive or a thumb drive. Normally picked up following visits to malicious websites, fileless malware does not exist as a file that can be detected by standard antivirus programs. It lurks within a computer’s working memory and is exceptionally difficult to identify. However, this type of malware rarely survives a computer reboot, after which the computer should work as it did prior to infection.",
    "Alias":"FM"
    },
    {"Name":"Firewall",
    "Description":"A Firewall is a security system that forms a virtual perimeter around a network of workstations preventing viruses, worms, and hackers from penetrating."
    },
    {"Name":"Greylist",
    "Description":"A Greylist contains items that are temporarily blocked (or temporarily allowed) until an additional step is performed."
    },
    {"Name":"Hacker",
    "Description":"A Hacker is a term commonly used to describe a person who tries to gain unauthorized access to a network or computer system."
    },
    {"Name":"Honeypot",
    "Description":"Honeypots are computer security programs that simulate network resources that hackers are likely to look for to lure them in and trap them. An attacker may assume that you’re running weak services that can be used to break into the machine. A honeypot provides you with advanced warning of a more concerted attack. Two or more honeypots on a network form a honeynet."
    },
    {"Name":"Identity and Access Management",
    "Description":"Identity and Access Management (IAM) is the process used by an organization to grant or deny access to a secure system. IAM is an integration of workflow systems that involves organizational think tanks that analyze and make security systems work effectively.",
    "Alias":"IAM"},
    {
    "Name":"Identity Theft",
    "Description":"Identity Theft occurs when a malicious actor gathers enough personal information from the victim (Name, address, date of birth, etc.) to enable him to commit identity fraud – i.e., the use of stolen credentials to obtain goods or services by deception. Stolen data can be used to create a new account in the victim’s name (e.g., a bank account), to take over an existing account held by the victim (e.g., a social network account), or to masquerade as the victim while carrying out criminal activities."
    },
    {"Name":"Indicators of Compromise",
    "Description":"Indicators of Compromise (IoC) are bits of forensic data from system log entries or files that identify potentially malicious activity on a system or network. Indicators of Compromise aid information security and IT professionals in detecting data breaches, malware infections, or other threat activity.",
    "Alias":"IOC"
    },
    {"Name":"In-line Network Device",
    "Description":"An In-line Network Device is one that receives packets and forwards them to their intended destination. In-line network devices include routers, switches, firewalls, and intrusion detection and intrusion prevention systems, web application firewalls, anti-malware, and network taps."
    },
    {"Name":"Insider Threat",
    "Description":"An Insider Threat is when an authorized system user, usually an employee or contractor, poses a threat to an organization because they have authorized access to inside information and therefore bypass most perimeter-based security solutions."
    },
    {"Name":"Intrusion Prevention System",
    "Description":"An Intrusion Prevention System (IPS) is a network security system designed to prevent network penetration by malicious actors.",
    "Alias":"IPS"
    },
    {"Name":"IoT",
    "Description":"The term Internet of Things (IoT) is used to describe everyday objects that are connected to the internet and are able to collect and transfer data automatically, without the need for human interaction. The Internet of Things encompasses any physical object (not just traditional computers) that can be assigned an IP address and can transfer data: this includes household appliances, utility meters, cars, CCTV cameras, and even people (e.g., heart implants).",
    "Alias":"Internet of Things"
    },
    {"Name":"Keylogger",
    "Description":"A Keylogger is a kind of spyware software that records every keystroke made on a computer’s keyboard. It can record everything a user types including instant messages, email, usernames, and passwords."
    },
    {"Name":"Malvertising",
    "Description":"Malvertising is the use of online ads to distribute malicious programs. Cybercriminals embed a special script in a banner, or redirect users who click on an ad to a special page containing code for downloading malware. Special methods are used to bypass large ad network filters and place malicious content on trusted sites. In some cases, visitors do not even need to click on a fake ad — the code executes when the ad is displayed."
    },
    {"Name":"Malware",
    "Description":"Malware is a general term for any type of intrusive computer software with malicious intent against the user."
    },
    {"Name":"Man-in-the Middle Attack",
    "Description":"A man-in-the-middle attack (MITM) is an attack where the attacker secretly relays and possibly alters the communications between two parties who believe they are directly communicating with each other. For example, a victim believes he’s connected to his bank’s website and the flow of traffic to and from the real bank site remains unchanged, so the victim sees nothing suspicious. However, the traffic is redirected through the attacker’s site, allowing the attacker to gather any personal data entered by the victim (login, password, PIN, etc.).",
    "Alias":"MITM"
    },
    {"Name":"Network-based (cyber) Security",
    "Description":"Mass-market cybersecurity services (e.g., anti-malware, anti-phishing) that operate from within a CSP’s network and not at the endpoint, such as a PC or a mobile device. Network-based services can protect any connected device regardless of model or operating system. This type of service, however, cannot be bypassed like other cybersecurity solutions and they can be implemented with no software installation, upgrades or configuration required on the part of the end user, leading to high rates of service adoption."
    },
    {"Name":"Parental Controls",
    "Description":"Parental Controls are features which may be included in digital television services, computer and video games, mobile devices, and software that allow parents to restrict the access of content to their children. These controls were created to help parents control which types of content can be viewed by their children."
    },
    {"Name":"Patch",
    "Description":"A Patch provides additional, revised or updated code for an operating system or application. Except for open source software, most software vendors do not publish their source code. So, patches are typically pieces of binary code that are patched into an existing program (using an install program)."
    },
    {"Name":"Pen Testing",
    "Description":"Penetration testing (Pen Testing) is the practice of intentionally challenging the security of a computer system, network, or web application to discover vulnerabilities that an attacker or hacker could exploit.",
    "Alias":"Penetration testing"
    },
    {"Name":"Phishing",
    "Description":"Phishing is a type of internet fraud that seeks to acquire a user’s credentials by deception. It includes the theft of passwords, credit card numbers, bank account details, and other confidential information. Phishing messages usually take the form of fake notifications from banks, providers, e-pay systems, and other organizations. The phishing attempt will try to encourage a recipient, for one reason or another, to enter/update personal data. Common reasons given can include suspicious login to the account, or expiration of the password."
    },
    {"Name":"PII",
    "Description":"Personal Identifiable Information (PII or PII) is a type of data that identifies the unique identity of an individual.",
    "Alias":"Personal Identifiable Information"
    },
    {"Name":"Process Hollowing",
    "Description":"Process Hollowing is a security exploit in which an attacker removes code in an executable file and replaces it with malicious code. The process hollowing attack is used by hackers to cause an otherwise legitimate process to execute malicious code. This attack can be done while evading potential defenses, such as detection analysis software."
    },
    {"Name":"Ransomware",
    "Description":"Ransomware is the name given to malicious programs designed to extort money from victims by blocking access to the computer or encrypting stored data. The malware displays a message offering to restore the system/data in return for payment. Sometimes, cybercriminals behind the scam try to lend credibility to their operation by masquerading as law enforcement officials. Their ransom message asserts that the system has been blocked, or the data encrypted, because the victim is running unlicensed software or has accessed illegal content, and that the victim must pay a fine."
    },
    {"Name":"Remote Desktop Protocol",
    "Description":"RDP is a protocol for remotely connecting to computers running Windows. It enables interaction with desktop elements as well as access to other device resources. RDP was conceived as a remote administration tool. However, it is often used by intruders to penetrate targeted computers. By exploiting incorrectly configured RDP settings or system software vulnerabilities, cybercriminals can intercept an RDP session and log into the system with the victim’s permissions.",
    "Alias":"RDP"
    },
    {"Name":"Risktool",
    "Description":"Risktool programs have various functions, such as concealing files in the system, hiding the windows of running applications, or terminating active processes. They are not malicious in themselves, but include cryptocurrency miners that generate coins using the target device’s resources. Cybercriminals usually use them in stealth mode."
    },
    {"Name":"Rootkit",
    "Description":"A Rootkit is a collection of software tools or a program that gives a hacker remote access to, and control over, a computer or network. Rootkits themselves do not cause direct harm – and there have been legitimate uses for this type of software, such as to provide remote end user support. However, most rootkits open a backdoor on targeted computers for the introduction of malware, viruses, and ransomware, or use the system for further network security attacks. A rootkit is typically installed through a stolen password, or by exploiting system vulnerabilities without the victim’s knowledge. In most cases, rootkits are used in conjunction with other malware to prevent detection by endpoint antivirus software."
    },
    {"Name":"Sandbox",
    "Description":"In cybersecurity, a sandbox is an isolated environment on a network that mimics end-user operating environments. Sandboxes are used to safely execute suspicious code without risking harm to the host device or network."
    },
    {"Name":"Scareware",
    "Description":"Scareware is malware that uses scare tactics, often in the form of pop-ups that falsely warn users they have been infected with a virus, to trick users into visiting malware-containing websites."
    },
    {"Name":"SECaaS",
    "Description":"Security as a Service (SECaaS) is a type of cloud computing service where the provider offers the customer the ability to use a provided application. Examples of a SECaaS include online e-mail services or online document editing systems. A user of a SECaaS solution is only able to use the offered application and make minor configuration tweaks. The SECaaS provider is responsible for maintaining the application. Allot Secure is the first solution to offer SECaaS en mass to network service subscribers.",
    "Alias":"Security as a Service"
    },
    {"Name":"Secure Socket Layer",
    "Description":"A Secure Socket Layer (SSL) is the standard security technology for establishing an encrypted link between a web server and a browser. SSL was originally developed by Netscape to allow the private transmission of documents via the Internet.",
    "Alias":"SSL"
    },
    {"Name":"Security Incident Response",
    "Description":"Incident response is a planned approach to addressing and managing the reaction after a cyber attack or network security breach. The goal is to have clear procedures defined before an attack occurs to minimize damage, reduce disaster recovery time, and mitigate breach-related expenses."
    },
    {"Name":"Security Operations Center",
    "Description":"An Information Security Operations Center ( ISOC or SOC) is a facility where enterprise information systems (websites, applications, databases, data centers and servers, networks, desktops, and other endpoints) are monitored, assessed, and defended by SOC analysts.",
    "Alias":["Information Security Operations Center","SOC","ISOC"]
    },
    {"Name":"Security Perimeter",
    "Description":"A Security Perimeter is a digital boundary that is defined for a system or domain within which a specified security policy or security architecture is applied."
    },
    {"Name":"SIEM",
    "Description":"Security Information and Event Management (SIEM) is a formal process by which the security of an organization is monitored and evaluated on a constant basis. SIEM helps to automatically identify systems that are out of compliance with the security policy as well as to notify the IRT (Incident Response Team) of any security-violating events.",
    "Alias":"Security Information and Event Management"
    },
    {"Name":"SIM Swapping",
    "Description":"SIM Swapping is a scam used to intercept online banking SMS verification codes. To get hold of one-time passwords for financial transactions, cybercriminals create or fraudulently obtain a copy of the victim’s SIM card — for example, pretending to be the victim, the attacker might claim to have lost the SIM card and request a new one from the mobile operator. To protect clients from such schemes, most banks require that a replacement SIM card be re-linked to the account."
    },
    {"Name":"Sniffing",
    "Description":"Packet sniffing allows the capture of data as it is being transmitted over a network. Packet sniffer programs are used by network professionals to diagnose network issues. Malicious actors can use sniffers to capture unencrypted data like passwords and usernames in network traffic. Once this information is captured, the bad actor can then gain access to the system or network.",
    "Alias":"Sniffer"
    },
    {"Name":"SOAR",
    "Description":"SOAR (Security Orchestration, Automation and Response) is a solution stack of compatible software programs that organizations use to collect data about security threats from across the network and respond to low-level security events without human assistance.",
    "Alias":"Security Orchestration, Automation and Response"
    },
    {"Name":"Social Engineering",
    "Description":"Social Engineering is an increasingly popular method of gaining access to unauthorized resources by exploiting human psychology and manipulating users – rather than by breaking in or using technical hacking techniques. Instead of trying to find a software vulnerability in a corporate system, a social engineer might send an email to an employee pretending to be from the IT department, trying to trick him into revealing sensitive information. Social engineering is the foundation of spear phishing attacks."
    },
    {"Name":"Spam",
    "Description":"Spam is the name commonly given to unsolicited emails. Essentially unwanted advertising, it’s the email equivalent of physical junk mail delivered through the post."
    },
    {"Name":"Spear Phishing",
    "Description":"Spear Phishing is a phishing scam that targets a specific individual or organization, usually via a personalized email, SMS or other electronic communication to defraud them under the guise of a legitimate transaction."
    },
    {"Name":"Spoofing",
    "Description":"A Spoof is an attack attempt by an unauthorized entity or attacker to gain illegitimate access to a system by posing as an authorized user. Spoofing includes any act of disguising a communication from an unknown source as being from a known, trusted source. Spoofing can apply to emails, phone calls, and websites, or can be more technical, such as a computer spoofing an IP address.",
    "Alias":"Spoof"
    },
    {"Name":"Spyware",
    "Description":"Spyware is software that is secretly installed on a user’s device to gather sensitive data. Spyware quietly collects information such as credentials and sends it outside the network to bad actors. Spyware often comes in the form of a free download and is installed automatically, with or without user consent."
    },
    {"Name":"Threat Assessment",
    "Description":"Threat Assessment is a structured process used to identify and evaluate various risks or threats that an organization might be exposed to. Cyber threat assessment is a crucial part of any organization’s risk management strategy and data protection efforts."
    },
    {"Name":"Threat Hunting",
    "Description":"Cyber Threat Hunting is an active cyber defense activity where cybersecurity professionals actively search networks to detect and mitigate advanced threats that evade existing security solutions.",
    "Alias":"Cyber Threat Hunting"
    },
    {"Name":"Threat Intelligence",
    "Description":"Threat Intelligence, or cyber threat intelligence, is intelligence proactively obtained and used to understand the threats that are targeting the organization. Trojan Trojans are malicious programs that perform actions that are not authorized by the user: they delete, block, modify or copy data, and they disrupt the performance of computers or computer networks. Unlike viruses and worms, Trojans are unable to make copies of themselves or self-replicate.",
    "Alias":"cyber threat intelligence"
    },
    {"Name":"Two-factor Authentification",
    "Description":"Two-factor Authentification combines a static password with an external authentication device such as a hardware token that generates a randomly-generated one-time password, a smart card, an SMS message (where a mobile phone is the token), or a unique physical attribute like a fingerprint."
    },
    {"Name":"Two-step Authentification",
    "Description":"Two-step Authentification is commonly used on websites and is an improvement over single factor authentication. This form of authentication requires the visitor to provide their username (i.e. claim an identity) and password (i.e. the single factor authentication) before performing an additional step. The additional step could be receiving a text message with a code, then typing that code back into the website for confirmation. Alternatives include receiving an email and needing to click on a link in the message for confirmation, or viewing a pre-selected image and statement before typing in another password or PIN."
    },
    {"Name":"Virus",
    "Description":"A Virus is a malicious computer program that is often sent as an email attachment or a download with the intent of infecting that device. Once the device is infected, a virus can hijack the web browser, display unwanted ads, send spam, provide criminals with access to the device and contact list, disable security settings, scan, and find personal information like passwords."
    },
    {"Name":"VPN",
    "Description":"A Virtual Private Network (VPN) extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network. It is essentially a virtual, secure corridor.",
    "Alias":"Virtual Private Network"
    },
    {"Name":"Vulnerability",
    "Description":"Vulnerabilities are weaknesses in software programs that can be exploited by hackers to compromise computers."
    },
    {"Name":"WAF",
    "Description":"A Web Application Firewall (WAF) is a specific form of application firewall that filters, monitors, and blocks HTTP traffic to and from a web service. By inspecting HTTP traffic, it can prevent attacks exploiting a web application’s known vulnerabilities, such as SQL injection, cross-site scripting (XSS), file inclusion, and improper system configuration.",
    "Alias":"Web Application Firewall"
    },
    {"Name":"White Hat",
    "Description":"White hat and Black Hat are terms to describe the ‘good guys’ and ‘bad guys’ in the world of cybercrime. Black hats are hackers with criminal intentions. White hats are hackers who use their skills and talents for good and work to keep data safe from other hackers by finding system vulnerabilities that can be fixed.",
    "Alias":"Black hat"
    },
    {"Name":"Black Hat",
    "Description":"White hat and Black Hat are terms to describe the ‘good guys’ and ‘bad guys’ in the world of cybercrime. Black hats are hackers with criminal intentions. White hats are hackers who use their skills and talents for good and work to keep data safe from other hackers by finding system vulnerabilities that can be fixed.",
    "Alias":"White hat"
    },
    {"Name":"Whitelist",
    "Description":"A Whitelist, allowlist, passlist is a list of permitted items that are automatically let through whatever gate is being used."
    },
    {"Name":"Worm",
    "Description":"A Worm is a computer program that installs itself on a victim’s device and then looks for a way to spread to other computers, causing damage by shutting down parts of the network."
    },
    {"Name":"Zero-day Exploit",
    "Description":"This term is used to describe exploit code that has been written to take advantage of a vulnerability before the software vendor knows about it and can publish a patch for it. The result is that would-be attackers are free to exploit the vulnerability, unless proactive exploit prevention technologies have been implemented to defend the computer being targeted by the attacker."
    },
    {"Name":"Zero-touch Provisioning",
    "Description":"Zero-Touch Provisioning (ZTP) is an automatic device configuration process that frees IT administrators for more important tasks. The automated process reduces the possibility of errors when manually configuring devices and slashes the time it takes to set up devices for employee use, often without requiring IT intervention. Users can set up their devices with a few clicks, eliminating the need for administrators to create and track system images or manage the infrastructure required to push those images to new or repurposed devices.",
    "Alias":"ZTP"
    },

)

"""
Logic pathway:
    Define words (Check)
    Pick a specific word, store it as Name and Description
    Create the screen and put in however many spaces are necessary
    Handle guesses
"""

#Return what the word's name, description, and aliases are
def chooseword ():
    number = random.randint(0,len(words))
    word = words[number]
    Name = word["Name"]
    Description = word["Description"]
    if word.get("Alias") == None:
        return Name, Description, None
    else:
        return Name, Description, word["Alias"]


#Draw the gallows for the man
def drawgallows(x,startx,starty):
    #Create a turtle and move it to the desired location
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.home
    pen.setpos(startx,starty)
    pen.setheading(0)
    pen.pendown()
    #Draw the gallows
    pen.forward(0.5*x)
    pen.right(90)
    pen.forward(x)
    pen.right(90)
    pen.forward(x)
    pen.right(90)
    pen.forward(0.125*x)
    pen.right(90)
    pen.forward(x)
    pen.left(90)
    pen.forward(0.75*x)
    pen.left(45)
    pen.forward(1.4*0.125*x)
    pen.penup()


#A generic function to write words. It takes the words, which turtle will be used, their position, and where to wrap the text
def writewords (words, startx, starty,width, newpen):
    written = words.split()
    newpen.hideturtle()
    newpen.penup()
    newpen.setpos(startx,starty)
    for word in written:
        #Iterates through each word. Must check whether its position is too close
        #to the edge of the screen (say, 30 pixels)
        if newpen.xcor() > width/2-30:
            newpen.penup()
            newpen.setpos(startx,newpen.ycor()-15)
        newpen.write(word,move=True)
        newpen.forward(4)



#Process: iterate through each letter, if it is already seen draw it unless it
#has already been drawn
def drawwords (word,seenletters,drawnletters,startx,starty,width,pen):
    pen.hideturtle()
    x = startx
    y = starty
    i = 0
    correct = False
    for letter in word:
        #This will loop through until everything has been taken care of.
        if letter.lower() in seenletters:
            if drawnletters[i] == letter.lower():
                x = x+10
                i = i+1
            else:
                writewords(letter,x,y,width,pen)
                x = x+10
                drawnletters[i] = letter.lower()
                i = i+1
                correct = True
        else:
            writewords("_",x,y,width,pen)
            x = x+10
            i = i+1
    return drawnletters, correct


#Iterative function to handle user input
def guess (seen,prompt):
    letter = t.textinput("Guess",prompt).lower()
    if letter == "exit":
        return "Exit"
    elif letter in seen:
        guess(seen,"You have already guessed that letter")
    elif len(letter) > 1:
        guess(seen,"Your guess is longer than one character")
    else:
        seen.add(letter)
    return seen


#Define a simple circle-drawing function
def drawcircle (x,y,radius,turtle):
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(x,y+radius)
    turtle.setheading(0)
    steps = 50
    for i in range(steps):
        turtle.pendown()
        turtle.forward(2*radius*3.14/steps)
        turtle.right(360/steps)
    turtle.pendown()


#Function to draw the man
def drawman(stage,x,y,turtle,width):
    pen = turtle
    pen.hideturtle()
    size = width/64
    if stage == 1:
        pen.penup()
        pen.goto(x,y)
        pen.right(90)
        pen.pendown()
        pen.forward(size)
        drawcircle(x,y-size*2,size,pen)        
    elif stage == 2:
        pen.penup()
        pen.setpos(x,y-size*3)
        pen.right(90)
        pen.pendown()
        pen.forward(size*3)
    elif stage == 3:
        pen.penup()
        pen.setpos(x,y-size*6)
        pen.pendown()
        pen.setheading(0)
        pen.right(45)
        pen.forward(size*2)

    elif stage == 4:
        pen.penup()
        pen.setpos(x,y-size*6)
        pen.pendown()
        pen.setheading(0)
        pen.right(135)
        pen.forward(size*2)
    elif stage == 5:
        pen.penup()
        pen.setpos(x,y-size*4)
        pen.pendown()
        pen.setheading(0)
        pen.left(45)
        pen.forward(size*2)
    elif stage == 6:
        pen.penup()
        pen.setpos(x,y-size*4)
        pen.pendown()
        pen.setheading(0)
        pen.left(135)
        pen.forward(size*2)    


#Found on StackOverflow, authors rsmoothy and Neeraj
def ireplace(old, new, text):
    idx = 0
    while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new) 
    return text


#Initialize variables and other aspects
def initialize():    
    #Find the word's name, its description, and any aliases
    Name,Description, Alias = chooseword()
 
    Hint = ireplace(Name,"___",Description)
    if Alias == None:
        pass
    elif type(Alias) == str:
        Hint = ireplace(Alias,"___",Hint)
    else:
        for i in Alias:
            Hint = ireplace(i,"___",Hint)

            
    #Create the screen and define what characters have been seen before
    sc = t.Screen()
    sc.clear()
    letters = ["-"," "]
    seen = set(letters)
    drawnletters = []
    for letter in Name:
        drawnletters.append("")
    sc.title("Hangman")
    sc.setup()
    #Find the width and height of the window
    width = sc.window_width()
    height = sc.window_height()
    hint = t.Turtle()
    hint.hideturtle()
    pen = t.Turtle()
    pen.hideturtle()
    writewords(Hint,0-width/4,0-height/4,width/2,hint)
    drawgallows(width*0.25,0,height/4)
    i = 0
    man = t.Turtle()
    man.hideturtle()
    drawnletters, correct = drawwords(Name,seen,drawnletters,0-len(Name)*5,0+height/4+10,width,pen)
    while i < 6:
        seen = guess(seen,"Guess a letter")
        if seen == "Exit":
            break            
        else:
            drawnletters, correct = drawwords(Name,seen,drawnletters,0-len(Name)*5,0+height/4+10,width,pen)
            drawnword = ""
            #Concatenate strings to check whether it is the same as the true word
            for letter in drawnletters:
                drawnword = drawnword+letter
            #If their guess is correct, congratulate them and exit
            if drawnword.lower() == Name.lower():
                pen = t.Turtle()
                writewords("Congratulations!",0-38,0+height/3,width/2,pen)
                hint.clear()
                writewords(Description,0-width/4,0-height/4,width/2,hint)
                break
        #If they are correct, then don't draw the next stage of the man
        if correct == True:
            pass
        else:
            i+=1
            drawman(i,0,height/4,man,width)
            if i == 6:
                pen = t.Turtle()
                pen.hideturtle()
                writewords("I'm sorry, you failed to guess the word. It was " + Name,0-width/4,0+height/3,width/2,pen)
                hint.clear()
                writewords(Description,0-width/4,0-height/4,width/2,hint)
                break
    restart = t.textinput("Restart","Do you want to restart? Y to restart, or any other key to exit")
    if restart.upper() == 'Y':
        return True
    else:
        return False


i = True
while i == True:
    i = initialize()
