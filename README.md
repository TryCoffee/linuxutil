
<img width="1536" height="1024" alt="logo" src="https://github.com/user-attachments/assets/49ed1010-1d1d-4a4e-8d8f-d2bf9f1d01fc" />



**Simon's Linux Utility** is a cross-distro Linux helper tool written in Python with a Qt6 GUI.  
It allows you to **install popular software**, perform **system tweaks**, and enable features like **multimedia codecs** — all in just a few clicks.

---

## ✨ Features

- 📦 **Install Popular Applications**  
  - Supports **most Linux distributions** (Debian/Ubuntu, Arch, Fedora)
  - Example: Brave Browser, Spotify, Discord, and others.

- 🛠 **System Tweaks**  
  - Install multimedia codecs on Fedora.  
  - Enable/disable optional system features.  

- 🎯 **Cross-Distro Support**  
  - Automatically detects your distribution.  
  - Uses native package managers if possible: `apt`, `dnf`, `pacman`, `yay`, `flatpak`.

- 🖥 **User-Friendly Interface**  
  - Built with Qt6 for a clean, modern look.  
  - Simple popups for password requests and confirmations.

---

## 📷 Screenshots

<img width="981" height="876" alt="Zrzut ekranu_20250813_221821" src="https://github.com/user-attachments/assets/bdd4c905-90b0-4c17-87b8-507dce8016d7" />


---

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/trycoffee/linuxutil.git
    cd linuxutil
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the program**:
    ```bash
    python main.py
    ```

---

## 📋 Requirements

- Python **3.11+**
- Qt6 (`PyQt6` or `PySide6`)
- Internet connection
- Appropriate privileges for package installation (sudo)

---

## ⚙️ Supported Distros & Package Managers

| Distribution Family | Example Distros            | Package Manager(s)  |
|---------------------|-----------------------------|----------------------|
| Debian-based        | Ubuntu, Linux Mint, Pop!_OS | `apt`                |
| Arch-based          | Manjaro, EndeavourOS        | `pacman`, `yay`      |
| Fedora-based        | Fedora Workstation, Nobara  | `dnf`                |
| Universal           | Any                         | `flatpak`            |

---

## 📌 Roadmap

- [ ] Add more software installation scripts  
- [ ] Add system cleanup tool  
- [ ] Add auto-update feature  
- [ ] Improve distro detection  
- [ ] Create AppImage / Flatpak version  

---

## 🛡 Disclaimer

This tool requires **administrator privileges** to install software and make system changes.  
Use at your own risk — I am not responsible for any issues caused by misuse.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ for Linux users by Szymon**
