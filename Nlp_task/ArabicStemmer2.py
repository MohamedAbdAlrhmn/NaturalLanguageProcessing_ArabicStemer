import tashaphyneStemmer

string = u'إذا شئت أن تحيا حياة طيبة ملؤها الرفاهية والرخاء' \
         u' وتنال رضا ربك فالزم ما أمر الله به واجتنب ما نهى عنه ، بهذا تبلغ الغاية' \
         u' ، فإن فعلت ذلك فزت بالسعادة فى الدارين الدنيا ' \
         u'والآخرة وكنت من الذين يستمعون القول فيتبعون أحسنه'

stems_list = tashaphyneStemmer.stem(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')
    print(word)
file.close()

