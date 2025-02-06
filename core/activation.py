# /Users/xiaohe/huihuibot/core/activation.py

import os

class ActivationManager:
    def __init__(self, activation_file='config/activation_codes.txt'):
        """
        初始化 ActivationManager。
        
        :param activation_file: 存储激活码的文件路径。
        """
        self.activation_file = activation_file
        self.activation_codes = set()  # 存储激活码
        self.activated_users = set()   # 存储已激活的用户
        self.load_activation_codes()   # 加载激活码

    def load_activation_codes(self):
        """
        从文件中加载激活码。
        """
        if os.path.exists(self.activation_file):
            with open(self.activation_file, 'r') as f:
                self.activation_codes = set(line.strip() for line in f.readlines())
        else:
            print(f"警告：激活码文件 {self.activation_file} 不存在。")

    def check_activation_code(self, code):
        """
        检查用户提供的激活码是否正确。

        :param code: 用户提供的激活码。
        :return: 如果激活码正确，返回 True；否则返回 False。
        """
        return code in self.activation_codes

    def activate_user(self, user_id):
        """
        激活用户。

        :param user_id: 用户的唯一标识符。
        """
        self.activated_users.add(user_id)
        print(f"用户 {user_id} 已激活。")

    def is_activated(self, user_id):
        """
        检查用户是否已激活。

        :param user_id: 用户的唯一标识符。
        :return: 如果用户已激活，返回 True；否则返回 False。
        """
        return user_id in self.activated_users