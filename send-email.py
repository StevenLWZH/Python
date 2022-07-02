# 寄送 Email 的程式

# 準備訊息物件設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "zxc0965386726@gmail.com"
msg["To"] = "steven.laiwang@gmail.com"
msg["Subject"] = "妳好，賴王"

# 寄送純文字的內容
msg.set_content("測試看看")

# 寄送多樣式的內容 (html)
# msg.add_alternative("<h3>優惠券</h3>滿五百送一百" , subtype="html")

# 連線到 SMTP Server 驗證寄件人身分並發送郵件
import smtplib
# 到網路搜尋 gmail(yahoo) smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("zxc0965386726@gmail.com", "yrdprqrlqgaepwlk")
server.send_message(msg)
server.close()