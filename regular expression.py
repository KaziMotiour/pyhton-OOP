import re
patterns = ['Team1', 'Team2']
text = "This is a starting with Team1, not to others"

# for pattern in patterns:
#     print("I'm searching for: "+pattern)
#     if re.search(pattern,text):
#     #if pattern in text:
#         print("Match")
#     else:
#         print("Not Match")

# match = re.search('Team1',text)
# print(match.start())

textSplit = re.split('s', text)
print(textSplit)