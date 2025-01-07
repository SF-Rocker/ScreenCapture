import subprocess
import os

def capture_image():
    # Define the output directory
    user_home = os.path.expanduser("~")  # Get the home directory of the current user
    output_dir = os.path.join(user_home, "Pictures", "Screenshots-Grim")
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Use Slurp to select a region of the screen
    try:
        # Run Slurp to get the selected area
        selection = subprocess.check_output(['slurp']).decode('utf-8').strip()
        
        # Define the output file path
        output_file = os.path.join(output_dir, 'screenshot.png')  # Change this to your desired output file name
        
        # Use Grim to capture the selected area
        subprocess.run(['grim', '-g', selection, output_file])
        
        print(f"Screenshot saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    capture_image()


