favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
friends = ['jen', 'marc', 'edward', 'phil', 'jonh']

for friend in friends:
    if friend in sorted(favorite_languages.keys()):
        print(f"{friend.title()}, thank you for taking the poll.")
    else:
        print(f"{friend.title()}, please take our poll!")
