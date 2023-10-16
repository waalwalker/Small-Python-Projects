import pandas as pd
import datetime
import os
import smtplib

os.chdir(r"C:\Users\dhana\OneDrive - Riga Technical University\C\Python Practice")
# os.mkdir("testing")

GMAIL_ID = 'theskadd@gmail.com'
GMAIL_PSWD = 'madarchod'

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)

    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit

if __name__ == "__main__":
    sendEmail(GMAIL_ID, "subject", "Test message")
    exit()
    df = pd.read_excel(
     os.path.join("C:/Users/dhana/OneDrive - Riga Technical University/C/Python Practice/data.xlsx"),
     engine='openpyxl'
    )
    # df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    # print(type(today))
    yearNow = datetime.datetime.now().strftime("%Y")

    writeInd = []
    for index, item in df.iterrows():
        print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        print(bday)
        # msg = ""
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)
        
    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        # print(yr)
        df.loc[i, 'Year'] = f"{str(yr)} ,{str(yearNow)}"
        # print(df.loc[i, 'Year'])
    
    print(df)
    df.to_excel('data.xlsx', index = False)