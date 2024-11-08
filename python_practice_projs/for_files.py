languages = ['English', 'German', 'Spanish']

for language in languages:
    with open(f"files/{language}.txt", "w") as file:
        file.write(language)