def input_select (prompt: str, options: list):
  print(f"{prompt}: {', '.join(options)}")
  response = None
  while response not in options:
      response = input("Input: ")
  return response