import os
import boto3;
from botocore.client import Config
import requests
import uuid

BUCKET = 'dragon-images'
config = Config(
        region_name = 'eu-north-1',
        signature_version = 's3v4',
)
s3_client = boto3.client('s3', config=config)

def getImageUrl(imageKey):
    url = s3_client.generate_presigned_url('get_object',
                                Params={
                                    'Bucket': BUCKET,
                                    'Key': imageKey,
                                },                                  
                                ExpiresIn=3600)
    print(url)
    return url
    #clairesDragons:6n=oBR3# OSKpXoC1JvPAInm
    
def putImage(url, imageKey):
    file_dir = download(url, imageKey);
    if file_dir != None:
        with open(file_dir, 'rb') as data:
            s3_client.upload_fileobj(data, BUCKET, imageKey)
    
def download(url, imageKey):
    response = requests.get(url)
    file_dir = f'dragons/{imageKey}.png'
    if response.status_code == 200:
        directory = os.path.dirname(file_dir)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_dir, "wb") as fp:
            fp.write(response.content)
        return file_dir
        
    else:
        print(f"Failed to download the image. Status code: {response.status_code}")
        return None
