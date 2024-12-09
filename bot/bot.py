import requests
import telebot,time
from telebot import types
import os
import requests
import telebot
from telebot import types
import random
import uuid
import re
import pycountry
import time
from mm import Payment
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,Document
token = "7907120878:AAGR03sjvPB-2D4auzYNYfhCI6eX8Evovxo" #tok
bot = telebot.TeleBot(token, parse_mode="HTML")


@bot.message_handler(commands=['start']) 
def start(message):
		
		bot.reply_to(message, "Send The File Now \n")


@bot.message_handler(content_types=['document'])
def  main(message):	
    		otp = 0
    		dd = 0
    		koko = bot.reply_to(message, "CHECKING STARTED BY BARRY...⌛").message_id
    		file_info = bot.get_file(message.document.file_id)
    		ee = bot.download_file(file_info.file_path)

    		with open("combo.txt", "wb") as w:
        		w.write(ee)

    		try:
        		with open("combo.txt", 'r') as file:
            			lino = file.readlines()
            			total = len(lino)	
            			for P in lino: 
                			try:
                    				start_time = time.time()
                    				res = Payment(P)
                    
                			except Exception as e:
                    				print(e)
                    				continue

                			try:
                    				if "challenge_required" in res:
                        				otp += 1
                        				stay = '3DS Challenge Required ❌'
                        				try:
                            					kill = res.split('"status":"')[1].split('",')[0]
                        				except:
                            					kill = ""
                        				infobin(P, stay, kill, start_time, message)
                        				try:
                            					kill = res.split('"status":"')[1].split('",')[0]
                        				except:
                            					kill = ""
                        				infobin(P, stay, kill, start_time, message)
                    				else:
                        				dd += 1
                        				try:
                            					kill = res.split('"status":"')[1].split('",')[0]
                        				except:                            
                            					kill = ""
               				except Exception as e:
                    				print(e)
                    				dd += 1

                			mes = types.InlineKeyboardMarkup(row_width=1)
                			cm1 = types.InlineKeyboardButton(f"• {P} •", callback_data='u8')
                			status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {kill} •", callback_data='u8')                
                			cm4 = types.InlineKeyboardButton(f"• OTP ✅ ➜ [ {otp} ] •", callback_data='x')
                			cm5 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
                			cm6 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
                			stop = types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
                			mes.add(cm1, status, cm4, cm5, cm6, stop)
                
                			bot.edit_message_text(chat_id=message.chat.id, message_id=koko,
                                      text='''WAITING MONEY ➜ @Barry_op ''', reply_markup=mes)

    		except Exception as e:
        						print(e)

def infobin(P, stay, kill, start_time, message):
    bin_number = P[:6]
    url = "https://bins.su"
    payload = f"action=searchbins&bins={bin_number}&bank=&country="
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; ART-L29N; HMSCore 6.13.0.321) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.303 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "max-age=0",
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"HuaweiBrowser\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'Upgrade-Insecure-Requests': "1",
        'origin': "https://bins.su",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "navigate",
        'Sec-Fetch-User': "?1",
        'Sec-Fetch-Dest': "document",
        'Referer': "https://bins.su/",
        'Accept-Language': "ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6",
    }

    api = requests.post(url, data=payload, headers=headers)
    res = re.search(r'<div id="result">(.+?)</div>', api.text, re.DOTALL)

    if res:
        bins = re.findall(r'<tr><td>(\d+)</td><td>([A-Z]{2})</td><td>(\w+)</td><td>(\w+)</td><td>(\w+)</td><td>(.+?)</td></tr>', res.group(1))
        if bins:
            bin_number, country_code, vendor, card_type, level, bank = bins[0]
        else:
            bin_number, country_code, vendor, card_type, level, bank = "", "", "", "", "", ""
    else:
        bin_number, country_code, vendor, card_type, level, bank = "", "", "", "", "", ""

    if len(country_code) == 2 and country_code.isalpha():
        country_code = country_code.upper()
        flag_offset = 127397
        flag = ''.join(chr(ord(char) + flag_offset) for char in country_code)
    else:
        flag = ""

    try:
        country = pycountry.countries.get(alpha_2=country_code)
        country_name = country.name if country else ""
    except:
        country_name = ""

    end_time = time.time()
    duration = int(end_time - start_time)

    msg = f"""
𝐕𝐁𝐕⇾ 🔰
𝐂𝐚𝐫𝐝 ⇾ {P}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⇾ {kill}
𝐌𝐚𝐬𝐬𝐚𝐠𝐞 ⇾ {stay}
━━━━━━━━━━━━━━━━━
- 𝗕𝗜𝗡 ⇾ {bin_number}
- 𝗜𝗻𝗳𝗼 ⇾ {card_type} - {level}
- 𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ {bank}
- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {country_name} {flag}
- 𝐎𝐓𝐇𝐄𝐑 ⇾ {vendor}
- 𝐓𝐢𝐦𝐞⇾ {duration}s
━━━━━━━━━━━━━━━━
◆ 𝐁𝐘: @Barry_op
    """

    bot.reply_to(message, msg)

print('Done')
while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(e)
        pass