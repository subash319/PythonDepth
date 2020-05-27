# 3. Write a program that inputs an email id and extracts the user name and domain name from the email id.
# For example if email is myname@somesite.com then username is myname and domain name is somesite.com

email_id = input("Please enter the email address:")
name = email_id[:email_id.index('@')]
domain = email_id[email_id.index('@')+1:]
print(f'name extracted is {name} and domain extracted is {domain}')