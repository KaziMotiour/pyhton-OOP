import re
def multi_find(text_patterns,phrase):
    for pat in test_patterns:
        print("Search for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')


patterns = ['Team1', 'Team2']
text = "This is a starting! with Team1, 1234567, not to others arr arrr"

# for pattern in patterns:
#     print("I'm searching for: "+pattern)
#     if re.search(pattern,text):
#     #if pattern in text:
#         print("Match")
#     else:
#         print("Not Match")

# match = re.search('Team1',text)
# print(match.start())

# textSplit = re.split('with', text)
# print(textSplit)
# print(re.findall('a', text))

# test_patterns = ['ar*']
# test_patterns = ['ar+']
# test_patterns = ['ar{2}']
# test_patterns = ['ar{1,2}']
# test_patterns = ['[^!>?]+']
# test_patterns = ['[a-z]+'] # show all the lowercase in text
# test_patterns = ['[A-Z]+'] # show all the uppercase in text
# test_patterns = [r'\d'] # show all the number in text
# test_patterns = [r'\d+'] # show all the number in text
# test_patterns = [r'\D+']  # show all the text except number in text
test_patterns = [r'\w+']   # show all the text alpha numeric in text

multi_find(test_patterns,text)