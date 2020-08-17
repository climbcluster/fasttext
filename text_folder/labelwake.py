import MeCab
labels = ["label_ikari.txt", "label_keno.txt", "label_kyofu.txt", "label_yorokobi.txt", "label_kanashimi.txt", "label_odoroki.txt"]
prefiles = ["ikari_pre.txt", "keno_pre.txt", "kyofu_pre.txt", "yorokobi_pre.txt", "kanashimi_pre.txt", "odoroki_pre.txt"]
class_labels = ["__label__1", "__label__2", "__label__3", "__label__4", "__label__5", "__label__6"]   #ラベル (怒り、嫌悪、恐怖、喜び、悲しみ、驚き)=(1,2,3,4,5,6)
count_sum = 0

for label, prefile, class_label in zip(labels, prefiles, class_labels):
    count = 0  #カウンター
    with open(label, "w", encoding="utf_8") as f1:   #出力ファイル label_*.txt
        with open(prefile, "r", encoding="utf_8") as f2:
            lines = f2.readlines()
            for line in lines:
                tagger = MeCab.Tagger("-Owakati")
                word_sep = tagger.parse(line)
                f1.write(class_label + " " + word_sep)
                count += 1
    print(label + "には" + str(count) + "件格納されました。")
    count_sum += count
print("総計" + str(count_sum) + "件")