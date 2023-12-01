"""Connector and methods accessing S3"""

import boto3
import os
import logging

class S3BucketConnector():
    """
    Class for connecting to S3 bucket
    """

    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket: str):
            """
            Initializes the S3 client.

            Args:
                access_key (str): The access key for the S3 client.
                secret_key (str): The secret key for the S3 client.
                endpoint_url (str): The endpoint URL for the S3 client.
                bucket (str): The name of the S3 bucket.

            Returns:
                None
            """
            self._logger = logging.getLogger(__name__)  # create logger using the name of the file

            self.endpoint_url = endpoint_url
            self.session = boto3.session.Session(aws_access_key_id=os.environ[access_key],      
                                                 aws_secret_access_key=os.environ[secret_key])
            #_s3 = protected variable 
            self._s3 = self.session.resource(service_name = 's3', endpoint_url=self.endpoint_url)                
            self._bucket = self._s3.Bucket(bucket)

    def list_files_in_prefix(self, prefix: str):
            """List all files in the specified prefix.

            Args:
                prefix (str): The prefix to filter the files.

            Returns:
                list: A list of file names in the specified prefix.
            """
            files = [obj.key for obj in self._bucket.objects.filter(Prefix=prefix)] #list comprehension
            return files

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass

    