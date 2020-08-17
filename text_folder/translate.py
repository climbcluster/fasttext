import emoji, re, normalize

def remove_emoji(line):
    #return ''.join(c for c in line if c not in emoji.UNICODE_EMOJI)
    result = []
    for c in line:
        if c not in emoji.UNICODE_EMOJI:
            result.append(c)
        else:
            result.append(" ")
    str_res = ''.join(result)
    return str_res

faces = ["😠", "😩", "😱", "😆", "😢", "😯"] #怒り、嫌悪、恐怖、喜び、悲しみ、驚き
efiles = ["ikari.txt", "keno.txt", "kyofu.txt", "yorokobi.txt", "kanashimi.txt", "odoroki.txt"]
prefiles = ["ikari_pre.txt", "keno_pre.txt", "kyofu_pre.txt", "yorokobi_pre.txt", "kanashimi_pre.txt", "odoroki_pre.txt"]

for face, efile, prefile in zip(faces, efiles, prefiles):
    with open("emoji.txt", "w", encoding="utf_8") as f1:
        with open(efile, "r", encoding="utf_8") as f2:  #ki do ai rk .txt
            lines = f2.readlines()
            for line in lines:
                if face in line:   #"😠", "😩", "😱", "😆", "😢", "😯"
                    f1.write(line)
    print(efile + "から絵文字文抽出 ", end="")

    with open(prefile, "w", encoding="utf_8") as f1:
        with open("emoji.txt", "r", encoding="utf_8") as f2:
            lines = f2.readlines()
            for line in lines:
                line = normalize.normalize(line)  #正規化
                line = re.sub("@[a-zA-Z0-9_]+|!+|\?+|。+|、+|~+|〜+|〰️+|\.+|・+|∀+|https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+", " ", line) #記号除去
                line = re.sub(r'[!-/:-@[-`{-~]', ' ', line)   #半角置換
                line = re.sub(u'[■-♯]', ' ', line)            #全角置換
                line = remove_emoji(line)          #絵文字処理
                line = re.sub(' +', ' ', line)    #複数空白をまとめる
                line = line.strip(" *")            #先頭末尾空白除去
                line = re.sub('^\n', '', line)    #空行除去
                f1.write(line)
    print("前処理完了" + prefile)