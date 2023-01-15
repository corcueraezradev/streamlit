# streamlit
The application will function as an automatic OTP generator consisting of 6-digit alphanumeric characters with the capability of sending the OTP to the recipient’s email address. 
Once the user has entered the OTP, the application will verify it and prompt a success or fail notification for the user.

Static password is used as the first line of defense from unauthorized access to a resource. Implementing a one-time password (OTP) adds additional layer of security. 
A one-time password is an automatically generated numeric or alphanumeric string of characters that authenticates a user for a single transaction or login session. An OTP is more secure than a static password, especially a user-created password, which can be weak and/or reused across multiple accounts. 
OTP Verification is the process of verifying a user by sending a unique password so that the user can be verified before completing a process. Distribution of OTP to the correct recipient is also a concern. And finally, the verification of OTP from the one that the user has entered.
The application utilizes the following:
•	Python’s “random” module to generate random number and letter for OTP
random.randint()
•	Python’s “smtp” module for sending emails using the Simple Mail Transfer Protocol (SMTP)
smtplib.SMTP(), startttls(), login(), sendmail()
•	Gmail account “app password” to allow login access of smtp
•	Streamlit python library to integrate graphical user-interface
session_state(), text_input(), button(), title(), markdown() 
System Analysis 
(Describe the purpose, what your software tool will do?)
The application will function as an automatic OTP generator consisting of 6-digit alphanumeric characters with the capability of sending the OTP to the recipient’s email address. 
Once the user has entered the OTP, the application will verify it and prompt a success or fail notification for the user.
Flowchart OTP application

