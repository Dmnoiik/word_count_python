with open('some_text.txt', 'r') as text_file:
    text = text_file.readlines()
    lines = 0
    lines_count = [line for line in text if line != "\n"]
    print(len(lines_count))
