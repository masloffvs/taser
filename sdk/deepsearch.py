def has_str(file_path, word):
  with open(file_path, 'r') as file:
    # read all content of a file
    content = file.read()
    # check if string present in a file
    if word in content:
      return True

  return False