#!/usr/bin/env bash

# cd /d4/src

uvicorn main:app --proxy-headers --host 0.0.0.0 --port 3000
