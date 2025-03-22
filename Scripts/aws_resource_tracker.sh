#!/bin/bash

#Author: Muskan Dhamani
#Date: 20-03-2025
#version: v2
#
#Purpose: This script will report the AWS resource usage
#
#AWS S3, AWS EC2, IAM, and AWS Lambda
#
#List AWS s3 buckets
echo "List of s3 buckets"
aws s3 ls

#List ec2 instances
echo "List ec2 instances"
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'

#List AWS Lambda functions
echo "Print Lambda Functions"
aws lambda list-functions

#List IAM users
echo "List IAM users"
aws iam list-users
