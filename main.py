from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6.uic import loadUi
import sys, os
import subprocess
from PyQt6.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from popups import *
from installers import *
import distro

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        loadUi(resource_path("mainui.ui"), self)

        self.setWindowTitle("Simon's Linux Utility")

        id_like = distro.like().lower()
        name = distro.id().lower()
        self.distro1 = 0

        if "debian" in id_like or "ubuntu" in name:
            print("This is a Debian-based distro")
            self.distro = "debian"
            self.debianbased.setChecked(True)
            self.currentdistro.setText("Detected distro: Debian based")
        elif "rhel" in id_like or "fedora" in name or "centos" in name:
            print("This is a Red Hat-based distro")
            self.distro = "redhat"
            self.distro1 = 1
            self.redhatbased.setChecked(True)
            self.currentdistro.setText("Detected distro: RedHat based")
        elif "arch" in id_like or "arch" in name:
            print("This is an Arch-based distro")
            self.distro = "arch"
            self.archbased.setChecked(True)
            self.currentdistro.setText("Detected distro: Arch based")
        else:
            print("Unknown distro")
            self.distro = "none"
            self.currentdistro.setText("Detected distro: Unknown")
            show_info("Simon's Linux Utility", "Could not auto-recognize distro")

        self.brave_install.clicked.connect(lambda: brave_installer(self.distro))
        self.spotify_install.clicked.connect(lambda: spotify_installer(self.distro))
        self.discord_install.clicked.connect(lambda: discord_installer(self.distro))
        self.davinci_install.clicked.connect(lambda: davinci_installer(self.distro))
        self.fedora_codecs.clicked.connect(lambda: fedora_codecs(self.distro1))
        self.rustdesk_install.clicked.connect(lambda: rustdesk_installer(self.distro))
        self.steam_install.clicked.connect(lambda: steam_installer(self.distro))

        self.archbased.toggled.connect(self.radio_arch)
        self.debianbased.toggled.connect(self.radio_debian)
        self.redhatbased.toggled.connect(self.radio_redhat)
        self.flatpak.toggled.connect(self.radio_flatpak)



    def radio_flatpak(self):
        if self.flatpak.isChecked():
            print("Flatpak is checked")
            self.currentdistro.setText("")
            self.distro = "flatpak"
            print("Selected package manager: Flatpak")


    def radio_arch(self):
        if self.archbased.isChecked():
            print("Arch is checked")
            self.currentdistro.setText("")
            self.distro = "arch"
            print("Selected distro: Arch")

    def radio_debian(self):
        if self.debianbased.isChecked():
            print("Debian is checked")
            self.currentdistro.setText("")
            self.distro = "debian"
            print("Selected distro: Debian")

    def radio_redhat(self):
        if self.redhatbased.isChecked():
            print("RedHat is checked")
            self.currentdistro.setText("")
            self.distro = "redhat"
            print("Selected distro: RedHat")


def window():
    app = QApplication(sys.argv)
    #qdarktheme.setup_theme("dark")
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

window()
