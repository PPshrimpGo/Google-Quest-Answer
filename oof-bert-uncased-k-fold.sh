# python oof-k-fold.py --model_type "bert" --model_name "bert-base-uncased" --content "Question_Answer" --seed 2020 --n_splits 10 --valid_batch_size 32 --loss "bce" --augment --num_workers 4



# python oof-k-fold.py --model_type "bert" --model_name "bert-base-uncased" --content "Question" --seed 2020 --n_splits 5 --valid_batch_size 32 --loss "bce" --augment --num_workers 4



python oof-k-fold.py --model_type "bert" --model_name "bert-base-uncased" --content "Answer" --seed 2020 --n_splits 5 --valid_batch_size 32 --loss "bce" --augment --num_workers 4 --merge
