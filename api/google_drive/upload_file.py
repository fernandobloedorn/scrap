from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

import authentication

def upload_file(fileName):

    gauth = GoogleAuth()
    authentication.GoogleDriveAuthentication(gauth)

    drive = GoogleDrive(gauth)

    file = drive.CreateFile({"parents":  [{'id': '1T9xL8H5cSmqJAyVRCun8MTqBgzYiv9-w'}], 'title': fileName}) # id da pasta Mais Trading
    file.Upload()