# coding: utf-8
from __future__ import unicode_literals # It is not necessary when you use python3.
from pyknp import Juman
juman = Juman(jumanpp=False)   # default is JUMAN++: Juman(jumanpp=True). if you use JUMAN, use Juman(jumanpp=False)
result = juman.analysis("下鴨神社の参道は暗かった。")
for mrph in result.mrph_list(): # 各形態素にアクセス
    print("見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
            % (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))

### (成功例) ###
#見出し:下鴨, 読み:しもがも, 原形:下鴨, 品詞:名詞, 品詞細分類:地名, 活用型:*, 活用形:*, 意味情報:自動獲得:Wikipedia Wikipedia地名, 代表表記:
#見出し:神社, 読み:じんじゃ, 原形:神社, 品詞:名詞, 品詞細分類:普通名詞, 活用型:*, 活用形:*, 意味情報:代表表記:神社/じんじゃ ドメイン:文化・芸術 カテゴリ:場所-施設 地名末尾, 代表表記:神社/じんじゃ
#見出し:の, 読み:の, 原形:の, 品詞:助詞, 品詞細分類:接続助詞, 活用型:*, 活用形:*, 意味情報:NIL, 代表表記:
#見出し:参道, 読み:さんどう, 原形:参道, 品詞:名詞, 品詞細分類:普通名詞, 活用型:*, 活用形:*, 意味情報:代表表記:参道/さんどう ドメイン:文化・芸術 カテゴリ:場所-施設, 代表表記:参道/さんどう
#見出し:は, 読み:は, 原形:は, 品詞:助詞, 品詞細分類:副助詞, 活用型:*, 活用形:*, 意味情報:NIL, 代表表記:
#見出し:暗かった, 読み:くらかった, 原形:暗い, 品詞:形容詞, 品詞細分類:*, 活用型:イ形容詞アウオ段, 活用形:タ形, 意味情報:代表表記:暗い/くらい, 代表表記:暗い/くらい
#見出し:。, 読み:。, 原形:。, 品詞:特殊, 品詞細分類:句点, 活用型:*, 活用形:*, 意味情報:NIL, 代表表記:
