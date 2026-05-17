import zipfile

# Using 'with' ensures the file is closed automatically
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    zip_ref.extractall('')
    print("Files extracted successfully.")
