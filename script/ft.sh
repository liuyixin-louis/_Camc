time python ft.py \
/home/dataset/cifar \
--scan-dir=/home/young/liuyixin/CAMC_disllter/experiments/resnet20-ddpg-private/2020.09.15-193705   \
                --output-csv=ft_2epoch_results.csv \
                --arch=resnet20_cifar --lr=0.1 --vs=0 -p=50 --epochs=2 \
                --compress=/home/young/liuyixin/CAMC_disllter/ft.yaml \
                -j=1 --deterministic --processes=16