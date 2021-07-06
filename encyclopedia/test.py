#First use
user_email = "abc@yahoo.com"

email_services = ["hotmail", "gmail", "yahoo"]
email_contains_service = any(email_service in user_email for email_service in email_services)

print(email_contains_service)


#Second use
list_item = ["food", "swimming", "coffee", 'toffuu', 'taff']
query = "ff"

#pay attention
#111 --- confirming ---
s = any(query in item for item in list_item)
print(s)

new_filtered_query = []
#222 --- indexing ---
for item in list_item :
	if query in item :
		new_filtered_query.append(item)

print(new_filtered_query)

	

