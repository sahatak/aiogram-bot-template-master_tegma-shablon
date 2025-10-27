from environs import Env

# environs kutubxonasidan foydalanish
import os
env = Env()

# .env fayl data papkasidan bitta yuqorida joylashgan bo‘lgani uchun:
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
env.read_env(env_path)

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili



# tekshirish uchun

# print("📂 .env yo‘li:", env_path)
# print("📄 Fayl mavjudmi:", os.path.exists(env_path))
#
# if os.path.exists(env_path):
#     print("📑 Fayl mazmuni:")
#     with open(env_path, 'r', encoding='utf-8') as f:
#         print(f.read())
#
# env.read_env(env_path)
#
# BOT_TOKEN = env.str("BOT_TOKEN")
# print(f"✅ BOT_TOKEN: {BOT_TOKEN}")
