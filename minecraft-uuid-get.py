import sys
import requests
import pyperclip

#MojangAPIからUUID取得
x = sys.argv [1]
y = requests.get('https://api.mojang.com/users/profiles/minecraft/'+x).text
print (y)
#クリップボードにコピー
pyperclip.copy(y)
print ("I copied it to the clipboard.")