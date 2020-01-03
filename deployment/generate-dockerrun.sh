#!/bin/bash
set -e

cat Dockerrun.aws.json.tpl | sed "s#TAG#$1#g" > Dockerrun.aws.json 
