from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import sys
import os
import mimetypes


class GoogleDriveBackupCreator():
    def __init__(self):
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        self.drive = GoogleDrive(g_login)
    
    def backup(self, directory):
        dir_name = directory.split("/")[-1]
        gdrive_folder = self.drive.CreateFile({
            'title': dir_name,
            "mimeType": "application/vnd.google-apps.folder"
        })
        gdrive_folder.Upload()
        gdrive_folder_id = gdrive_folder['id']
        files = os.listdir(directory)

        for file in files:
            full_name = os.path.join(directory, file)
            print("Backing up {}".format(full_name))
            mime_type = mimetypes.guess_type(full_name)[0]
            if mime_type:
                f = self.drive.CreateFile({ 
                    'title': 'test.txt', 
                    "parents": [{ "id": gdrive_folder_id }],
                    'mimeType': mime_type})
                f.SetContentFile(full_name)
                f.Upload()
            else:
                print("Mime type for {} could not be determined. Skipping".format(file))
        
        print("Directory: {} backed up successfully".format(directory))

