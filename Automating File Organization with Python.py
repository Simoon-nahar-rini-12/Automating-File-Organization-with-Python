import os
from datetime import datetime
import shutil

def organize_files(path, mode="type", size_limit=10 * 1024 * 1024):  # 10 MB in bytes
  """Organizes files in a directory based on user-specified criteria (type or size).
  Args:
      path: The path to the directory containing the files.
      mode: The organization mode ("type" or "size").
       size_limit: The size threshold in bytes (used only in size mode, default: 10MB).
  """

  files = os.listdir(path)
  for file in files:
    file_path = os.path.join(path, file)

    try:
      if mode == "type":
        # Get file extension
        filename, extension = os.path.splitext(file)
        extension = extension[1:].lower()  # Convert to lowercase
        target_dir = path + '/' + extension
      elif mode == "size":
        # Get file size
        file_size = os.path.getsize(file_path)
        if file_size < size_limit:
          target_dir = path + '/Small_Files'
        else:
          target_dir = path + '/Large_Files'
      else:
        raise ValueError("Invalid organization mode. Choose 'type' or 'size'.")

      if not os.path.exists(target_dir):
        os.makedirs(target_dir)
      shutil.move(file_path, target_dir + '/' + file)
      print(f"Moved '{file}' to directory '{target_dir}'.")
    except Exception as e:
      print(f"Error organizing '{file}': {e}")

# Get user input for path and organization mode
path = input("Enter path: ")
valid_modes = ["type", "size"]
while True:
  mode = input("Choose organization mode (type or size): ").lower()
  if mode in valid_modes:
    break
  else:
    print(f"Invalid mode. Please choose from {', '.join(valid_modes)}.")

# Call the organize_files function with user-provided options
if mode == "size":
  size_limit = int(input("Enter size limit in MB (defaults to 10): ") or 10) * 1024 * 1024
  organize_files(path, mode, size_limit)
else:
  organize_files(path, mode)  # No size_limit needed for type mode
