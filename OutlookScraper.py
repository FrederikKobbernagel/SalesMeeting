email_string = []
email = open("/Users/frederikkobbernagel/Documents/EY/SalesMeeting/meet_test.txt", mode="r")

email_string = email.read()

email.close()
email_string = email_string.replace("\n", '')
words = email_string.split(' ')
for i in words:
    if 'Danske' in i:
        print(str(i) + ' is your index')
print(words)

# Insert function to loop through emails

