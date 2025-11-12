from flask import Flask, jsonify, request
import json
import os
import Add, Delete, Save
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 新增
ASSET_FILE = "assets.json"


# 读取资产数据
def load_assets():
    if os.path.exists(ASSET_FILE):
        with open(ASSET_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# 获取所有资产
@app.route("/api/assets", methods=["GET"])
def get_assets():
    assets = load_assets()
    return jsonify(assets)


# 添加新资产
@app.route("/api/assets", methods=["POST"])
def add_asset():
    data = request.get_json()
    assets = load_assets()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Add.add_asset(assets, data["category"], data["name"], data["owner"])
    Save.save_assets(assets)
    return jsonify({"message": "资产已添加", "total": len(assets)})


# 删除资产
@app.route("/api/assets/<asset_id>", methods=["DELETE"])
def delete_asset(asset_id):
    assets = load_assets()
    index = next((i for i, a in enumerate(assets) if a["id"] == asset_id), None)
    if index is None:
        return jsonify({"error": "资产未找到"}), 404
    Delete.delete_asset(assets, index)
    Save.save_assets(assets)
    return jsonify({"message": "资产已删除"})


if __name__ == "__main__":
    app.run(debug=True)
