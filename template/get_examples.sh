#!/usr/bin/env bash

PROBLEM_PATH=${1}
if [[ -z ${PROBLEM_PATH} ]]; then
  PROBLEM_PATH="problem.md"
  echo "Updating problem definition..."
  aoc download >/dev/null
  echo "Done"
fi

echo "Extracting examples from '${PROBLEM_PATH}'. Will store in 'example_part1' & 'example_part2'"

grep -iPzo '(?s)for example:.*?```.*?```' "${PROBLEM_PATH}"| grep -va '```\|example' |  awk -v RS= '{print > ("example_part" NR)}'

# Remove file created by aoc cli
rm -f example.txt
