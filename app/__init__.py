import os
import logging

from flask import Flask
from config import config
from app.sdk.tencent_cos import TencentCOS

# 对象存储变量
cos = TencentCOS()


# 创建 Flask 应用实例
def create_app(config_name):
    app = Flask(__name__)

    # 加载不同的配置类
    app.config.from_object(config[config_name])

    # 设置临时文件目录
    temp_dir = app.config['TEMP_FOLDER']
    os.makedirs(temp_dir, exist_ok=True)

    # 注册蓝图
    from .api.v1 import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix=f'/{app.config["SERVER_NAME"]}/v1')

    # 初始化COS
    cos.init_app(app)

    # 屏蔽urllib3的warning
    urllib3_logger = logging.getLogger('urllib3')
    urllib3_logger.setLevel(logging.CRITICAL)

    return app


# 配置数据库（如果使用）
# from .models import db
# db.init_app(app)


# 应用启动时的命令行参数
if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app.run(debug=True)
