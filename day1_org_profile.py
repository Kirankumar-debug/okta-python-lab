org_name = input("Please enter your Otka org name: ")
admin_email = input("Enter the admin email address: ")

mfa_enforced = False

print(f"Org Name: '{org_name}' is administered by {admin_email}. MFA enforcement: {mfa_enforced}")

print(type(mfa_enforced))