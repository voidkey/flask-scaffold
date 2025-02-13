import os
from datetime import datetime

from flask import jsonify, request, current_app
from app.api.v1 import api_v1_bp
from app import cos
from app.service import xxx_service
from app.util import helper


@api_v1_bp.route('/xxx_api', methods=['POST'])
def xxx_api():
    try:
        req = request.get_json()
        if not req:
            return jsonify({"status": "error", "message": "No JSON data provided"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    # 下载文件
    file_path = f"{current_app.config['TEMP_FOLDER']}/{int(datetime.now().timestamp() * 1000)}-{helper.generate_random_string(3)}.pptx"
    cos.download(req['object'], file_path)

    # 调用service方法
    res = xxx_service.xxx_service_function(file_path)

    # 删除临时文件
    os.remove(file_path)

    # 返回提取的备注内容
    return jsonify({'res': res})
