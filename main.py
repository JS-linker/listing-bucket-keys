from sys import prefix
import boto3

# config
BUCKET_NAME = ':TODO'

PATHS = ['extension_collector/buybox/seller_central/seller_central_ad',
         'extension_collector/buybox/seller_central/seller_central_business_report']

# aws sdk session
session = boto3.session.Session(
    profile_name='js-pipeline', region_name='us-west-2')

s3 = session.resource('s3')
# get bucket all key
# objects = s3.Bucket(BUCKET_NAME).objects.all()

for path in PATHS:
    # target path
    # target file
    targetFile = "%s.csv" % (path.split('/')[-1])
    # write target file
    with open(targetFile, 'w') as f:
        for item in s3.Bucket(BUCKET_NAME).objects.filter(Prefix="%s/" % path):
            # filter contains target path and item is file no folder
            itemKey = item.key
            print(itemKey)
            if itemKey.endswith('/') == False:
                f.write("%s,%s\n" % (BUCKET_NAME, itemKey))
