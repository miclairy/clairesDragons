import boto3;
from botocore.client import Config

BUCKET = 'dragon-images'
config = Config(
        region_name = 'eu-north-1',
        signature_version = 's3v4',
)

def galleryImages():
    s3_client = boto3.client('s3', config=config)
    response = s3_client.get_object(Bucket=BUCKET, Key='img-bPbi2DPYdr4mv6Q0lLUdoZK6.png')
    # image = response['Body'].read()
    url = s3_client.generate_presigned_url('get_object',
                                Params={
                                    'Bucket': BUCKET,
                                    'Key': 'img-bPbi2DPYdr4mv6Q0lLUdoZK6.png',
                                },                                  
                                ExpiresIn=3600)
    print(url)
    return url
    #clairesDragons:6n=oBR3# OSKpXoC1JvPAInm