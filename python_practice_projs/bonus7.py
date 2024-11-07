filenames = ["1.Raw Data", "2.Second Data", "3.Presentations"]

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)