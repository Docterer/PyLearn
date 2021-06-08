"""字典学习"""
self_map = {}
self_map.setdefault("中国", "江苏省")
self_map.setdefault("江苏省", "苏州市")
self_map.setdefault("苏州市", "工业园区")
print(self_map)
keys = list(self_map.keys())
print(keys)
for key in keys:
    child_key = self_map.get(key)
    print("%s-%s" % (key, child_key))
print(self_map)

temp_dict = {"工业园区": "唯亭街道"}
self_map.update(temp_dict)
print(self_map)

# update键相同，value会更新
temp_dict2 = {"工业园区": "娄葑街道"}
self_map.update(temp_dict2)
print(self_map)

# 清空字典
self_map.clear()
print(self_map)
