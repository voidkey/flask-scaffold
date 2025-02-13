import random
import string


def generate_random_string(length: int) -> str:
    # 选择可以用于生成随机字符串的字符集（包括字母和数字）
    char_pool = string.ascii_letters + string.digits
    # 使用 random.choice 从字符池中随机选取字符并组成字符串
    random_string = ''.join(random.choice(char_pool) for _ in range(length))
    return random_string
