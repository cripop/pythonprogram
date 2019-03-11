#sending mail using python

import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='kashyappriyankindias@gmail.com'
	receiver='kingcofcrew@gmail.com'
	msg="hii"
	s.login(sender,'password')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent sucessfully")
	s.quit()