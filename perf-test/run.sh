#!/bin/bash
set -e

TARGET_URL=$1

if [ "$TARGET_URL" == "" ]; then
  echo Error: please supply Jiangren CMS URL.
  echo Example: ./run.sh http://58.18.43.23/
  exit 1
fi

echo "Please access locust via http://127.0.0.1:8089 once docker finished with 'Starting web monitor at *:8089' message."
docker run --rm -it -p 8089:8089 -w /app -v $(pwd):/app quay.io/wantedly/locust -f /app/locustfile.py -H $TARGET_URL   
