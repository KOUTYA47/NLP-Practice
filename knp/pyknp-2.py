from pyknp import KNP

def parse_sentence(sentence):
    knp = KNP()
    result = knp.parse(sentence)

    def print_tree(node, indent=0):
        print(' ' * indent + node.midasi)
        for child in node.children:
            print_tree(child, indent + 2)

    # 文全体の依存関係を解析
    for bnst in result.bnst_list():
        if bnst.parent is None:
            # ルートノードから木を出力
            print_tree(bnst)

if __name__ == "__main__":
    sentence = "太郎は花子が読んでいる本を次郎に渡した。"
    parse_sentence(sentence)
