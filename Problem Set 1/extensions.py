# Main
def main():
    file = input("File name: ").lower().strip()
    print(file_type(file))


# Pass in file name and return file type
def file_type(to_check):
    if to_check.endswith(".gif"):
        return "image/gif"
    elif to_check.endswith(".jpg"):
        return "image/jpg"
    elif to_check.endswith(".jpeg"):
        return "image/jpeg"
    elif to_check.endswith(".png"):
        return "image/png"
    elif to_check.endswith(".pdf"):
        return "application/pdf"
    elif to_check.endswith(".txt"):
        return "text/plain"
    elif to_check.endswith(".zip"):
        return "application.zip"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()
