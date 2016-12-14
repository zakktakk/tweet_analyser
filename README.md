# tweet_analyzer
## やったこと
* ツイートを分かち書きにし，基本形に変換
* 上記ツイートデータから特定の品詞のみを抽出
* 成形したツイートデータに対し，word count, tf-idf, word2vecを適用し重要語,類似語っぽいものを抽出

## データ詳細
+ tweet_data : ツイートデータを格納したtsv
+ original_data : tsvからツイート部分だけを抜き出し
+ wakati : original_dataを分かち書きにし，基本形に変形
+ dripped_wakati : wakatiから特定品詞の単語のみを抜き出し
