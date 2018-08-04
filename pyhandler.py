import boto3

client = boto3.client('s3')

target_content_type = 'image/svg+xml'
file_type = '.svg'

def bucketHandler(event, content):
    print(event)

    records = event['Records']
    print(records)

    for r in records:
        bucket = r['s3']['bucket']['name']
        key = r['s3']['object']['key']

        response = client.head_object(
            Bucket=r['s3']['bucket']['name'],
            Key=r['s3']['object']['key']
        )

        print(response)
        contentType = response['ContentType']

        if key.endswith(file_type) and contentType != target_content_type:
            print('update content type')

            response = client.copy_object(
                Bucket=bucket,
                Key=key,
                CopySource=bucket + '/' + key,
                ContentType=target_content_type,
                MetadataDirective='REPLACE'
            )

            print(response)
        else:
            print('no update needed')


#            copy_source = {
#                'Bucket': bucket,
#                'Key': key
#            }
#           response = client.copy(
#                copy_source, bucket, key,
#                ExtraArgs={
#                    "Metadata": {
#                        "Content-Type": target_content_type
#                    },
#                    "MetadataDirective": "REPLACE"
#                }
#            )

#            print(response)

