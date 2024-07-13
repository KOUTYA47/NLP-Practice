from pyknp import KNP

def parse_sentence(sentence):
    knp = KNP()
    result = knp.parse(sentence)

    # 文節のリストを取得
    bnst_list = result.bnst_list()

    # 文節のインデックスをキーにした辞書を作成
    bnst_dict = {bnst.bnst_id: bnst for bnst in bnst_list}

    def print_tree(node_id, indent=""):
        # 現在の文節を取得
        node = bnst_dict[node_id]

        # 現在の文節を出力
        print(f"{indent}{node.midasi}")
        new_indent = indent + "  "

        # 子ノードを再帰的に処理
        for child_id in node.children:
            print(f"{indent}  ├─ ", end="")
            print_tree(child_id, new_indent + "│ ")

    # ルートノードを探して出力
    for bnst in bnst_list:
        if bnst.parent_id == -1:  # ルートノードは親がない
            print_tree(bnst.bnst_id)

if __name__ == "__main__":
    sentence = "太郎は花子が読んでいる本を次郎に渡した。"
    parse_sentence(sentence)
