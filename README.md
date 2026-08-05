# ⚡ CR TG-Bot — Telegram Reseller Bot

A complete Telegram reseller bot for selling VPN/panel services with **card-to-card payment**, **manual admin approval**, and **automatic delivery** to the customer.

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=2400&pause=900&color=00F0FF&center=true&vCenter=true&width=640&lines=Full+Telegram+Reseller+Bot;Card-to-Card+Payment+%2B+Wallet;Referral+System+%2B+Discount+Codes;Auto-Delivery+After+Admin+Approval;One+Port.+SQLite.+Zero+Cost." alt="Typing animation" />

</div>

## ✨ Features

| | |
|---|---|
| 🛍️ **Two service types** | Gaming plans (volume-based) + Multi-location plans (user-based) |
| 💳 **Card-to-card payment** | Receipt upload → admin approval → auto delivery |
| 💰 **Built-in wallet** | Instant wallet payment, admin top-up approval, tiered recharge bonus |
| 🤝 **Permanent referral commission** | % of every successful purchase credited instantly to the referrer's wallet |
| 🎟️ **Discount codes** | Admin-created coupons with custom percent & usage capacity |
| 🖥️ **"My Services"** | Every order with live status + delivered configs kept per user |
| 🛠️ **Full admin panel** | Tariffs, welcome text, rules, referral % , coupons, wallet bonus — all editable from inside the bot |
| 🛡️ **Rate limiting** | Built-in anti-spam middleware (0.7s messages / 0.4s callbacks) |
| 🗄️ **SQLite + WAL** | Zero external DB, crash-proof path handling, fast concurrent reads |

<!-- animated feature icons -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#00f0ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
  <path d="M13 2 L4.5 13.5 H11 L9.5 22 L19.5 9.5 H12.5 Z">
    <animate attributeName="opacity" values="1;0.35;1" dur="1.6s" repeatCount="indefinite"/>
  </path>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 2 L20 6 V12 C20 17 16.5 20.5 12 22 C7.5 20.5 4 17 4 12 V6 Z"/>
  <path d="M9 12 L11 14 L15.5 9.5">
    <animate attributeName="stroke-dashoffset" values="0" dur="0s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.4;1" dur="2.2s" repeatCount="indefinite"/>
  </path>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="3">
    <animate attributeName="r" values="3;4;3" dur="2s" repeatCount="indefinite"/>
  </circle>
  <path d="M19.4 15 C20.4 13.8 21 12.9 21 12 C21 11.1 20.4 10.2 19.4 9"/>
  <path d="M4.6 9 C3.6 10.2 3 11.1 3 12 C3 12.9 3.6 13.8 4.6 15"/>
  <path d="M12 21 C12.9 21 13.8 20.4 15 19.4"/>
  <path d="M9 4.6 C10.2 3.6 11.1 3 12 3 C12.9 3 13.8 3.6 15 4.6"/>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
  <rect x="3" y="11" width="18" height="2" rx="1">
    <animate attributeName="y" values="11;10.6;11" dur="1.4s" repeatCount="indefinite"/>
  </rect>
  <path d="M3 11 L5.5 6 H18.5 L21 11"/>
  <path d="M7 11 V19 M11 11 V19 M15 11 V19 M19 11 V19"/>
</svg>
<br/>
<b>Payment • Security • Wallet • Delivery</b>
</div>

## 🚀 Deploy on Railway

```bash
# 1. Create a bot token
#    @BotFather  →  /newbot  →  copy the token

# 2. Get your numeric ID
#    @userinfobot  →  this is your ADMIN_IDS

# 3. Push this repo to GitHub and connect it in Railway:
#    New Project → Deploy from GitHub repo
#    Railway auto-detects the Dockerfile.
```

Then set these **Variables** in the project:

| Key | Value |
|---|---|
| `BOT_TOKEN` | Token from BotFather |
| `ADMIN_IDS` | Numeric admin ID(s), comma separated |
| `CARD_NUMBER` | Card number shown to buyers |
| `CARD_HOLDER` | Card holder name |
| `DB_PATH` | `/data/bot.db` (see volume step) |
| `BRAND_NAME` | Brand shown in welcome message (default `CR`) |
| `SUPPORT_USERNAME` | Support username without `@` (default `CYBRSupport`) |
| `REFERRAL_REQUIRED_COUNT` | Successful purchases needed for the referral gift (default `3`) |
| `REFERRAL_REWARD_VOLUME` | Gift volume in GB (default `50`) |

### 💾 Database persistence (IMPORTANT)

> Railway resets the filesystem on every deploy. To keep orders:

1. Open **Volumes** tab → create a volume mounted at `/data`
2. Keep `DB_PATH=/data/bot.db` set

The bot is now **crash-proof**: it auto-creates the database directory on startup, so a missing volume or a fresh mount can never break it again with `unable to open database file`.

## 🧭 Main Menu

```
🛍️ Buy Service  |  🖥️ My Services
💰 Wallet       |  💬 Support
🤝 Invite       |  📜 Rules
🛠️ Manage Bot   (admins only)
```

## 🛒 Purchase Flow

`Buy Service` → pick service (Gaming / Multi-location) → pick tariff → order summary + card number with buttons:
**📤 Send Receipt** · **💰 Pay with Wallet** (if balance is enough) · **🔙 Back**

Admin gets the order with **✅ Approve / ❌ Reject** buttons. After approval, the admin sends the panel/config info and the bot **delivers it automatically** to the buyer.

## 🛠️ Admin Panel (`/admin` or menu button)

- **Tariffs** — edit price, enable/disable, add new plans
- **✉️ Welcome message** — fully customizable HTML
- **📜 Rules** — editable text
- **🤝 Referral settings** — cash commission percent per successful referral purchase
- **🎟️ Discount codes** — create/enable/disable/delete coupons
- **💳 Wallet recharge bonus** — tiered threshold + bonus percent

All settings persist in SQLite — they survive restarts as long as the volume is mounted.

## ⚡ Performance

- SQLite in **WAL mode** (`journal_mode=WAL`, `busy_timeout=10s`, `synchronous=NORMAL`) — concurrent reads never block, no more database-lock crashes
- Auto-created DB directory — deploy on any host without volume config
- Anti-spam rate limiting on all messages and callbacks

## 🗂️ Files

```
├── bot.py           # Main bot + all handlers + admin panel
├── config.py        # Env vars, defaults, default tariffs
├── database.py      # SQLite layer (WAL, auto-mkdir, 50+ queries)
├── requirements.txt
├── Dockerfile
├── railway.json
├── env.example
└── .gitignore
```

---

<div align="center">
<br/>
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%" />

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 20 20">
  <path d="M10 18 C 4 12, 2 8, 2 5 C 2 2, 5 1, 7 3 C 8 4, 9 5, 10 6 C 11 5, 12 4, 13 3 C 15 1, 18 2, 18 5 C 18 8, 16 12, 10 18 Z" fill="#f43f5e">
    <animate attributeName="opacity" values="1;0.35;1" dur="1.4s" repeatCount="indefinite"/>
  </path>
</svg>

**⚡ CR TG-Bot — Sell. Approve. Deliver. Repeat.** ⚡

</div>
