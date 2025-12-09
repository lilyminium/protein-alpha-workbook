# Running yammbs benchmark on different UCI hardware

The scripts and plots here demonstrate how to, and the effect of, running yammbs benchmarks on particular hardware.

Most of the `.py` scripts are copied wholesale from the yammbs-dataset-submission repo, as are the datasets. 

`run-benchmark-yammbs-*.sh` demonstrate use of the `--nodelist` constraint. Note, as implied by the name, `nodelist` allows a list of values. You can see node specs [here](https://rcic.uci.edu/hpc3/specs.html#node-details).

Note, you can also specify hardware with constraints using `--constraint`. The particular nodes/constraints you can list on UCI with:

```
$ sinfo --format="%N %f"
NODELIST AVAIL_FEATURES
hpc3-14-[00-31],hpc3-15-[00-31],hpc3-17-[00-19],hpc3-20-[00-20,23-32],hpc3-21-[16-17],hpc3-22-[05-13] intel,avx512,mlx5_ib
hpc3-18-[00-01],hpc3-19-[00-01,03-07,09-11,18-19],hpc3-l18-00 amd,epyc,epyc7601,mlx5_ib
hpc3-24-[00-02] intel,avx512,mlx5_ib,nvme,fastscratch,hbm
hpc3-19-[12,14-16] intel,mlx4_ib
hpc3-19-13 intel,mlx5_ib
hpc3-20-[21-22],hpc3-21-[00-15,18-32],hpc3-22-[00-04,14,17],hpc3-23-[00-18],hpc3-gpu-l54-[03-06] intel,avx512,mlx5_ib,nvme,fastscratch
hpc3-l18-01 amd,epyc,epyc7601,mlx4_ib
hpc3-19-17 amd,epyc,epyc7551,mlx4_ib
hpc3-l18-[04-05] intel,avx512,mlx4_ib
hpc3-gpu-16-[00-07],hpc3-gpu-17-[02-04],hpc3-gpu-18-[00-02] intel,avx512,mlx5_ib,gpugeneric
hpc3-gpu-18-[03-04],hpc3-gpu-24-[05-08],hpc3-gpu-k54-[00-08],hpc3-gpu-l54-[00-02,07-09] intel,avx512,mlx5_ib,nvme,fastscratch,gpugeneric
```

Running on nodes with different CPUs can produce substantially different results for some data points. We can see the difference in three replicates.

![same-hardware](ffs-on-same-hardware.png)

Above, the same force field on the same hardware produces identical results (by RMSD) over each replicate.

![different-hardware](ffs-on-diff-hardware.png)

Above, the same force field on different hardware produces some pretty different RMSDs. `hpc3-14-16` runs on a Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz, whereas `hpc3-19-15` runs on the older Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz.