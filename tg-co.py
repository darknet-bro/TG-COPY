import telegram
import os, sys

print("""\033[1;32m

           (               (              *               )  (       )  
  *   )    )\ )     (      )\ )   (     (  `        (  ( /(  )\ ) ( /(  
` )  /((  (()/( (   )\ )  (()/(   )\    )\))(       )\ )\())(()/( )\()) 
 ( )(_))\  /(_)))\ (()/(   /(_)|(((_)( ((_)()\ ___(((_|(_)\  /(_)|(_)\  
(_(_()|(_)(_)) ((_) /(_))_(_))  )\ _ )\(_()((_)___)\___ ((_)(_))__ ((_) 
|_   _| __| |  | __(_)) __| _ \ (_)_\(_)  \/  |  ((/ __/ _ \| _ \ \ / / 
  | | | _|| |__| _|  | (_ |   /  / _ \ | |\/| |   | (_| (_) |  _/\ V /  
  |_| |___|____|___|  \___|_|_\ /_/ \_\|_|  |_|    \___\___/|_|   |_|   
                                                                   
                                           \033[1;36mdasturchi: @darknet_off1cial 



""")
os.system("termux-open-url https://t.me/darknet_off1cial")
darknet = input("\033[1;32mBot tokenini yozing:\033[1;36m ")
b = 1
c = 140000000000000000  
d = input("\033[1;32mQaysi kanalga Malumotlarni forward qilmoqchisiz?:\033[1;36m ")
e = input("\033[1;32mqaysi kanaldan malumotlarni jonatmoqchisiz:\033[1;36m")
auth = telegram.Bot(token=darknet)
print("\033[1;34mDastur ishga tushdi, Malumotlar ohirgacha nusxalangandan soʻng ctrl/c bosing !!")
def forward(b):
    try :
        for msg in range (b,c+1):
            telegram.Bot.forwardMessage(auth, chat_id=d, from_chat_id=e, message_id=msg)
    except telegram.error.BadRequest:
        b = msg+1
        forward(b)
        print("habarlar muvafaqiyatli kochirildi")

if __name__ == "__main__":
    forward(b)