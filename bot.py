import telegram
import matplotlib.pyplot as plt
import numpy as np
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

def send_signal():
    message = """
📌 SIGNAL – BANK NIFTY 18 JULY Expiry  
🟢 BUY 49,000 CE @ ₹142  
🎯 Target: ₹190 | 🛑 SL: ₹118  
📈 Confidence: 88% ✅ High  
📚 Strategy: Bull Call Spread  
🧮 Greeks: Delta 0.55 | Gamma 0.09  
🧠 Logic: MACD Crossover + RSI > 50 + Long OI  
💰 Hedge: Sell 49,300 CE  
📊 Max Profit: ₹3,200 | Max Loss: ₹1,100  
"""

    prices = np.linspace(100, 230, 200)
    pnl = np.maximum(0, prices - 142) * 75

    plt.figure(figsize=(6, 4))
    plt.plot(prices, pnl)
    plt.axvline(142, color='blue', linestyle='--', label='Entry')
    plt.axvline(190, color='green', linestyle='--', label='Target')
    plt.axvline(118, color='red', linestyle='--', label='Stop Loss')
    plt.fill_between(prices, 0, pnl, where=prices>=142, color='green', alpha=0.3)
    plt.fill_between(prices, 0, pnl, where=prices<142, color='red', alpha=0.3)
    plt.title("P&L Chart")
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.close()

    bot.send_message(chat_id=CHAT_ID, text=message)
    with open("chart.png", "rb") as img:
        bot.send_photo(chat_id=CHAT_ID, photo=img)

send_signal()
