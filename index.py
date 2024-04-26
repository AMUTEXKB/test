from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace with your storage account name and account key
storage_account_name = "csb100320035ef4bba7"
storage_account_access_key = "FuzT2dpyGS/JKVdFiMgr7Zp+PZR6kwzzKfMY6WxUx8KaNeX7qbmyxa1GTI9IO3ANJKTnsAq6+Y0E+AStOghpnw=="

# Create a blob service client
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=storage_account_access_key)

# Now you can use the blob_service_client to interact with your storage account
# Replace with your container name
container_name = "amutexsimple"

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# List all blobs in the container
blob_list = container_client.list_blobs()

# Print all blob names
for blob in blob_list:
    print(blob.name)
