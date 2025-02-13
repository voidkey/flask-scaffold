# 配置类
class Config:
    SERVER_NAME = 'server_name'
    SECRET_KEY = 'secret_key'
    DEBUG = False
    DATABASE_URI = 'mysql://xxx'
    PORT = 25001
    TEMP_FOLDER = 'tmp'
    # COS
    STORAGE_BUCKETS = {
        'default': {
            'STORAGE_BUCKET': '',
            'STORAGE_BASEURL': '',
            'STORAGE_SECRET_ID': '',
            'STORAGE_SECRET_KEY': '',
            'STORAGE_REGION': '',
            'STORAGE_DOMAIN': ''
        },
        'xxx': {
            'STORAGE_BUCKET': '',
            'STORAGE_BASEURL': '',
            'STORAGE_SECRET_ID': '',
            'STORAGE_SECRET_KEY': '',
            'STORAGE_REGION': '',
            'STORAGE_DOMAIN': ''
        }
    }

    # 配置项

    # 其他配置项...


# 环境特定的配置类
class DevelopmentConfig(Config):
    NAME = 'Development'
    DEBUG = True
    # 开发环境特定的配置项...
    AI_MASTER = {
        'END_POINT': '',
        'FETCH': "/ai-master/v1/run/fetch",
        'REPORT': "/ai-master/v1/run/progress",
        'START': "/ai-master/v1/run/start",
        'STOP': "/ai-master/v1/run/stop",
    }


class ProductionConfig(Config):
    NAME = 'Production'
    DEBUG = False
    # 生产环境特定的配置项...
    AI_MASTER = {
        'END_POINT': '',
        'FETCH': "/ai-master/v1/run/fetch",
        'REPORT': "/ai-master/v1/run/progress",
        'START': "/ai-master/v1/run/start",
        'STOP': "/ai-master/v1/run/stop",
    }


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
