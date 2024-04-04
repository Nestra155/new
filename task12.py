'''
Дана строка.s Удалите изe этой строки все символы @.
'''
# Дана строка
s = "user@example.com"

# Удаление символов "@"
result = s.replace('@', '')

print(result)