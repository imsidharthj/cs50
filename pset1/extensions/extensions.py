filetype = input("file nmae: ")

if filetype.endswith(".gif"):
   print(filetype,"/gif")
elif filetype.endswith(".jpg"):
   print(filetype,"/jpg")
elif filetype.endswith(".jpeg"):
   print(filetype,"/jpeg")
elif filetype.endswith(".png"):
   print(filetype,"/png")
elif filetype.endswith(".pdf"):
   print(filetype,"/pdf")
elif filetype.endswith(".txt"):
   print(filetype,"/txt")
elif filetype.endswith(".zip"):
   print(filetype,"/zip")
else :
   print("application/octet-stream")