users = [
    ("jdoe", "ACTIVE", "no", "yes"),
    ("asmith", "ACTIVE", "yes", "no"),
    ("mchen", "SUSPENDED", "no", "yes"),
    ("svc_backup", "ACTIVE", "no", "no"),
    ("rpatel", "ACTIVE", "yes", "yes"),
    ("tnguyen", "DEPROVISIONED", "no", "no"),
    ("bwilson", "ACTIVE", "", "yes"),   # bad data on purpose — empty MFA field
    ("kgarcia", "ACTIVE", "no", "no"),
]

block_count = 0

for index, user in enumerate(users):
    username, status, mfa_raw, priv_raw = user

    #skip bad data instead of crashing

    if mfa_raw == "" or priv_raw == "":
        print(f"[{index}] SKIPPED - {username}: incomplete data!")
        continue

    mfa_enabled = mfa_raw.lower() == "yes"
    is_privileged = priv_raw.lower() == "yes"

    if status == "ACTIVE":
        if is_privileged and not mfa_enabled:
            decision = "BLOCK - Privileged account without MFA"
        elif not mfa_enabled:
            decision = "FLAG - remediation required"
        else:
            decision = "ALLOW"

    elif status == "SUSPENDED":
        decision = "BLOCK - account suspended"

    else:
        decision = "BLOCK - account deprovisioned or unknown status"

    if decision.startswith("BLOCK"):
        block_count += 1

    print(f"[{index}] {username} | {status} | {decision}")

print(f"\n Total Blocked users: {block_count}")