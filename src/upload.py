from compgraphicscat.src import google_drive_upload


def upload():
    google_drive_upload.upload_to_google_drive(source_directory="../outputs",
                                               destination_folder_name="outputs",
                                               parent_folder_name="Computer Graphics")


upload()
