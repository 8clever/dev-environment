def input_select (prompt: str, options: list):
  print(f"{prompt}:")
  for option in options:
    print(f" - {option}")
  response = None
  while response not in options:
    response = input("Input: ")
  return response