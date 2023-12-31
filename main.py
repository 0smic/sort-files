import os
import shutil
import argparse

auhtor = "Gokul B"

parser = argparse.ArgumentParser(description="Hello it worked")

parser.add_argument(
    "--dirpath",
    "-d",
    nargs = 1,
    help="The path of the directory to sort."
)
args = parser.parse_args()


if args.dirpath:
    source_directory = r'' + args.dirpath[0]
    print(f"Sorting files in the {source_directory}")


image_folder = "images"
exe_folder = "executable"
pdf_folder = "pdfs"
docx_folder = "docx"
zip_folder = "zip"
video_folder = "videos"

# Create folders if they do not exist
for folder in [image_folder, exe_folder, pdf_folder, docx_folder, zip_folder, video_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def get_file_type(file_path):
    file_type = None
    file_extension = file_path.split('.')[-1].lower()
    if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
        file_type = "image"
    elif file_extension in ["docx", "doc"]:
        file_type = "docx"
    elif file_extension == 'pdf':
        file_type = "pdf"
    elif file_extension == "exe":
        file_type = "exe"
    elif file_extension == "zip":
        file_type = "zip"
    elif file_extension in ["mp4", "mkv"]:
        file_type = "video"
    return file_type

def move_file(file_path, dest_folder):
    file_name = os.path.basename(file_path)
    dest_path = os.path.join(dest_folder, file_name)
    shutil.move(file_path, dest_path)

# Walk through the source directory and organize files
for dirpath, dirnames, files in os.walk(source_directory):
    for file in files:
        file_path = os.path.join(dirpath, file)
        file_type = get_file_type(file_path)
        if file_type == 'image':
            move_file(file_path, image_folder)
        elif file_type == 'pdf':
            move_file(file_path, pdf_folder)
        elif file_type == 'exe':
            move_file(file_path, exe_folder)
        elif file_type == "docx":
            move_file(file_path, docx_folder)
        elif file_type == "zip":
            move_file(file_path, zip_folder)
        elif file_type == "video":
            move_file(file_path, video_folder)

print("Process Finished")
