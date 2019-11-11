import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vaulted-scholar-254612-a0766eabcf5e.json'
storage_client = storage.Client()

bucket_name = 'smoking_bucket2'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print('Bucket {} created.'.format(bucket.name))