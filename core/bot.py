from core.activation import ActivationManager

class WeChatBot:
    def __init__(self):
        self.activation_manager = ActivationManager()

    def handle_message(self, message):
        user_id = message.source
        if not self.activation_manager.is_activated(user_id):
            if self.activation_manager.check_activation_code(message.content):
                self.activation_manager.activate_user(user_id)
                return "激活成功！"
            else:
                return "请提供正确的激活码。"
        else:
            return "用户已激活，可以正常使用机器人。"