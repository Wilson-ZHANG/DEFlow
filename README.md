# DEFlow

![cover](figures/framework.pdf)

Code release for the paper "Data-centric Entry-wise Normalizing Flows for Molecule Generation" , under review at *TKDE*.

## Environment

Install the required packages from `requirements.txt`.

**Note**: If you want to set up a rdkit environment, it may be easiest to install conda and run:
``conda create -c conda-forge -n my-rdkit-env rdkit`` and then install the other required packages. But the code should still run without rdkit installed though.

## Train

### For QM9

```python train_model.py --data_name qm9  --batch_size 256  --max_epochs 200 --gpu 0  --debug True  --save_dir=results/qm9_0516  --b_n_flow 10  --b_hidden_ch 128,128  --a_n_flow 27 --a_hidden_gnn 64  --a_hidden_lin 128,64  --mask_row_size_list 1 --mask_row_stride_list 1 --noise_scale 0.6 --b_conv_lu 1  2>&1 | tee qm9_sin_0516.log```


### For MOSES

MOSES
```python train_model.py  --data_name moses  --batch_size  256  --max_epochs 200 --gpu 0  --debug True  --save_dir=results/moses_0514   --b_n_flow 10  --b_hidden_ch 512,512  --a_n_flow 38  --a_hidden_gnn 256  --a_hidden_lin  512,64   --mask_row_size_list 1 --mask_row_stride_list 1  --noise_scale 0.6  --b_conv_lu 2  2>&1 | tee moses_0514.log```

MOSES1k
```python train_model.py  --data_name moses1k  --batch_size  256  --max_epochs 200 --gpu 0  --debug True  --save_dir=results/moses1k_0515   --b_n_flow 10  --b_hidden_ch 512,512  --a_n_flow 38  --a_hidden_gnn 256  --a_hidden_lin  512,64   --mask_row_size_list 1 --mask_row_stride_list 1  --noise_scale 0.6  --b_conv_lu 2  2>&1 | tee moses1k_0516.log```

### For Osteogenesis

```CUDA_VISIBLE_DEVICES=1 python train_model.py  --data_name osteo  --batch_size  512  --max_epochs 300 --gpu 0  --debug True  --save_dir=results/osteo_240223   --b_n_flow 10  --b_hidden_ch 1024,1024  --a_n_flow 68  --a_hidden_gnn 512  --a_hidden_lin  1024,128   --mask_row_size_list 1 --mask_row_stride_list 1  --noise_scale 0.6  --b_conv_lu 2  2>&1 | tee osteo_240223.log```

## Generation

### For QM9

```python generate.py --model_dir results/qm9_0516 -snapshot model_snapshot_epoch_200 --gpu 0 --data_name qm9 --hyperparams-path moflow-params.json --batch-size 10000 --temperature 0.85 --delta 0.05 --n_experiments 5 --save_fig false --correct_validity true 2>&1 | tee qm9_random_generation_sin_0516.log```


### For MOSES

MOSES
```python generate.py --model_dir results/moses_0514  -snapshot model_snapshot_epoch_200 --gpu  0  --data_name moses --hyperparams-path moflow-params.json   --temperature 0.85  --batch-size 10000 --n_experiments 5  --save_fig false --correct_validity true 2>&1 | tee moses_random_generation_0515.log```

MOSES1k
```python generate.py --model_dir results/moses1k_0515  -snapshot model_snapshot_epoch_200 --gpu  0  --data_name moses1k --hyperparams-path moflow-params.json   --temperature 0.85  --batch-size 10000 --n_experiments 5  --save_fig false --correct_validity true 2>&1 | tee moses1k_random_generation_0516.log```

### For Osteogenesis

```python generate.py --model_dir results/osteo_240223  -snapshot model_snapshot_epoch_200 --gpu  0  --data_name moses1k --hyperparams-path moflow-params.json   --temperature 0.85  --batch-size 10000 --n_experiments 5  --save_fig false --correct_validity true 2>&1 | tee osteo_random_generation_0516.log```


## Acknowledgements

This repo is built upon the previous work [Moflow](https://doi.org/10.1145/3394486.3403104). Thanks to the authors for their great work!
