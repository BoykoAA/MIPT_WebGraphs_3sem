import networkx as nx
from tqdm import tqdm as tq
from itertools import product, combinations


def find_cap_3_plus(G):
    K_33 = []

    for n1, n2, n3 in tq(combinations(G.nodes(), 3)):
        cap = (set(G.neighbors(n1)) & set(
            G.neighbors(n2)) & set(G.neighbors(n3)))
#         print(cap)
#         print(n1,n2,n3)

        if len(cap) >= 3:
            for sub_n1, sub_n2, sub_n3 in combinations(list(cap), 3):
                new_K33 = build_item([n1, n2, n3], [sub_n1, sub_n2, sub_n3])
                if new_K33 not in K_33:
                    K_33.append(new_K33)
#                    print(K_33_counts)
#                    print(new_K33)

    return K_33, len(K_33)


def check_K33(K_33, G):
    err = 0
    for subgr in tq(K_33):
        a, b = subgr[:3], subgr[3:]
        for (i, j) in product(a, b):
            if str(j) not in set(G.neighbors(str(i))):
                err += 1
                print(a)
                print(b)
                break
    return err


def build_item(fst_list, snd_list):
    fst_list = sorted(map(int, fst_list))
    snd_list = sorted(map(int, snd_list))
    return fst_list + snd_list if fst_list[0] < snd_list[0] else snd_list + fst_list


G = nx.read_edgelist('4.graph.txt')
K_6 = nx.complete_graph(n=7)
# G=K_6
# print('vertice_num:{}'.format(G.nodes()))
# print('edges_num:{}'.format(G.edges()))
res, num = find_cap_3_plus(G)
print(num)
err_num = check_K33(res, G)
print(err_num)
