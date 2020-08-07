import boto3


class PreSignedUrl:

    @staticmethod
    def generate_presigned_url(bucket_name, object_name, expiration):
        """Generate a presigned URL to share an S3 object    :param bucket_name: string
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
        """
        s3_client = boto3.client('s3')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)

        return response
