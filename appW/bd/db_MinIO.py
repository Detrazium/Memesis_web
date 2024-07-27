import os.path
from pathlib import Path
from minio import Minio as Sync_minio
from miniopy_async import Minio as Async_minio
from miniopy_async.error import S3Error


BuImg = 'Minio_img_file_'
bucket = "python-bucket"

client = Async_minio(
    endpoint="localhost:9000",
    access_key="Detraz",
    secret_key="ASDFGHASDFGH",
    secure=False
)

def create_bucket():
    sync_client = Sync_minio(
        endpoint="localhost:9000",
        access_key="Detraz",
        secret_key="ASDFGHASDFGH",
        secure=False)

    found = sync_client.bucket_exists(bucket)
    if not found:
        sync_client.make_bucket(bucket)
        print('|Корзина для картинок создана!|')
    else:
        print('Корзина |', bucket, '| already exists')

async def InpFile(file_name, file_path):
    try:
        await client.fput_object(
            bucket, file_name,file_path
        )
        print(
            'Minio успешно загрузил фото:', file_name, 'В корзину', bucket
        )
        await GetFile(file_name)
    except:
        print('Load File to minio ERROR')

async def GetFile(file_name):
    url = await client.fget_object(bucket_name=bucket, object_name=file_name, file_path='appW/images_static/'+file_name)
    return url
async def DelFile(file_name):
    await client.remove_object(bucket_name=bucket, object_name=file_name)








