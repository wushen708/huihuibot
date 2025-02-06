# /Users/xiaohe/huihuibot/main.py

from core.activation import ActivationManager

def test_activation_manager():
    # 初始化 ActivationManager
    activation_manager = ActivationManager()

    # 测试激活码检查
    print("测试激活码检查：")
    print("激活码 '123456' 是否正确？", activation_manager.check_activation_code('123456'))  # 应返回 True
    print("激活码 'wrong_code' 是否正确？", activation_manager.check_activation_code('wrong_code'))  # 应返回 False

    # 测试用户激活
    print("\n测试用户激活：")
    user_id = 'user_001'
    print(f"用户 {user_id} 是否已激活？", activation_manager.is_activated(user_id))  # 应返回 False
    activation_manager.activate_user(user_id)
    print(f"用户 {user_id} 是否已激活？", activation_manager.is_activated(user_id))  # 应返回 True

if __name__ == '__main__':
    test_activation_manager()