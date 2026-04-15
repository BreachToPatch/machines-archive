#!/usr/bin/env bash
# health_check.sh — SLA test for Bee-Path
# Verifies that the Apache service is reachable and responding on port 80.
# Exit codes:
#   0 = service UP and healthy
#   1 = service DOWN or not responding

set -euo pipefail

TARGET_IP="${TARGET_IP:-192.168.56.10}"
TARGET_PORT="${TARGET_PORT:-80}"
TIMEOUT=5

echo "[*] Checking Apache on ${TARGET_IP}:${TARGET_PORT} ..."

HTTP_CODE=$(curl --silent --max-time "${TIMEOUT}" \
  --output /dev/null \
  --write-out "%{http_code}" \
  "http://${TARGET_IP}:${TARGET_PORT}/")

if [[ "${HTTP_CODE}" == "200" || "${HTTP_CODE}" == "403" ]]; then
  echo "[+] Service is UP (HTTP ${HTTP_CODE})"
  exit 0
else
  echo "[-] Service is DOWN or unexpected response (HTTP ${HTTP_CODE})"
  exit 1
fi
