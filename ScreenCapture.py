import subprocess

# Run the 'slurp' command to select the area for the screenshot
print("Please select the area to capture with your mouse...")
command = "sudo apt-get install grim && sudo apt install slurp"
command = "grim -g \"$(slurp)\" screenshot.png"

try:
    # Execute the Grim command
    subprocess.run(command, shell=True, check=True)
    print("Screenshot saved as screenshot.png")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while taking the screenshot: {e}")
