import os
from dotenv import load_dotenv

load_dotenv()

# توکن ربات - از @BotFather بگیرید
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# آیدی عددی ادمین‌ها (با کاما جدا کنید اگر چند نفر هستند) مثال: 123456789,987654321
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

# کیف پول‌های ارز دیجیتال برای پرداخت (هیچ شماره کارتی دیگه استفاده نمیشه)
GRAM_WALLET = os.getenv("GRAM_WALLET", "UQAu5M2VScsaoQC6RMqjai4iWqEvoAalfojAbWJwUcffFqvm")  # TON
TRX_WALLET = os.getenv("TRX_WALLET", "TPFE3BacNSRygh3qfF9E2qzLGDH2GC1x49")       # TRON (TRX)
USDT_WALLET = os.getenv("USDT_WALLET", "TPFE3BacNSRy3qfF9E2qzLGDH2GC1x49")       # USDT (شبکه TRC-20)

# مسیر دیتابیس - روی Railway پیشنهاد میشه از Volume استفاده کنید تا دیتا پاک نشه
DB_PATH = os.getenv("DB_PATH", "bot.db")

# نام برند/ربات که در پیام خوش‌آمدگویی نمایش داده میشه
BRAND_NAME = os.getenv("BRAND_NAME", "CR")

# آیدی پشتیبانی (بدون @) - در دکمه «ارتباط با پشتیبانی» استفاده میشه
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "CYBRSupport")

# تنظیمات سیستم رفرال (دعوت دوستان)
REFERRAL_REQUIRED_COUNT = int(os.getenv("REFERRAL_REQUIRED_COUNT", "3"))   # تعداد خرید موفق لازم

# تعرفه‌های پیش‌فرض سرویس ها - فقط در اولین اجرا استفاده میشه
DEFAULT_MULTI_PLANS = [
    ("تک کاربره نامحدود یک‌ماهه", 150000),
    ("دو کاربره نامحدود یک‌ماهه", 250000),
    ("تک کاربره نامحدود دو‌ماهه", 250000),
    ("دو کاربره نامحدود دو‌ماهه", 450000),
]
