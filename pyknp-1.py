from pyknp import Juman, KNP

def parse_sentence(sentence):
    # Juman++で形態素解析を実行
    juman = Juman()
    juman_result = juman.analysis(sentence)

    # KNPで構文解析を実行
    knp = KNP()
    result = knp.parse(sentence)

    # 文節のリストを取得
    bnst_list = result.bnst_list()

    # 文節のIDをキーにした辞書を作成
    bnst_dict = {bnst.bnst_id: bnst for bnst in bnst_list}

    def print_tree(node, indent="", last=True):
        # 現在の文節を出力
        prefix = indent + ("└─ " if last else "├─ ")
        print(f"{prefix}{node.midasi}")

        # 新しいインデントを準備
        new_indent = indent + ("    " if last else "│   ")

        # 子ノードを取得
        children = [child for child in bnst_list if child.parent_id == node.bnst_id]

        # 子ノードを再帰的に処理
        for i, child in enumerate(children):
            print_tree(child, new_indent, i == len(children) - 1)

    # ルートノードを探して出力
    for bnst in bnst_list:
        if bnst.parent_id == -1:  # ルートノードは親がない
            print_tree(bnst)

    print("\n句構造解析:")
    # 形態素解析結果を表示
    for mrph in juman_result.mrph_list():
        print(f"{mrph.midasi} ({mrph.genkei}) - {mrph.hinsi} ({mrph.bunrui})")

if __name__ == "__main__":
    # sentence = "太郎は花子が読んでいる本を次郎に渡した。"
    #sentence ="ある日の暮方の事である。一人の下人が、羅生門の下で雨やみを待っていた。広い門の下には、この男のほかに誰もいない。ただ、所々丹塗の剥げた、大きな円柱に、蟋蟀が一匹とまっている。羅生門が、朱雀大路にある以上は、この男のほかにも、雨やみをする市女笠や揉烏帽子が、もう二三人はありそうなものである。それが、この男のほかには誰もいない。"
    with open('knp.txt', 'r', encoding='cp932') as file:
        sentence = file.read()
    parse_sentence(sentence)
