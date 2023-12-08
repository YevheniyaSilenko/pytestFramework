import subprocess
import platform


def ping_websites(websites, count=3):
    system_platform = platform.system().lower()

    for website in websites:
        print(f"Pinging {website}...")

        command = ["ping", website]

        if system_platform == "windows":
            command += ["-n", str(count)]
        elif system_platform == "linux" or system_platform == "darwin":
            command += ["-c", str(count)]
        else:
            print(f"Unsupported operating system: {system_platform}")
            return

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while pinging {website}: {e}")

        print("\n" + "=" * 30 + "\n")  # Separator


websites_to_ping = ["www.google.com", "www.google.com"]
ping_websites(websites_to_ping)
