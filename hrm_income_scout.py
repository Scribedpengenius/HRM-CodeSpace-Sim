import random

# Simple list of income opportunities
opportunities = [
    {"name": "Affiliate Marketing", "risk": 0.3, "reward": 0.7},
    {"name": "Amazon KDP Publishing", "risk": 0.4, "reward": 0.8},
    {"name": "Crypto Staking", "risk": 0.6, "reward": 0.9},
    {"name": "Online Course Licensing", "risk": 0.2, "reward": 0.6},
    {"name": "Music Royalties", "risk": 0.5, "reward": 0.75},
]

# Simple scoring function (later we can make this E8-inspired)
def score(opp):
    return opp["reward"] - opp["risk"] * 0.5

# Shuffle and rank
random.shuffle(opportunities)
ranked = sorted(opportunities, key=score, reverse=True)

print("💡 Top Income Opportunities (Prototype Scout):")
for opp in ranked:
    print(f"- {opp['name']} | Score: {score(opp):.2f}")
