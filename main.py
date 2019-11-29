from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import sys
import os
import mimetypes

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

# file_list = drive.ListFile(
#     {'q': "'root' in parents and trashed=false"}).GetList()

# mimetypes = {
#     # Drive Document files as MS Word files.
#     'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',

#     # Drive Sheets files as MS Excel files.
#     'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

#     # etc.
# }

# for file1 in file_list:
#     download_mimetype = None
#     if file1['mimeType'] in mimetypes:
#         download_mimetype = mimetypes[file1['mimeType']]
#         file1.GetContentFile(file1['title'], mimetype=download_mimetype)

directory = sys.argv[1]
dir_name = directory.split("/")[-1]
file1 = drive.CreateFile({'title': dir_name,
    "mimeType": "application/vnd.google-apps.folder"})
file1.Upload()

root_id = file1['id']
files = os.listdir(directory)
for file in files:
    full_name = os.path.join(directory, file)
    print("Backing up {}".format(full_name))
    mime_type = mimetypes.guess_type(full_name)[0]
    if mime_type:
        f = drive.CreateFile({ 
            'title': 'test.txt', 
            "parents": [{ "id": root_id }],
            'mimeType': mime_type})
        f.SetContentFile(full_name)
        f.Upload()
    else:
        print("Mime type for {} could not be determined".format(file))
