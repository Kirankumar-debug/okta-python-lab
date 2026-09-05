users = [
    ("jdoe", "ACTIVE", "no", "yes"),
    ("asmith", "ACTIVE", "yes", "no"),
    ("mchen", "SUSPENDED", "no", "yes"),
    ("svc_backup", "ACTIVE", "no", "no"),
    ("rpatel", "ACTIVE", "yes", "yes"),
    ("tnguyen", "DEPROVISIONED", "no", "no"),
    ("bwilson", "ACTIVE", "", "yes"),
    ("kgarcia", "ACTIVE", "no", "no"),
    ("svc_reports", "SUSPENDED", "no", "no"),
]

active_users = [u for u in users if u[1] == "ACTIVE"]
print(active_users)

sorted_active = sorted(active_users, key=lambda u: u[0])
print(sorted_active)

active_usernames = [u[0] for u in sorted_active]
print(active_usernames)

active_svcUsers = [u[0] for u in users if u[0].startswith("svc")]
print(active_svcUsers)