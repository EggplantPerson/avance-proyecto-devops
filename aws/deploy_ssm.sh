#!/bin/bash

INSTANCE_ID=$1

aws ssm send-command \
--document-name "AWS-RunShellScript" \
--targets "Key=instanceIds,Values=$INSTANCE_ID" \
--parameters commands=["docker run -d -p 5000:5000 devops-app"]