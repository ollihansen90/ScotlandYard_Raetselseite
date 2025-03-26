def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        inhalt = file.read()
    return inhalt