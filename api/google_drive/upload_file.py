from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# import authentication

def fileUpload(fileName, fileContent):

    gauth = GoogleAuth()
    # authentication.GoogleDriveAuthentication(gauth)

    drive = GoogleDrive(gauth)

    # fileName    = 'com_content.txt'
    # fileContent = 'hello.txt'

    # file = drive.CreateFile({"parents":  [{'id': '1T9xL8H5cSmqJAyVRCun8MTqBgzYiv9-w'}], 'title': fileName}) # id da pasta Mais Trading
    file = drive.CreateFile({"parents":  [{'id': '1T9xL8H5cSmqJAyVRCun8MTqBgzYiv9-w'}], 'title': fileName, 'id': '1O89Z8QK_qbOVqXNnrhW-6So_PZAazqfB'})
    file.SetContentFile(fileContent)
    file.Upload()