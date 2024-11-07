temperatures = [10, 12, 14]
temperatures = [str(temp) + '\n' for temp in temperatures]

file = open("files/file.txt", 'w')

file.writelines(temperatures)
print('file.txt created succesfully')