# Get the value of environment variables from the user

email_from_value = input('Enter the email address of the sendter: ')
email_to_value = input('Enter recipient email address: ')
email_login_from_value = input('Enter login from sender email address: ')
email_pass_from_value = input('Enter password from sender email address: ')

file = open('.env', 'w', encoding='utf-8')
file.write("EMAIL_FROM={}\n".format(email_from_value))
file.write("EMAIL_FROM_LOGIN={}\n".format(email_login_from_value))
file.write("EMAIL_FROM_PASS={}\n".format(email_pass_from_value))
file.write("EMAIL_TO={}\n".format(email_to_value))
file.close()
# Set environment variables
#os.environ['EMAIL_FROM'] = email_from_value
#os.environ['EMAIL_TO'] = email_to_value
#os.environ['EMAIL_FROM_LOGIN'] = email_login_from_value
#os.environ['EMAIL_FROM_PASS'] = email_pass_from_value

print('Setup script completed successfully')
#print(os.getenv('EMAIL_FROM'))
#print(os.getenv('EMAIL_TO'))
#print(os.getenv('EMAIL_FROM_LOGIN'))
#print(os.getenv('EMAIL_FROM_PASS'))
