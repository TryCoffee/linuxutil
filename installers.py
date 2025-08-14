import subprocess
from popups import *

def brave_installer(distro):
    print("Brave installer")
    match distro:
        case "arch":
            answer = ask_native_or_flatpak("AUR", "Flatpak", "Brave Installer", "Do you want to install Brave from AUR (prefered) or Flatpak?")
            if answer == "AUR":
                if yay_installed():
                    try:
                        command = "yay -Sy brave-bin"
                        subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                        print("Installation succeeded")
                        show_info("Brave Installer", "Installation succeeded. Now you can close terminal.")
                    except subprocess.CalledProcessError:
                        print("Installation failed")
                else:
                    print("You need to install yay before installation!")
                    show_info("Brave Installer", "You need to install yay before installation!")

            elif answer == "Flatpak":
                if flatpak_installed():
                    try:
                        command = "flatpak install -y flathub com.brave.Browser"
                        subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                        print("Installation succeeded")
                        show_info("Brave Installer", "Installation succeeded. Now you can close terminal.")
                    except subprocess.CalledProcessError:
                        print("Installation failed")
                else:
                    show_info("Brave Installer", "Please, install flatpak first")
            else:
                print("Aborting install...")


        case "debian":
            if ask_confirmation("Brave Installer", "Following commands will be executed\nsudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg\n\nsudo curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources\n\nsudo apt update && sudo apt install brave-browser\n\nContinue?"):
                if curl_installed():
                    try:
                        command = "sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && sudo curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources && sudo apt update && sudo apt install brave-browser"
                        subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                        print("Installation succeeded")
                        show_info("Brave Installer", "Installation succeeded.")
                    except subprocess.CalledProcessError:
                        print("Installation failed")
                else:
                    show_info("Brave_Installer", "You have to install curl!")
            else:
                print("Aborting install...")


        case "redhat":
            if ask_confirmation("Brave Installer", "Following commands will be executed\nsudo dnf install dnf-plugins-core\nsudo dnf config-manager addrepo --from-repofile=https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo\nsudo dnf install brave-browser\n\nContinue?"):
                try:
                    command = "sudo dnf install dnf-plugins-core && sudo dnf config-manager addrepo --from-repofile=https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo && sudo dnf install brave-browser"
                    subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                    print("Installation succeeded")
                    show_info("Brave Installer", "Installation succeeded.")
                except subprocess.CalledProcessError:
                    print("Installation failed")
            else:
                print("Aborting install...")

        case "flatpak":
            if flatpak_installed():
                try:
                    subprocess.run("flatpak install -y flathub com.brave.Browser", shell=True, check=True)
                    print("Installation succeeded")
                except subprocess.CalledProcessError:
                    print("Installation failed")
                    show_info("Brave Installer", "Installation failed")
            else:
                print("Flatpak not installed")
                show_info("Brave Installer", "Installation failed - Flatpak is not installed!")

        case _:
            print("You must select distro")
            show_info("Brave Installer", "It would be okay if you choose DISTRO!")

def spotify_installer(distro):
    print("Spotify Installer")
    match distro:
        case "arch":
            answer = ask_native_or_flatpak("AUR", "Flatpak", "Spotify Installer", "On Arch you can install spotify with flatpak or with AUR.\nWhich one do you prefer?")
            if answer == "Flatpak":
                if flatpak_installed():
                    try:
                        subprocess.run("flatpak install -y flathub com.spotify.Client", shell=True, check=True)
                        print("Installation succeeded")
                    except subprocess.CalledProcessError:
                        print("Installation failed")
                        show_info("Spotify Installer", "Installation failed")
                else:
                    print("Flatpak not installed")
                    show_info("Spotify Installer", "Installation failed - Flatpak is not installed!")
            elif answer == "Flatpak":
                if yay_installed():
                    try:
                        subprocess.run("yay -S spotify", shell=True, check=True)
                    except subprocess.CalledProcessError:
                        print("Installation failed")
                        show_info("Spotify Installer", "Installation failed")
                else:
                    print("You need to install yay before installation!")
                    show_info("Spotify Installer", "You need to install yay before installation!")
            else:
                print("Aborting install...")

        case "debian":
            if ask_confirmation("Spotify Installer",'Following commands will be executed\ncurl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg\n\necho "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list\n\nsudo apt-get update && sudo apt-get install spotify-client\n\nContinue?'):
                try:
                    command = 'curl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg && echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list && sudo apt-get update && sudo apt-get install spotify-client'
                    subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                    print("Installation succeeded")
                    show_info("Spotify Installer", "Installation succeeded. Now you can close terminal.")
                except subprocess.CalledProcessError:
                    print("Installation failed")
            else:
                print("Aborting install...")

        case "redhat":
            if ask_confirmation("Spotify Installer", "Spotify doesn't provide native RPM package. Do you want to install it with flatpak?"):
                if flatpak_installed():
                    try:
                        subprocess.run("flatpak install -y flathub com.spotify.Client", shell=True, check=True)
                        print("Installation succeeded")
                    except subprocess.CalledProcessError:
                        print("Installation failed")
                        show_info("Spotify Installer", "Installation failed")
                else:
                    print("Flatpak not installed")
                    show_info("Spotify Installer", "Installation failed - Flatpak is not installed!")
            else:
                print("Aborting install...")

        case "flatpak":
            if flatpak_installed():
                try:
                    subprocess.run("flatpak install -y flathub com.spotify.Client", shell=True, check=True)
                    print("Installation succeeded")
                except subprocess.CalledProcessError:
                    print("Installation failed")
                    show_info("Spotify Installer", "Installation failed")
            else:
                print("Flatpak not installed")
                show_info("Spotify Installer", "Installation failed - Flatpak is not installed!")


        case _:
            print("You must select distro!")
            show_info("Spotify Installer", "It would be okay if you choose DISTRO!")


def discord_installer(distro):
    print("Discord Installer")
    match distro:
        case "arch":
            try:
                command = "sudo pacman -S discord"
                subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                print("Installation succeeded")
                show_info("Discord Installer", "Installation succeeded. Now you can close terminal.")
            except subprocess.CalledProcessError:
                print("Installation failed")
        case "debian":
            if ask_confirmation("Discord Installer", "Unfortunately discord doesn't have it's own debian repository. Do you want to download & install .deb package from the internet?"):
                try:
                    subprocess.run('wget "https://discord.com/api/download?platform=linux&format=deb" -O /tmp/discord.deb', shell=True, check=True)
                    print("Download succeeded")
                    try:
                        command = 'sudo apt install /tmp/discord.deb && echo Installation ended'
                        subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                        print("Installation succeeded")
                        show_info("Discord Installer", "Installation succeeded. Now you can close terminal.")
                    except subprocess.CalledProcessError:
                        print("Installation failed")

                except subprocess.CalledProcessError:
                    print("Download failed")
        case "redhat":
            show_info("Discord Installer", "On Red Hat Based distros discord is located in fusion repo make sure it's enabled.")
            try:
                command = 'sudo dnf install discord'
                subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                print("Installation succeeded")
                show_info("Discord Installer", "Installation succeeded. Now you can close terminal.")
            except subprocess.CalledProcessError:
                print("Installation failed")

        case "flatpak":
            if flatpak_installed():
                command = "flatpak install -y flathub com.discordapp.Discord"
                message = 'Press any key to close this window...'

                subprocess.run([
                    'konsole',
                    '-e',
                    f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
                ])
            else:
                print("Flatpak not installed")

def davinci_installer(distro):
    print("DaVinci Resolve Studio Installer")
    match distro:
        case _:
            if ask_confirmation("DaVinci Resolve Installer", "Normally you would need to download DaVinci Resolve from website, repack and then install. Program can be downloaded from my local server and then installed. Do you want to continue?"):
                command = "wget http://integra.fun/api/public/dl/gsC2gYMz -O /tmp/davinci_resolve.run"
                subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                subprocess.run("notify-send 'DaVinci Resolve successfully downloaded!'", shell=True, check=True)
                command = "SKIP_PACKAGE_CHECK=1 /tmp/davinci_resolve.run"
                subprocess.run(['konsole', '-e', f'bash -c "{command} && exit"'])
                if ask_confirmation("DaVinci Resolve Installer", "Do you want to delete installer now?"):
                    subprocess.run('rm /tmp/davinci_resolve.run',shell=True, check=True)
                else:
                    print("Leaving installer in /tmp")
            else:
                print("Aborting install...")

def fedora_codecs(distro):
    print("Fedora Codecs")
    print("Make sure fusion repository is enabled!")
    if distro == 0:
        if ask_confirmation("Fedora Codecs Installer", "Are you sure that you are on fedora?"):
            command = "sudo dnf swap ffmpeg-free ffmpeg --allowerasing -y"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])

    else:
        command = "sudo dnf swap ffmpeg-free ffmpeg --allowerasing -y"
        message = 'Press any key to close this window...'

        subprocess.run([
            'konsole',
            '-e',
            f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
        ])

def rustdesk_installer(distro):
    print("RustDesk Installer")
    match distro:
        case "arch":
            show_info("RustDesk Installer", "Installer is going to download latest tar.gz package and install it. Continue?")
            command = "sudo pacman -Sy wget && wget https://github.com/rustdesk/rustdesk/releases/download/1.4.1/rustdesk-1.4.1-0-x86_64.pkg.tar.zst -O /tmp/rustdesk-1.4.1-0-x86_64.pkg.tar.zst && sudo pacman -U /tmp/rustdesk-1.4.1-0-x86_64.pkg.tar.zst"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])

        case "debian":
            show_info("RustDesk Installer", "Installer is going to download latest debian package and install it. Continue?")
            command = "wget https://github.com/rustdesk/rustdesk/releases/download/1.4.1/rustdesk-1.4.1-x86_64.deb -O /tmp/rustdesk-1.4.1-0-x86_64.pkg.tar.zst && sudo apt install /tmp/rustdesk-1.4.1-x86_64.deb"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])

        case "redhat":
            show_info("RustDesk Installer", "Installer is going to download latest RPM package and install it. Continue?")
            command = "wget https://github.com/rustdesk/rustdesk/releases/download/1.4.1/rustdesk-1.4.1-0.x86_64.rpm -O /tmp/rustdesk-1.4.1-0.x86_64.rpm && sudo dnf install /tmp/rustdesk-1.4.1-0.x86_64.rpm"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])

        case "flatpak":
            if flatpak_installed():
                show_info("RustDesk Installer", "Continue?")
                command = "flatpak install -y flathub com.discordapp.Discord"
                message = 'Press any key to close this window...'

                subprocess.run([
                    'konsole',
                    '-e',
                    f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
                ])
            else:
                print("Flatpak not installed")

def steam_installer(distro):
    print("Steam Installer")
    match distro:
        case "arch":
            command = "sudo pacman -S steam"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])
        case "debian":
            command = "sudo apt install steam"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])
        case "redhat":
            command = "sudo dnf install steam"
            message = 'Press any key to close this window...'

            subprocess.run([
                'konsole',
                '-e',
                f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
            ])
        case _:
            if ask_confirmation("Steam Installer", "It is not recommended to install steam via flatpak. Are you sure you want to do that?"):
                command = "flatpak install flathub com.valvesoftware.Steam"
                message = 'Press any key to close this window...'

                subprocess.run([
                    'konsole',
                    '-e',
                    f'bash -c "{command}; echo \'{message}\'; read -n 1 -s; exit"'
                ])
            else:
                print("Aborting install...")


def flatpak_installed():
    try:
        subprocess.run(["flatpak", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return True

def curl_installed():
    try:
        subprocess.run(["curl", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return True


def yay_installed():
    try:
        subprocess.run(["yay", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return True
