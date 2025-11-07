import json


def save_assets(assets, filename="assets.json"):
    """保存资产到 JSON 文件"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(assets, f, ensure_ascii=False, indent=2)

    print("💾 资产数据已保存。")
