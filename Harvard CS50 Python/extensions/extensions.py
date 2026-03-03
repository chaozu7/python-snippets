file_type = input("File type: ")
file_type = file_type.casefold().strip()
file_extension = file_type.split(".")
file_extension = file_extension[-1].strip()


if len(file_extension) > 1:
    match file_extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")