file = input("File name: ").lower().strip()
if "." not in file:
    print("application/octet-stream")
else:
    ext = file.split(".")[-1]
    if ext=='gif' or ext=='png':
        print("image/" + ext)
    elif ext == 'jpg' or ext == 'jpeg':
        print("image/jpeg")
    elif ext == 'pdf' or ext == 'zip':
        print("application/" + ext)
    elif ext == 'txt':
        print("text/plain")
    else:
        print("application/octet-stream")
