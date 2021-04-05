import os
from azure.storage.blob import BlockBlobService

def upload_image_to_container(path, storage_name, storage_key, storage_container_name):

    root_path = path
    path = f"{root_path}"
    file_names = os.listdir(path)

    account_name = storage_name
    account_key = storage_key
    container_name = storage_container_name

    block_blob_service = BlockBlobService(
        account_name=account_name,
        account_key=account_key
    )

    for file_name in file_names:
        blob_name = file_name
        file_path = f"{path}/{file_name}"
        block_blob_service.create_blob_from_path(container_name, blob_name, file_path)



# path = '/home/fidx/Documents/I_Testing/Azure/cognitive-services-quickstart-code/python/CustomVision/ObjectDetection/Azure_Custom_Vision_Security-Detection-System-on-Armed-Robbery-Threatening/images'

# upload_image_to_container(path, 'spidersensestorage', 'CU9OtPwY0OfpMCf+t9YyXv+39RQ/zLsAyoFRRBVMo7QUC8JDNzx8Fb0k+ia3uvn972nZTJOMlpZE1nImY9AScw==', 'spidersensecontainer')