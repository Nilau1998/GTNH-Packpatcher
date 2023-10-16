#!/bin/bash

echo "Running prepare_update.py"
python3 prepare_update.py

echo "Running docker compose up -d"
docker compose up -d
sleep 15s
docker compose down

echo "Running patch_fresh_pack.py"
python3 patch_fresh_pack.py

echo "Don't forget to update the EULA and to have fun! =)"
rm -rf backup