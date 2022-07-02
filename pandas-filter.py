# 載入 pandas 模組
import pandas as pd

# 篩選練習
# data = pd.Series([30, 15, 20])
# condition = data > 18
# filteredData = data[condition]
# print(filteredData)

# data = pd.Series (["您好", "Python", "Pandas"])
# condition = data.str.contains("P")
# print(condition)
# filteredData = data[condition]
# print(filteredData)

# 篩選練習 - DataFrame
data = pd.DataFrame({
    "Name":["Amy", "Bob", "Charles"],
    "Salary":[30000,50000,40000]
})
condition = data["Name"] == "Amy"
print(condition)
filteredData = data[condition]
print(filteredData)