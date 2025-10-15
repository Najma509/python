filename=input("enter the file name")
if'.' in filename:
  extension=filename.split('.')[-1]
  print("The file extension is:", extension)
else:
  print("No extension found in the filename")
