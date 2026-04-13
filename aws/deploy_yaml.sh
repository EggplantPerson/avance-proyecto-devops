#!/bin/bash

aws cloudformation deploy \
--template-file template.yaml \
--stack-name devops-stack \
--capabilities CAPABILITY_NAMED_IAM