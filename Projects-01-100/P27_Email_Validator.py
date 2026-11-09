import time
print("P27_Email_Validator.py")
email = input("enter your email:\n").lower().strip()
print(email)
invalid_patterns = (email.find("@@") != -1 or email.find("..") != -1 or email.find(".@") != -1 or email.find("@.") != -1)
length = len(email)
print(length)
has_at = "@" in email
has_dot = "." in email
print(has_at, has_dot)
at_count = email.count("@")
dot_count = email.count(".")
one_at = at_count == 1
dot_count_valid = dot_count >= 1
at_position = email.find("@")
dot_position = email.find(".")
print(at_position)
print(dot_position)
domain = email[at_position+1:]
dot_domain_count = domain.count(".")
dot_domain_valid = dot_domain_count == 1
print("Domains: ", domain,dot_domain_count,dot_domain_valid)
last_dot_position = email.rfind(".")
print(last_dot_position)
dot_after_at = dot_position > at_position
last_dot_after_at = last_dot_position > at_position
at_position_valid = at_position != 0 and at_position != -1 and at_position != len(email)-1
print(at_position_valid) 
last_dot_position_valid = last_dot_position != -1 and last_dot_position != 0 and (last_dot_position != len(email)-1)
print(last_dot_position_valid) 
position_valid = at_position_valid and last_dot_position_valid
print(position_valid)
final_valid = length >= 6 and (one_at and dot_count_valid) and position_valid and last_dot_after_at and not invalid_patterns and dot_domain_valid
if final_valid:
    print("Email is valid.")
else:
    print("Email is invalid")
