class UnionFindSet(object):

    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        father = self.father_dict[node]
        if (node != father):
            if father != self.father_dict[father]:  # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if (a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if a_set_size >= b_set_size:
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size



if __name__ == '__main__':
    a = set()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    a.add("123123123123")
    union_find_set = UnionFindSet(a)
    union_find_set.union(1, 2)
    union_find_set.union(3, 5)
    union_find_set.union(3, 1)
    res_dict = {}
    for i in union_find_set.father_dict:
        rootNode = union_find_set.find(i)
        if rootNode in res_dict:
            res_dict[rootNode].append(i)
        else:
            res_dict[rootNode] = [i]

    keys = res_dict.keys()
    for item in keys:
        # if res_dict[item].__len__()>1:
        print(res_dict[item])
