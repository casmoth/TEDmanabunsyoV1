# import
import pyperclip # コピーするためのモジュール（使用するためにはpip install pyperclipをする必要があります！）


# ファイルのパス / file path （MacならFinder開いて、入れたいファイルにControl押しながらクリックして、Optionキー押すとパスをコピーすると出るのでコピーする）
file_path = ""


# 1
# 入力 / input
while True:
    try:
        link = str(input("リンク（例：https://www.ted.com/）："))
        if link[0:20] == "https://www.ted.com/":
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
        output_mode = int(input("出力するデータの型（txtデータなら1, wordデータなら2, コピーなら3）："))
        if output_mode == 1 or output_mode == 2 or output_mode == 3:
            print("出力データの型入力完了")
            print("-----------------------------------------------------")
            break
        else:
            print("無効な入力です。")
            print("-----------------------------------------------------")

    except ValueError:
        print("無効な入力です。")
        print("-----------------------------------------------------")
    

# 3
data = "aaa" # テスト



# 4



# 5 txt_data
if output_mode == 1:
    file_path += "/TED.txt" # テキストデータのパスに/TED.txtを加えてTED.txtというファイルの名前を作る

    with open(file_path, mode='w') as f:
        f.write(data) # ファイルがなかったら作り、ファイルがあったら上書きして出力
    
    print("ファイル作成完了！")
    print("-----------------------------------------------------")

# 5 wordデータ
elif output_mode == 2:
    file_path += "/TED.docx" # テキストデータのパスに/TED.docxを加えてTED.docxというファイルの名前を作る

    with open(file_path, mode='w') as f:
        f.write(data) # ファイルがなかったら作り、ファイルがあったら上書きして出力

    print("ファイル作成完了！")
    print("-----------------------------------------------------")

elif output_mode == 3:
    pyperclip.copy(data)

    print("ファイル作成完了！")
    print("-----------------------------------------------------")


# 出力 / output
# 6
print("出力完了！！")
