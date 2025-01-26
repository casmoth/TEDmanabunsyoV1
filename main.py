# import



# ファイルのパス / file path （MacならFinder開いて、入れたいファイルにOptionキー押しながらでパスを取るとコピーできる）
file_path = ""


# 1
# 入力 / input
while True:
    try:
        link = str(input("リンク（例：https://www.ted.com/）："))
        if link[0] == 'h':
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
        output_mode = int(input("出力するデータの型（txtデータなら1, Google docsなら2, wordデータなら3）："))
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
data = ""



# 4


# 5 txt_data
if output_mode == 1:
    with open(file_path, mode='w') as f:
        f.write(data)
    
    print("ファイル作成完了！")
    print("-----------------------------------------------------")

# 5
elif output_mode == 2:
    pass

# 出力 / output
# 6
print("出力完了！！")
