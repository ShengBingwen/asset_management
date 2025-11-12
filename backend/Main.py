# 资产管理系统
import Show, Delete, Add, Save
import json

assets = []
print("=====Asset Management System=====")
try:
    with open("assets.json", "r", encoding="utf-8") as f:
        assets = json.load(f)
except FileNotFoundError:
    print("未找到资产文件，初始化为空资产列表。")
    assets = []


while True:
    print("=====Please choose one operation!=====")
    print("1. 显示资产")
    print("2. 添加资产")
    print("3. 删除资产")
    print("4. 退出")
    choice = input("请选择操作 (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("无效选择，请重新输入。\n")
        continue
    if choice == "1":
        Show.show_assets(assets)
    elif choice == "2":
        category = input("请输入要添加的资产类型: ")
        name = input("请输入要添加的资产名称: ")
        owner = input("请输入要添加的资产归属: ")
        Add.add_asset(assets, category, name, owner)
        Save.save_assets(assets)
    elif choice == "3":
        index = int(input("请输入要删除的资产索引 (从1开始): ")) - 1
        Delete.delete_asset(assets, index)
    elif choice == "4":
        print("退出资产管理系统。")
        break
