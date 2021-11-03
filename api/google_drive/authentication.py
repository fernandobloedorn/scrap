def GoogleDriveAuthentication(gauth):
    gauth.LoadCredentialsFile("credentials.txt")

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile("credentials.txt")