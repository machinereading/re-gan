#!/bin/bash

file="word2vec_gru_noise_drop_adv"
if [ $# -gt 0 ]; then
    file=$1
fi

if [ ! -d ./model/$file ]; then
    mkdir ./model/$file
    mkdir ./log/$file
    mkdir ./log/$file/train
    mkdir ./log/$file/test
    mkdir ./stats/$file
fi

#rm -r ./model/$file/*
rm -r ./log/$file/train/*
rm -r ./log/$file/test/*
#rm -r ./stats/$file/*

python3 bag_runner.py --name $file --epoch 30 \
    --dataset kaist \
    --lrate 0.001 \
    --embed ../data/kaist/embedding/fasttext/vector_np_100d_wikipedia.pkl \
    --model_dir ./model/$file --log ./log/$file --eval_dir ./stats/$file \
    --bag_num 50 \
    --vocab_size 1500000 \
    --L 80 \
    --entity_dim 3 \
    --enc_dim 200 \
    --cat_n 50 \
    --cell_type gru \
    --lrate_decay 0 \
    --report_rate 0.2 \
    --seed 57 \
    --test_split 1000 \
    --clip_grad 1 \
    --gpu_usage 0.9 \
    # --dropout 0.5 \
    # --adv_eps 0.25
    # --tune_embed
