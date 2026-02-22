```
  ____   ___   ___ _____ _  _____ _____   ____   ____    _    _   _ _   _ _____ ____  
 |  _ \ / _ \ / _ \_   _| |/ /_ _|_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
 | |_) | | | | | | || | | ' / | |  | |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
 |  _ <| |_| | |_| || | | . \ | |  | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
 |_| \_\\___/ \___/ |_| |_|\_\___| |_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
```
ROOTKIT-SCANNER
A minimalist but powerful Python security automation tool that leverages the 
'chkrootkit' engine. It performs a deep system audit to detect rootkits, 
backdoors, and suspicious binary signatures, filtering the output to show 
only critical security warnings and infected files.

**Features**
* **Deep System Audit:** Scans system binaries and kernel for known rootkit signatures.
* **Smart Filtering:** Automatically pipes output to `grep` to highlight only 'WARNING' or 'INFECTED' status.
* **Clean Interface:** Provides a clear terminal output using 'figlet' for immediate visual recognition.
* **One-Click Execution:** Simplifies a complex security command into a single, executable script.

**Prerequisites**
The following tools are required for the script to function correctly:
* Python 3.x
* chkrootkit: The primary scanning engine (Must be installed on your system).
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/Rootkit-Scanner.git

Navigate to the directory:
   * cd Rootkit-Scanner

Make the script executable:
   * chmod +x rootkit_scanner.py

**Usage**
Rootkit detection requires low-level system access, so the script must be run with sudo:

sudo python3 rootkit_scanner.py

**How it works:**
The script executes the system command `chkrootkit` and monitors the kernel and critical system paths. By using the `-E 'WARNING|INFECTED'` flag, it suppresses normal logs and only alerts you if something suspicious is found, making it ideal for regular security checkups.

**Important Notes:**
* **False Positives:** Chkrootkit can sometimes flag common system tools. Always investigate a "WARNING" before taking action.
* **Dependencies:** If the scan doesn't start, run `sudo apt install chkrootkit` manually.
* **Security Best Practice:** It is recommended to run this scanner on a regular schedule (e.g., via Cron) to ensure system integrity.
