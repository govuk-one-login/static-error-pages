#!/usr/bin/env python3

from __future__ import print_function
from crhelper import CfnResource

import logging
import boto3

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120, ssl_verify=None)

try:
  s3 = boto3.resource('s3')
  logger.info("Created boto3 S3 resource")

  with open("index.html") as f:
    logger.info("Able to open index.html")

except Exception as e:
  helper.init_failure(e)

@helper.create
@helper.update
def updateBucket(event, context):
  logger.info("Got Create or Update")
  properties = event["ResourceProperties"]
  bucket = s3.Bucket(properties["BucketName"])

  try:
    with open("index.html", 'rb') as f:
      bucket.put_object(Key='cloudfront-error/index.html', Body=f, ContentType='text/html')
  except Exception:
    logger.critical('Could not upload to S3')
    raise


@helper.delete
def no_op(_, __):
  pass

def handler(event, context):
  helper(event, context)
