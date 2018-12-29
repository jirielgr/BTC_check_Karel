import urllib2
import time
import datetime
import smtplib
from email.mime.text import MIMEText

############### User variables HERE: ###############
download_minute = 47 # every hour in this minute, default 47
port = 465  # 465 for SSL, or 25 for PLAIN  
smtp_server = "smtp.seznam.cz" # Enter SMTP server, example for seznam.cz
sender_email = "***@seznam.cz"  # Enter your address
receiver_email = "***@seznam.cz"  # Enter receiver address, can be sameas sender_email
password = "***" # Enter your password :-)
############### End of user variables ###############

data_log = [0]
data_log_time = [0]

#first_line_data = "1\n" # for test only
while True:
    data = urllib2.urlopen("https://devel.novacisko.cz/trading/position")
    first_line_data = data.readline()
    # first_line_data += "-1\n" # for test only
    first_line_data = first_line_data.replace("-1\n","SHORT")
    first_line_data = first_line_data.replace("1\n","LONG")
    print "Last data:"
    print first_line_data
    if (first_line_data != data_log[-1]):
        data_log.append(first_line_data)
        data_log_time.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        message_text = data_log[-1] + " from " + data_log_time[-1]
        if (len(data_log) > 2):
            message_text +="\n"
            message_text +=data_log[-2] + " from " + data_log_time[-2]
        if (len(data_log) > 3):
            message_text +="\n"
            message_text +=data_log[-3] + " from " + data_log_time[-3]
        msg = MIMEText(message_text)
        msg['Subject'] = ('BTC position update to %s' % first_line_data)
        msg['From'] = sender_email
        msg['To'] = receiver_email
        if (port != 25):
            send = smtplib.SMTP_SSL(smtp_server,port)
        else:
            send = smtplib.SMTP(smtp_server,port)
        send.login(sender_email,password)
        send.sendmail(sender_email, receiver_email, msg.as_string())
        send.quit()
    print "All in memory:"
    print data_log
    print data_log_time
    print ""
    minutes_time = int(datetime.datetime.now().strftime("%M"))
    if (minutes_time < download_minute):
        download_interval = (download_minute - minutes_time)*60
    else:
        download_interval = (download_minute - minutes_time + 60)*60
    print("Next download in %s s" % download_interval) 
    time.sleep(download_interval)

