import json
import random
import os

ids = [186, 1116, 834, 410, 112, 468, 1684, 208, 1597, 1069, 726, 378, 1979, 916, 1285, 702, 644, 1105, 1639, 572, 1427, 1168, 1776, 354, 1182, 37, 1677, 1473, 1690, 850, 254, 1934, 673, 86, 686, 609, 1230, 642, 1759, 720, 861, 1713, 1451, 797, 1840, 929, 201, 727, 187, 309, 877, 356, 316, 1263, 1783, 129, 873, 658, 802, 1446, 1190, 459, 707, 905, 1980, 402, 1100, 899, 131, 1157, 1969, 1530, 1620, 1142, 1760, 397, 1058, 627, 1589, 880, 144, 64, 1879, 466, 1019, 1738, 280, 544, 353, 1040, 1053, 574, 729, 1481, 207, 1119, 1494, 117, 674, 1127]

def sample_json_data(input_file, output_file, ids ):
    try:
        samples = []
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"输入文件不存在: {input_file}")
        
        # 读取JSON文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 验证数据格式
        if not isinstance(data, list):
            raise ValueError("JSON数据格式必须为列表")
        
        sample_size = 0
        for item in data:
            if item['id'] in ids:
                samples.append(item)
                sample_size += 1
        
        # 写入新的JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(samples, f, ensure_ascii=False, indent=2)
        
        print(f"已成功从 {input_file} 中抽取 {sample_size} 条数据到 {output_file}")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 使用示例
    model_name = 'o1' #'claude3.7-sonnet' #'deepseek-reasoner'
    input_json = f"shield_results/{model_name}/{model_name}_gen_res_outputs_results.json"  
    output_json = f"shield_results_sample/{model_name}/{model_name}_gen_res_outputs_results.json"  

    basedir = os.path.dirname(f"shield_results_sample/{model_name}/")
    os.makedirs(basedir, exist_ok=True)

    sample_json_data(input_json, output_json, ids)