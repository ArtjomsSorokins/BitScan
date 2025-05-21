import requests
import time

BOT_TOKEN = "7236306645:AAHmxVQJf-FOgl9vsVVEDuFro57H9Q54QTY"
CHANNEL_ID = "-1002658636459"

CHECK_INTERVAL = 60
THRESHOLD = 25
MAX_RETRIES = 3

def get_btc_price_eur():
    for _ in range(MAX_RETRIES):
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return float(data["bitcoin"]["eur"])
        except (requests.RequestException, KeyError, ValueError) as e:
            print(f"Kļūda, iegūstot cenu: {e}")
            time.sleep(5)
    return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload, timeout=10)
    except requests.RequestException as e:
        print(f"Kļūda, nosūtot ziņojumu uz Telegram: {e}")

def notify_change(old_price, new_price):
    change = round(new_price - old_price, 2)
    direction = "pieaudzis 📈" if change > 0 else "krities 📉"
    message = (
        f"<b>Bitcoin kursa izmaiņas</b>\n"
        f"Kurss ir {direction} par <b>{abs(change)}€</b>\n"
        f"Vecais: {old_price} €\n"
        f"Jaunais: {new_price} €"
    )
    send_telegram_message(message)

def main():
    last_price = None
    while last_price is None:
        last_price = get_btc_price_eur()
        if last_price is None:
            print("Neizdevās iegūt sākotnējo cenu. Mēģinu vēlreiz...")
            time.sleep(10)

    print(f"Sākotnējā cena: {last_price} €")
    while True:
        time.sleep(CHECK_INTERVAL)
        current_price = get_btc_price_eur()
        if current_price is None:
            continue

        if abs(current_price - last_price) >= THRESHOLD:
            notify_change(last_price, current_price)
            last_price = current_price

if __name__ == "__main__":
    main()
