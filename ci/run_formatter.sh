#!/bin/bash
set -e

poetry run black --check --diff json_db
