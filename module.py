#載入內建的 sys 模組並取得資訊
# import sys as s
# print(s.platform)
# print(s.maxsize)

# 建立 geometry 模組，載入使用
# import geometry
# result=geometry.distance(0,0,3,4)
# print(result)
# result=geometry.slope(0,0,3,4)
# print(result)

# 調整搜尋模組的路徑
# import sys
# sys.path.append("modules") # 在模組的搜尋路徑列表中【新增路徑】
# print(sys.path) #印出模組的搜尋路徑列表
# import geometry
# print(geometry.distance(0,0,3,4))

import sys
sys.path.append("done") # 在模組的搜尋路徑列表中【新增路徑】
print(sys.path) #印出模組的搜尋路徑列表
