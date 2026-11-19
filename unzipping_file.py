import zipfile
import os

# Define the path to the zip file and the directory to extract to 
zip_file_path = r'C:\Users\besha\OneDrive\Desktop\Kaggle\Digit Recognizer\digit-recognizer.zip'
extract_to_path = r'C:\Users\besha\OneDrive\Desktop\Kaggle\Digit Recognizer'

# Create the directory if it doesn't exitst
os.makedirs(extract_to_path, exist_ok=True)

# Open the zip file and extract all contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref :
    zip_ref.extractall(extract_to_path)

print (f"Extracted all files to {extract_to_path}")