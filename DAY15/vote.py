#To build voting system
candidates = {
    "A": "Alice",
    "B": "Bob",
    "C": "Charlie"
}
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}
voted_users = set()   
n = int(input("Enter number of voters: "))
for i in range(n):
    voter_id = input("\nEnter voter ID: ")
    if voter_id in voted_users:
        print("You have already voted!")
        continue
    print("Candidates:")
    for key, value in candidates.items():
        print(key, "→", value)
    choice = input("Enter your vote (A/B/C): ").upper()
    if choice in candidates:
        candidate_name = candidates[choice]
        votes[candidate_name] += 1
        voted_users.add(voter_id)
        print("Vote recorded successfully!")
    else:
        print("Invalid vote!")
print("\n--- Vote Count ---")
for candidate, count in votes.items():
    print(candidate, ":", count)
winner = max(votes, key=votes.get)
print("\nWinner is:", winner)
