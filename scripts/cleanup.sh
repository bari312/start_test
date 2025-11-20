#!/bin/bash
set -e
echo "Cleaning up LocalStack environment..."
docker-compose down
# docker-compose down -v　でボリュームも削除可能
rm -rf /tmp/mock_prices.csv
rm -rf logs/
echo "Temporary files and logs removed."
echo "Cleanup complete."

