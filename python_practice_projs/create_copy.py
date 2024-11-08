with open("files/story.txt") as file:
    content = file.read()
    
with open("files/story_copy.txt", "w") as file:
    file.write(content)