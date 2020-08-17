# coding=utf-8

"""
Created by jayvee on 2020/8/17.
https://github.com/JayveeHe
"""

# this is a simple example to show how to build a faiss index from scratch

from faisstoolbox.FaissManager import FaissIndexManager
import numpy as np

# create index
vec_dim = 128  # dimension of your vectors
index_types_str = 'Flat'  # index type, string format, ref: https://github.com/facebookresearch/faiss/wiki/Faiss-indexes
# here we use Flat, which means we won't do any encoding and compression on raw vector

fim = FaissIndexManager(dim=vec_dim, index_types=index_types_str)

# add some rand vec by Numpy
rand_vecs = np.random.rand(1000, vec_dim)
print(rand_vecs.shape)
for i in range(len(rand_vecs)):
    vec_arr = rand_vecs[i]
    fim.add_vec(np.array(vec_arr, dtype=np.float32), str(i))
    if i % 100 == 0:
        print(i, 'done')

index_path = './demo_index.idx'
vec_key_path = './demo_vec_key.dic'
fim.save(index_file_path=index_path, dict_path=vec_key_path)

# load index and perform search
new_fim = FaissIndexManager(index_file_path=index_path, id_dict_path=vec_key_path)
test_vec = np.array(np.random.rand(1, vec_dim), dtype=np.float32)
test_vec = test_vec[0]
dist_list, key_list = new_fim.search_vec(np.array([test_vec]), topk=10)
result_list = []
for idx in range(len(dist_list)):
    result_list.append(list(zip(key_list[idx], dist_list[idx])))

print(result_list)
