# BitScan
Project for Python
# Bitcoin kursa izmaiņu paziņošanas sistēma

## Projekta uzdevums
Šis projekts ir automatizēta sistēma, kas uzrauga Bitcoin cenu eiro valūtā un nosūta paziņojumus Telegram kanālā, ja cena ir mainījusies par noteiktu slieksni. Šī sistēma ir noderīga investoriem un kriptovalūtu entuziastiem, kas vēlas saņemt ātrus un precīzus paziņojumus par tirgus svārstībām.

## Izmantotās Python bibliotēkas un to nozīme
Projektā tiek izmantotas šādas Python bibliotēkas:
- **requests** – nepieciešama, lai veiktu HTTP pieprasījumus uz [CoinGecko API](https://www.coingecko.com/), kas nodrošina informāciju par Bitcoin cenu.
- **time** – tiek izmantota, lai kontrolētu laika intervālus starp pieprasījumiem un atkārtotu mēģinājumus kļūmju gadījumā.

Šīs bibliotēkas nodrošina uzticamu datu iegūšanu un paziņojumu nosūtīšanu uz Telegram platformu.

## Izmantotās datu struktūras
Projektā tiek definētas šādas datu struktūras:
- **float** – tiek izmantots, lai saglabātu un apstrādātu Bitcoin cenu eiro.
- **dict** – tiek izmantots, lai strukturētu datus, kas tiek nosūtīti uz Telegram API.
- **string** – tiek izmantots ziņojumu sagatavošanai un formatēšanai pirms nosūtīšanas uz Telegram.

## Programmatūras izmantošanas metodes
1. **Skripta palaišana**: Programma tiek palaista, izsaucot `main()` funkciju, kas sākotnēji iegūst Bitcoin cenu un pēc tam regulāri pārbauda cenu izmaiņas.
2. **Datu iegūšana**: Cenas tiek iegūtas, izmantojot `get_btc_price_eur()`, kas nosūta pieprasījumu uz CoinGecko API.
3. **Ziņojumu nosūtīšana**: Ja cena ir mainījusies par slieksni (definēts kā `THRESHOLD`), tiek izsaukta `notify_change()`, kas formatē ziņojumu un nosūta to uz Telegram, izmantojot `send_telegram_message()`.
4. **Atkārtoti mēģinājumi**: Gadījumā, ja pieprasījumi neizdodas, programmatūra veic atkārtotus mēģinājumus (`MAX_RETRIES`) un gaida (`time.sleep(5)`), lai nodrošinātu stabilu darbību.

---
n gaida (time.sleep(5)), lai nodrošinātu stabilu darbību.
