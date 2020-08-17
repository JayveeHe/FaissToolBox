# coding=utf-8

"""
Created by jayvee on 2020/8/16.
https://github.com/JayveeHe
"""

import hashlib
import io
import math
import os
import pickle
import sys

import faiss
import numpy as np

# PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# print('current file:%s, PROJECT_PATH: %s' % (__file__, PROJECT_PATH))
# sys.path.append(PROJECT_PATH)

from .utils.logger_utils import default_logger


class FaissIndexManager(object):
    def __init__(self, index_file_path=None, id_dict_path=None, dim=128, index_types='Flat'):
        if index_file_path and id_dict_path:
            default_logger.info('loading index from %s' % index_file_path)
            self.index = faiss.read_index(index_file_path, 0)
            self.id2key = pickle.load(open(id_dict_path, 'rb'))
        else:
            self.index = faiss.index_factory(dim, index_types)
            self.index = faiss.IndexIDMap(self.index)
            self.id2key = {}
        default_logger.info('index inited, is_trained=%s' % (self.index.is_trained))

    def add_vec(self, vec, id_key):
        """
        add image vector to the Index, and transform the id_key into ids.
        :param vec:
        :param id_key: string type
        :return:
        """
        ids = FaissIndexManager.str2ids(id_key)
        self.index.add_with_ids(np.array([vec]), np.array([ids]))
        self.id2key[ids] = id_key

    @staticmethod
    def str2ids(str_key):
        hash_val = hash(hashlib.md5(str_key.encode('utf8')).hexdigest())
        return hash_val

    def search_vec(self, query_vec_list, topk=5, threshold=None):
        '''
        search by vecs
        :param query_vec_list: np.array([vecs],dtype=np.float32)
        :param topk:
        :param threshold:
        :return: a tuple of (dist_list, key_list), dist_list stands for distance list
        '''
        dist_score, indexes = self.index.search(query_vec_list, k=topk)
        key_list = []
        dist_list = []
        for i in range(len(indexes)):
            tmp_key_list = []
            tmp_dist_list = []
            for j in range(len(indexes[i])):
                dist = dist_score[i][j] / math.sqrt(self.index.d)
                cur_id = indexes[i][j]
                if ((threshold and dist < threshold) or not threshold) and cur_id in self.id2key:
                    tmp_key_list.append(self.id2key[cur_id])
                    tmp_dist_list.append(dist)

            key_list.append(tmp_key_list)
            dist_list.append(tmp_dist_list)
        # key_list = [[self.id2key[b] for b in a] for a in indexes]
        return dist_list, key_list

    def save(self, index_file_path, dict_path):
        try:
            with open(dict_path, 'wb') as dict_fout:
                faiss.write_index(self.index, index_file_path)
                pickle.dump(self.id2key, dict_fout)
            print('successfully save index to %s, dict path: %s' % (index_file_path, dict_path))
        except Exception as e:
            print('error in saving dict and index file, details=%s' % (str(e)))

    def __repr__(self):
        return 'total items: %s\ndim: %s\ntotal index key: %s\n is_trained=%s' % (
            self.index.ntotal, self.index.d, len(self.id2key), self.index.is_trained)
