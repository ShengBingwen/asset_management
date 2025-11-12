def delete_asset(assets, index):
    """删除资产"""
    try:
        removed_asset = assets.pop(index)
        print(
            f"已删除资产: {removed_asset['category']} {removed_asset['name']}{removed_asset['owner']}"
        )
    except IndexError:
        print("❌错误: 资产索引无效。")
