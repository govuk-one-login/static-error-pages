#!/usr/bin/env python3

from __future__ import print_function
from crhelper import CfnResource

import logging
import boto3
import glob

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120, ssl_verify=None)
htmlFiles = glob.glob('*.html')

try:
  s3 = boto3.resource('s3')
  logger.info("Created boto3 S3 resource")

  for htmlFile in htmlFiles:
    with open(htmlFile) as f:
      logger.info(f"Able to open {htmlFile}")

except Exception as e:
  helper.init_failure(e)

@helper.create
@helper.update
def updateBucket(event, context):
  logger.info("Got Create or Update")
  properties = event["ResourceProperties"]
  bucket = s3.Bucket(properties["BucketName"])

  try:
    for htmlFile in htmlFiles:
      with open(htmlFile, 'rb') as f:
        bucket.put_object(Key=f'cloudfront-error/{htmlFile}', Body=f, ContentType='text/html')
  except Exception:
    logger.critical('Could not upload to S3')
    raise

@helper.delete
def no_op(_, __):
  pass

def handler(event, context):
  helper(event, context)
