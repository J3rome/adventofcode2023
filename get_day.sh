#!/usr/bin/env bash
set -e

DAY="${1}"
if [[ -z ${DAY} ]]; then
  echo "Must provide DAY"
  exit 2
fi

FOLDER_PATH="day_${DAY}"

if [[ -e ${FOLDER_PATH} ]]; then
  echo "${FOLDER_PATH} already exists"
  exit 3
fi

aoc new -y 2023 -d "${DAY}"
