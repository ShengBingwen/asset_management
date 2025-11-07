def show_assets(assets):
    # """显示资产"""
    if not assets:
        print("当前没有资产。")
        return

    print("=== 当前资产列表 ===")
    for i, asset in enumerate(assets, 1):
        print(
            f"[{asset['id']:<10}] [{asset['category']:<10}] [{asset['name']:<10}] [{asset['owner']:<10}] [{asset['date']:<20}]"
        )
