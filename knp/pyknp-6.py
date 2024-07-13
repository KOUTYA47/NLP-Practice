from pyknp import Juman, KNP

def parse_sentence(sentence):
    juman = Juman()
    juman_result = juman.analysis(sentence)

    knp = KNP()
    result = knp.parse(sentence)

    bnst_list = result.bnst_list()

    bnst_dict = {bnst.bnst_id: bnst for bnst in bnst_list}

    def print_tree(node, indent="", last=True):
        prefix = indent + ("└─ " if last else "├─ ")
        print(f"{prefix}{node.midasi}")

        new_indent = indent + ("    " if last else "│   ")

        children = [child for child in bnst_list if child.parent_id == node.bnst_id]

        for i, child in enumerate(children):
            print_tree(child, new_indent, i == len(children) - 1)

    for bnst in bnst_list:
        if bnst.parent_id == -1:  
            print_tree(bnst)

    print("\n句構造解析:")
    with open('result-knp.txt', 'w', encoding='utf-8') as f:
        f.write("句構造解析:\n")
        for mrph in juman_result.mrph_list():
            f.write(f"{mrph.midasi} ({mrph.genkei}) - {mrph.hinsi} ({mrph.bunrui})\n")
        f.write("\n")
        for bnst in bnst_list:
            f.write(f"文節ID: {bnst.bnst_id}, 親文節ID: {bnst.parent_id}, 主辞: {bnst.parent_id}, 係り受けタイプ: {bnst.dpndtype}\n")

if __name__ == "__main__":
    with open('knp.txt', 'r', encoding='cp932') as file:
        sentence = file.read()

    parse_sentence(sentence)
