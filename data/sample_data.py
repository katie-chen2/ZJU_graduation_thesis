import json
import random
import os

def sample_json_data(input_file, output_file, total_items=2000, sample_size=100):
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"输入文件不存在: {input_file}")
        
        # 读取JSON文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 验证数据格式
        if not isinstance(data, list):
            raise ValueError("JSON数据格式必须为列表")
        
        # 确保数据量足够
        if len(data) < total_items:
            raise ValueError(f"文件中的数据不足 {total_items} 条")
        
        # 截取前total_items条数据
        selected_data = data[:total_items]
        
        # 随机抽样
        if sample_size > total_items:
            raise ValueError("抽样数量不能大于总数据量")
        
        sampled_data = random.sample(selected_data, sample_size)
        
        # 写入新的JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sampled_data, f, ensure_ascii=False, indent=2)
        
        print(f"已成功从 {input_file} 中抽取 {sample_size} 条数据到 {output_file}")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 使用示例
    input_json = 'released_data.json'  # 替换为实际的输入JSON文件路径
    output_json = 'sampled_data.json'  # 替换为实际的输出JSON文件路径
    
    sample_json_data(input_json, output_json)