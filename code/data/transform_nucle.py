import json

import numpy as np

nucle_atomic_num_list = [32, 1, 0, 35, 5, 6, 7, 8, 9, 14, 15, 80, 17, 50, 82, 16, 53]  # 0 is for virtual node.
max_atoms = 40
n_bonds = 4


def one_hot_nucle(data, out_size=40):
    num_max_id = len(nucle_atomic_num_list)
#    print('data.shape[0]: ',data.shape[0])
    assert data.shape[0] == out_size
    b = np.zeros((out_size, num_max_id), dtype=np.float32)
    for i in range(out_size):
        ind = nucle_atomic_num_list.index(data[i])
        b[i, ind] = 1.
    return b


def transform_fn_nucle(data):
    node, adj, label = data
    # convert to one-hot vector
    # node = one_hot(node).astype(np.float32)
    node = one_hot_nucle(node).astype(np.float32)
    # single, double, triple and no-bond. Note that last channel axis is not connected instead of aromatic bond.
    adj = np.concatenate([adj[:3], 1 - np.sum(adj[:3], axis=0, keepdims=True)],
                         axis=0).astype(np.float32)
    return node, adj, label


def get_val_ids():
    file_path = '../data/valid_idx_nucle.json'
    print('loading train/valid split information from: {}'.format(file_path))
    with open(file_path) as json_data:
        data = json.load(json_data)
    val_ids = [idx-1 for idx in data]
    return val_ids
