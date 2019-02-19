#!/bin/bash
set -e
set -x
cd "$(dirname "$0")/.."


python gong/main.py
