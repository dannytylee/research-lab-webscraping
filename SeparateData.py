import os
import shutil

# Set the source directory where your Excel files are located
source_directory = r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Data'

# Set the destination directories for each remainder
destination_folders = {
    0: r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Data\Completing college',
    1: r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Data\Completing some college',
    2: r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Data\Completing high school only',
    3: r'C:\Users\danny\OneDrive\Files\GitHub\research-lab-webscraping\Data\Not completing high school',
}

# Iterate through all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(source_directory, filename)
        
        # Get the remainder when the file number is divided by 4
        file_number = int(filename.replace('EducationReport(', '').replace(').xlsx', ''))
        remainder = file_number % 4
        
        # Move the file to the appropriate destination folder
        destination_folder = destination_folders.get(remainder)
        if destination_folder:
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved '{filename}' to '{destination_folder}'")
