# 先清洗后过滤
def clear_data(s):
    try:
        return int(s)
    except ValueError:
        return None

raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]
cleared = map(clear_data, raw_data)
filtered = filter(lambda x: x is not None and x >= 80, cleared)
result = list(map(lambda x: x / 100, filtered))

if any(x > 1.0 for x in result):
    print("核心过载")
else:
    print("运转正常")

# =========================================
# 先清洗后过滤(简洁版)
raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]
result = (int(i)/100 for i in raw_data if i.isdigit() and int(i) >= 80)
print("核心过载" if any(v > 1.0 for v in result) else "运转正常")