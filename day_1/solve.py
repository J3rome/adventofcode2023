import argparse
import sys
from typing import List
from pathlib import Path
import re

parser = argparse.ArgumentParser("aoc 2023 challenge")
parser.add_argument("-f", "--first_part", action="store_true", help="Will run first part of the challenge")
parser.add_argument("-s", "--second_part", action="store_true", help="Will run second part of the challenge")
parser.add_argument("-t", "--test_with_example", action="store_true", help="Will run the challenge using the example input")
parser.add_argument("-i", "--input_path", type=str, default="input.txt", help="Path to input file")
parser.add_argument("-e", "--example_path_prefix", type=str, default="example_part", help="Prefix of example files for each parts")

# ======= Solution

def first_part(input_lines: List[str]) -> str:
  answer = 0

  for line in input_lines:
    line_digits = [int(n) for n in line if n.isdigit()]
    answer += int(f"{line_digits[0]}{line_digits[-1]}")

  return str(answer)


DIGIT_FINDER_REGEX=re.compile(r'(?=(1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine))')


def second_part(input_lines: List[str]) -> str:
  digits_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  digits_str_to_val = {d: i for i,d in enumerate(digits_str)}

  answer = 0
  for line in input_lines:
    digits = DIGIT_FINDER_REGEX.findall(line)

    line_digits = [d if d.isdigit() else digits_str_to_val[d] for d in digits]

    answer += int(f"{line_digits[0]}{line_digits[-1]}")

  return str(answer)


# ======= Boilerplate

def read_file(input_path: Path):
  if not input_path.exists():
    print(f"[ERROR] Can't load input '{input_path}'. File doesn't exists")
    exit(3)

  with open(input_path, 'r') as f:
    return [l.strip() for l in f.readlines()]

def write_result_to_file(output_path: Path, result: List[str]):
  with open(output_path, "w") as f:
    f.write("\n".join(result))

def main(args):
  if args.first_part:
    part_id = 1
  elif args.second_part:
    part_id = 2
  else:
    print("[ERROR] Must specify either -f/--first_part or -s/--second_part")
    exit(2)

  if args.test_with_example:
    example_path = f"{args.example_path_prefix}{part_id}"
    input_lines = read_file(Path(example_path))
  else:
    input_lines = read_file(Path(args.input_path))

  if args.first_part:
    result = first_part(input_lines)
  elif args.second_part:
    result = second_part(input_lines)

  if args.test_with_example:
    print(f"Answer for example : {result}")
  else:
    print(f"Answer for Part {part_id} :", file=sys.stderr)
    print(result)


if __name__ == "__main__":
  args = parser.parse_args()
  main(args)
