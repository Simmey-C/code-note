# 原始情报
raw_info = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "

# 1. 去除首尾空格，分割成字段
clean_info = raw_info.strip()
fields = clean_info.split('; ')

# 2. 提取各字段信息
agent = fields[0].split(':')[1]
coords_str = fields[1].split(':')[1].strip('()')
coords = tuple(map(int, coords_str.split(',')))
items = list(set(fields[2].split(':')[1].split(',')))
mission = fields[3].split(':')[1]
# 截取核心任务代号
mission_code = mission.split('-')[1]

# 3. 归档到字典
agent_report = {
    "Agent": agent,
    "Coords": coords,
    "Items": items,
    "Mission": mission,
    "Mission_Code": mission_code
}

# 输出结果
print("情报解密结果：")
for key, value in agent_report.items():
    print(f"{key}: {value}")