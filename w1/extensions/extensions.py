def main():
    enter=input("File name: ").lower().strip()
    if enter.endswith(".gif"):
        print("image/gif")
    elif enter.endswith(".jpeg") or enter.endswith(".jpg"):
        print("image/jpeg")
    elif enter.endswith(".png"):
        print("image/png")
    elif enter.endswith(".pdf"):
        print("application/pdf")
    elif enter.endswith(".txt"):
        print("text/plain")
    elif enter.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()