#!/usr/bin/env bash
# Install Python dependencies for all services
set -e
for svc in backend/* gateway/api-gateway; do
  if [ -f "$svc/requirements.txt" ]; then
    pip install -r "$svc/requirements.txt"
  fi
done
