import boto3
import os
import sys
import subprocess


sess = boto3.session.Session(aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
              aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY')
sts_connection = sess.client('sts')
# Get Session Token
session_token_object = sts_connection.get_session_token(
                                                DurationSeconds=3600,
                                                SerialNumber='arn:aws:iam::YOURACCOUNTID:mfa/YOURUUSERNAME',
                                                TokenCode=sys.argv[1])
print(session_token_object)
credentials = session_token_object['Credentials']

# Update profile credentials using aws cli bash command
bash_accessKey = "aws configure set profile.YOURPROFILENAME.aws_access_key_id %s"%credentials['AccessKeyId']
bash_secretAccessKey = "aws configure set profile.YOURPROFILENAME.aws_secret_access_key %s"%credentials['SecretAccessKey']
bash_sessionToken = "aws configure set profile.YOURPROFILENAME.aws_session_token %s"%credentials['SessionToken']


process = subprocess.Popen(bash_accessKey.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

process = subprocess.Popen(bash_secretAccessKey.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

process = subprocess.Popen(bash_sessionToken.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
