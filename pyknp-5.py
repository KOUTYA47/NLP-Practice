from pyknp import KNP

def parse_sentence(sentence):
    knp = KNP()
    result = knp.parse(sentence)

    # 文節のリストを取得
    bnst_list = result.bnst_list()

    # 文節のインデックスをキーにした辞書を作成
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

if __name__ == "__main__":
    sentence = "太郎は花子が読んでいる本を次郎に渡した。"
    parse_sentence(sentence)
