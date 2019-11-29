import argparse

from google_drive_backup import GoogleDriveBackupCreator

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Directory name to backup")

args = parser.parse_args()

gdrive_backup_creator = GoogleDriveBackupCreator()
gdrive_backup_creator.backup(args.dir)

