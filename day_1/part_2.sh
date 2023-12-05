#!/usr/bin/env bash
if [[ ${1} == "submit" ]]; then
  ANSWER="$(python solve.py --second_part)"
  if [[ -z ${ANSWER} ]]; then
    echo "No answer provided"
    exit 1
  fi

  aoc submit -l 2 "${ANSWER}"
else
  python solve.py --test_with_example --second_part
fi
