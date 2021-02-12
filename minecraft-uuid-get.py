import requests
import pyperclip

#MojangAPIからUUID取得
print ("マインクラフトのユーザー名を入力して下さい。")
x = input()
y = requests.get('https://api.mojang.com/users/profiles/minecraft/'+x).text
print (y)
#クリップボードにコピー
pyperclip.copy(y)
print ("上の内容をクリップボードにコピーしました。Enterキーを押すことで終了できます。")
input()