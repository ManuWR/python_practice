import zipfile, pathlib

def make_archive(filepaths, dest_dir):
    """
    Creates a zip archive from the given filepaths and saves it to the specified destination directory.

    Args:
        filepaths (list): A list of file paths to be included in the archive.
        dest_dir (str): The destination directory where the archive will be saved.

    Returns:
        None
    """
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == '__main__':
    make_archive(filepaths=["bonus.py", "bonus1.1.py"], dest_dir="dest")