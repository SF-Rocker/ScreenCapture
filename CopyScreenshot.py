import subprocess
import os
import shutil
import datetime
import sys

def ensure_tools_installed():
    """Check if grim, slurp, maim, and clipboard tools are installed, install if missing."""
    required_tools = ["grim", "slurp", "maim", "xclip", "wl-copy"]
    missing = [tool for tool in required_tools if not shutil.which(tool)]

    if missing:
        print(f"Missing tools: {', '.join(missing)}. Installing...")
        try:
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y"] + missing, check=True)
            print("Installation complete.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install tools: {e}")
            sys.exit(1)

def capture_image():
    ensure_tools_installed()

    # Output directory
    user_home = os.path.expanduser("~")
    output_dir = os.path.join(user_home, "Pictures", "Screenshots")
    os.makedirs(output_dir, exist_ok=True)

    # Unique filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"screenshot_{timestamp}.png")

    # Detect session type
    session_type = os.environ.get("XDG_SESSION_TYPE", "").lower()

    try:
        if session_type == "wayland":
            # Slurp lets you click+drag to select region
            selection = subprocess.check_output(["slurp"]).decode("utf-8").strip()
            if not selection:
                print("Selection cancelled.")
                return
            subprocess.run(["grim", "-g", selection, output_file], check=True)
            # Copy to clipboard
            subprocess.run(["wl-copy"], input=open(output_file, "rb").read())
        elif session_type == "x11":
            # maim -s lets you click+drag to select region
            subprocess.run(["maim", "-s", output_file], check=True)
            # Copy to clipboard
            subprocess.run(["xclip", "-selection", "clipboard", "-t", "image/png", "-i", output_file], check=True)
        else:
            print(f"Unknown session type '{session_type}'. Defaulting to maim selection.")
            subprocess.run(["maim", "-s", output_file], check=True)
            subprocess.run(["xclip", "-selection", "clipboard", "-t", "image/png", "-i", output_file], check=True)

        print(f"Screenshot saved as {output_file} and copied to clipboard.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    capture_image()
