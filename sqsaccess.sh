#!/bin/bash

# check SQS read access
aws sqs send-message --queue-url $1 --message-attributes '{"check":{"DataType":"String", "StringValue":"true"}}' --message-body '{"first":{"S":"Sample"},"second":{"N":"40"}}'
readResult=$?

# check SQS write access
aws sqs receive-message --queue-url $1
writeResult=$?

# echo the result 0 when the all the permissions are present else -1
if [ "$readResult" -eq "0"  -a  "$writeResult" -eq "0" ]
then
  echo 0
else
  echo -1
fi
