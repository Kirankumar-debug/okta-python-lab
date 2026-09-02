username = input("Enter username: ")
status = input("Enter status (ACTIVE/INACTIVE/SUSPENDED): ")
mfa_enabled = input("Is MFA enabled? (yes/no): ")
is_privileged = input("Is this a privileged account? (yes/no): ")

mfa_enabled = mfa_enabled.lower() == "yes"
is_privileged = is_privileged.lower() == "yes"


print(is_privileged, type(is_privileged))

if status == "ACTIVE":
    if is_privileged and not mfa_enabled:
        decision = "BLOCK - privileged account without MFA"
    elif not mfa_enabled:
        decision = "FLAG - remidiation required"
    else:
        decision = "ALLOW"
elif status == "SUSPENDED":
    decision = "BLOCK- Account Suspended"
else:
    decision = "BLOCK - account deprovisioned or unknown status"

print(f"User: {username} | Status: {status} | Decision: {decision}")