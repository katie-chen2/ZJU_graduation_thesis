CUDA_VISIBLE_DEVICES=0 python -u eval.py --model_name o1 --greedy 1 --regen_exceed 1 --extra_info ""
CUDA_VISIBLE_DEVICES=0 python -u eval.py --model_name o3-mini --greedy 1 --regen_exceed 1 --extra_info ""
CUDA_VISIBLE_DEVICES=0 python -u eval.py --model_name deepseek-reasoner --greedy 1 --regen_exceed 1 --extra_info ""
CUDA_VISIBLE_DEVICES=0 python -u eval.py --model_name claude3.7-sonnet --greedy 1 --regen_exceed 1 --extra_info ""
python NewAPI.py --model_name deepseek-reasoner
python NewAPI.py --model_name o1
python NewAPI.py --model_name o3-mini
python NewAPI.py --model_name claude3.7-sonnet
# for more models, please see eval.py