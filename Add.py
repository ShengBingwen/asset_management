from datetime import datetime


def add_asset(assets, category, name, owner):
    # """添加资产"""
    # 计算下一个ID编号
    if assets:
        # 提取已有ID号中的数字部分
        last_id = max([int(asset["id"][4:]) for asset in assets if "id" in asset]) #列表推导式
        next_id = f"XXXY{last_id + 4:04d}"
    else:
        next_id = "XXXY0001"
    asset = {
        "id": next_id,
        "category": category.strip(),
        "name": name.strip(),
        "owner": owner.strip(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    assets.append(asset)
    print(
        f"✅ 已添加资产: id:{next_id} 类型：{category} 型号：{name} 归属: {owner} 添加日期: {asset['date']}"
    )
