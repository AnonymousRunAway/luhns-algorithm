import sys

def luhn(query: str, verify: bool = False):
  """Calculates or verifies the Luhn checksum for a given number.

  Args:
    query: The number to process.
    verify: If True, verifies the checksum; otherwise, calculates it.

  Returns:
    True if the checksum is valid, False otherwise.
  """

  try:
    digits = [int(x) for x in str(query)]
  except ValueError:
    print("Invalid input: Please enter a number.")
    sys.exit(1)

  clip = -1 if verify else len(digits)
  check_sum = 10 - (sum([x if i % 2 == 0 else x * 2 if x < 5 else (x * 2) % 10 + (x * 2) // 10 for i, x in enumerate(reversed(digits[:clip]))])) % 10
  return check_sum == digits[-1] if verify else check_sum

if __name__ == "__main__":
  number = input("Enter a number: ")
  print(luhn(number, verify=True))