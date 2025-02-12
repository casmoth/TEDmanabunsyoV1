# import
import pyperclip # コピーするためのモジュール（使用するためにはコンソールでpip install pyperclipをする必要があります！）
import requests # サイトのデータを読み取る
import re # データの編集（データ探し、ピリオドに改行を作るなど）

# ファイルのパス / file path （MacならFinder開いて、入れたいフォルダにControl押しながらクリックして、Optionキー押すとパスをコピーすると出るのでコピーする）
file_path = ""


# 1
# 入力 / input
while True:
    try:
        print("リンク例：https://www.ted.com/ ")
        print("コードを終了させたい場合、「no」と入力してください。")
        url = str(input("リンク："))
        if url == "no":
            print("コードを終了させます。")
            exit() 
        elif url.startswith("https://www.ted.com/"):
            if "/transcript" in url:
                url += "/transcript"
            print("リンク入力完了")
            print("-----------------------------------------------------")
            break
        else:
            print("無効な入力です。")
            print("-----------------------------------------------------")

    except ValueError:
        print("無効な入力です。")
        print("-----------------------------------------------------")


# 2
while True:
    try:
        output_mode = int(input("出力するデータ型（txtデータなら1, wordデータなら2, コピーなら3, コードを終了させるならno）："))
        if output_mode == "no":
            print("コードを終了させます。")
            exit()
        elif output_mode in [1, 2 ,3]:
            print("出力データ型入力完了")
            print("-----------------------------------------------------")
            break
        else:
            print("無効な入力です。")
            print("-----------------------------------------------------")

    except ValueError:
        print("無効な入力です。")
        print("-----------------------------------------------------")
    

# 3
response = requests.get(url)
pattern = r'"transcript":\s*"([^"]*?)",\s*"embedUrl"'
match = re.search(pattern, response.text)
match_data = match.group(1)


# 4
checked_data = re.sub(r'(?<!\d)(?<!Mr)(?<!Ms)(?<!Dr)(?<!Mrs)\.(?!\d)', '.\n', match_data)
data = re.sub(r"&apos;", "'", checked_data)

# 5 txt_data
if output_mode == 1 and file_path != "" and data != "":
    file_path += "/TED.txt" # テキストデータのパスに/TED.txtを加えてTED.txtというファイルの名前を作る

    with open(file_path, mode='w') as f:
        f.write(data) # ファイルがなかったら作り、ファイルがあったら上書きして出力
    
    print("ファイル作成完了！")
    print("-----------------------------------------------------")

# 5 wordデータ
elif output_mode == 2 and file_path != "" and data != "":
    file_path += "/TED.docx" # テキストデータのパスに/TED.docxを加えてTED.docxというファイルの名前を作る

    with open(file_path, mode='w') as f:
        f.write(data) # ファイルがなかったら作り、ファイルがあったら上書きして出力

    print("ファイル作成完了！")
    print("-----------------------------------------------------")

# 5 パソコンのクリップボードにコピー
elif output_mode == 3 and data != "":
    pyperclip.copy(data)

    print("ファイル作成完了！")
    print("-----------------------------------------------------")

# 5 パスが指定されていなかったり、うまく出力できなかったらエラー出力
else:
    print("エラー：出力不可")
    print("※パスが設定されていないかもしれません。")
    exit()


# 出力 / output
# 6
print("出力完了！！")
