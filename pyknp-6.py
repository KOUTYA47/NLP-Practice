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
    with open('result-knp.txt', 'w', encoding='utf-8') as f:
        f.write("句構造解析:\n")
        for mrph in juman_result.mrph_list():
            f.write(f"{mrph.midasi} ({mrph.genkei}) - {mrph.hinsi} ({mrph.bunrui})\n")
        f.write("\n")
        # 文節の情報をファイルに書き込む
        for bnst in bnst_list:
            f.write(f"文節ID: {bnst.bnst_id}, 親文節ID: {bnst.parent_id}, 主辞: {bnst.parent_id}, 係り受けタイプ: {bnst.dpndtype}\n")

if __name__ == "__main__":
    # テキストファイルから文章を Shift-JIS 文字コードで読み込む
    with open('knp.txt', 'r', encoding='cp932') as file:
        sentence = file.read()

    # 解析を実行
    parse_sentence(sentence)
