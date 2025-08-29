users = {
 "user1": {"email": "daniel@email.com", "status": "canceled"},
 "user2": {"email": "jenny@email.com", "status": "active" },
 "user3": {"email": "kiki@email.com", "status": "canceled" },
 "user4": {"email": "kim-juhno@email.com", "status": "active" },
 "user5": {"email": "lee-kang@email.com", "status": "active" },
}

# Check for canceled statuses here
for user,info in tuple(users.items()):
        if info["status"] =='canceled':
           del users[user]
           print("Subscription for user", user, "is deleted")

print(users)
