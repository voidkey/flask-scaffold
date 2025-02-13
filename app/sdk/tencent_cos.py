# -*- coding=utf-8
from qcloud_cos import CosConfig, CosS3Client

import sys
import logging


class TencentCOS:
    def __init__(self, app=None):
        self.clients = {}
        self.bucket = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        for bucket_name, bucket_config in app.config['STORAGE_BUCKETS'].items():
            secret_id = bucket_config['STORAGE_SECRET_ID']
            secret_key = bucket_config['STORAGE_SECRET_KEY']
            region = bucket_config['STORAGE_REGION']
            token = None
            domain = None

            config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token,
                               Domain=domain)
            client = CosS3Client(config)

            self.clients[bucket_name] = {
                'client': client,
                'bucket': bucket_config['STORAGE_BUCKET']
            }

    # 上传文件接口
    def upload(self, file_path: str, object_path: str):
        if "xxx/" in object_path:
            client = self.clients['xxx']
        else:
            client = self.clients['default']
        response = client['client'].upload_file(
            Bucket=client['bucket'],
            LocalFilePath=file_path,
            Key=object_path,
            PartSize=10,
            MAXThread=10,
            progress_callback=percentage
        )
        print(response['ETag'])

    # 生成下载 URL，未限制请求头部和请求参数
    def get_download_url(self, object_path: str) -> str:
        if "xxx/" in object_path:
            client = self.clients['xxx']
        else:
            client = self.clients['default']
        url = client['client'].get_presigned_url(
            Method='GET',
            Bucket=client['bucket'],
            Key=object_path,
            Expired=86400  # 24小时后过期
        )
        return url

    # 文件下载 获取文件到本地
    def download(self, object_path: str, file_path: str):
        if "xxx/" in object_path:
            client = self.clients['xxx']
        else:
            client = self.clients['default']
        response = client['client'].get_object(
            Bucket=client['bucket'],
            Key=object_path,
        )
        response['Body'].get_stream_to_file(file_path)


def percentage(consumed_bytes, total_bytes):
    """进度条回调函数，计算当前上传的百分比

    :param consumed_bytes: 已经上传/下载的数据量
    :param total_bytes: 总数据量
    """
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate))
        sys.stdout.flush()
