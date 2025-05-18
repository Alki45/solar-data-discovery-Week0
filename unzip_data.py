import zipfile
import os

def unzip_file(zip_path, extract_to='.'):
    """
    Unzips a .zip file to the specified directory.
    
    :param zip_path: Path to the .zip file.
    :param extract_to: Directory where files will be extracted.
    """
    if not zipfile.is_zipfile(zip_path):
        print(f"❌ Not a valid zip file: {zip_path}")
        return
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"✅ Extracted: {zip_path} to {extract_to}")

# Example usage
zip_file_path = 'data/data.zip'   
destination_folder = 'data/'            
unzip_file(zip_file_path, destination_folder)
