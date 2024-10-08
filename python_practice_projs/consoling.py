ranking = ['John', 'Sen', 'Lisa']
name=input("Enter a name: ")

rank_len=len(ranking)
i=0
while i < rank_len:
    if name == ranking[i]:
        print(i+1)
    i+=1
