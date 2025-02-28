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
if match:
    match_data = match.group(1)
else:
    print("データ読み取りができませんでした。")
    exit()


# 4
# HTML特殊文字を通常の文字に変換
data = re.sub(r"&apos;", "'", match_data)  # &apos; を ' に変換
data = re.sub(r"&quot;", '"', data)        # &quot; を " に変換

# 空白文字の整理
data = re.sub(r'^\s+', '', data)           # 行頭の空白を削除
data = re.sub(r'\n\s+', '\n', data)        # 改行後の余分な空白を削除

# ...の前での改行防止のため、一時的にマーカーに置換
data = re.sub(r'\.{3}', 'ELLIPSIS_MARKER', data)  # ... を一時的なマーカーに置換

# 引用文の整形
data = re.sub(r'([^.])"\s+', r'\1"\n', data)    # 引用文の終わりで改行

# 文末での改行（特定の条件を除外）
data = re.sub(
    r'(?<!\w[Mm]r)(?<!\w[Mm]s)(?<!\w[Dd]r)(?<!\w[Mm]rs)'  # Mr./Ms./Dr./Mrs. を除外
    r'(?<!\d)\.(?!\d)'                                      # 数字の間のピリオドを除外
    r'(?!\s*["\'])'                                         # 引用符の前のピリオドを除外
    r'\s*', 
    '.\n', 
    data
)

# 感嘆符と疑問符での改行
data = re.sub(r'([!?])\s+', r'\1\n', data)      # !と?の後で改行

# 角括弧テキストの処理（修正版）
data = re.sub(r'\[(.*?)\]', r'[\1]\n', data) # [...] の後に改行を入れ、余分な空白と改行を削除

# ダッシュでの改行
data = re.sub(r'--\s+', '--\n', data)           # -- の後で改行

# 引用符の改行を調整
data = re.sub(r'\."\s+', '"\n', data)           # ." の後で改行

# 括弧付きテキストの処理
data = re.sub(r".Laughter. ", r'(Laughter)\n', data)  # (Laughter) に変換して改行
data = re.sub(r".Applause. ", r'(Applause)\n', data)  # (Applause) に変換して改行
data = re.sub(r".Sigh. ", r'(Sigh)\n', data)     # (Sigh) に変換して改行

# マーカーを...に戻す
data = re.sub('ELLIPSIS_MARKER', '...', data)    # 一時的なマーカーを ... に戻す

# 複数の空行を単一の改行に置換
data = re.sub(r'\n\s*\n', '\n', data)           # 複数の改行を1つに統合

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
    print("※原稿データがなかったかもしれません。")
    exit()


# 出力 / output
# 6
print("出力完了！！")
