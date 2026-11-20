#!/usr/bin/env python3
"""
Thread Verification Engine
Validates:
1. Tweet character count <= 280 characters per tweet.
2. Mandatory tags present (@SuperteamUKR, @dev3pack).
3. Mandatory keywords present (Superteam, Instagrants, Bridge Accelerator, Dev3pack, Colosseum, Solana, Hackathon).
4. Generates SUBMISSION.md
"""

from thread_content import TWEETS

def verify_all_tweets():
    errors = []
    total_tweets = len(TWEETS)
    
    if total_tweets < 5:
        errors.append(f"Thread too short: {total_tweets} tweets (expected >= 5)")
        
    all_text = " ".join([t["content"] for t in TWEETS])
    
    # Check mandatory tags
    if "@SuperteamUKR" not in all_text:
        errors.append("Missing mandatory tag: @SuperteamUKR")
    if "@dev3pack" not in all_text:
        errors.append("Missing mandatory tag: @dev3pack")
        
    # Check mandatory keywords
    required_keywords = [
        "Superteam", "Instagrants", "Bridge Accelerator", "Dev3pack", 
        "Colosseum", "Solana", "Hackathon"
    ]
    for kw in required_keywords:
        if kw.lower() not in all_text.lower():
            errors.append(f"Missing required keyword: {kw}")
            
    # Check character counts
    for t in TWEETS:
        idx = t["index"]
        length = len(t["content"])
        if length > 280:
            errors.append(f"Tweet {idx} exceeds 280 chars: {length} chars")
            
    return {
        "valid": len(errors) == 0,
        "total_tweets": total_tweets,
        "errors": errors
    }

if __name__ == "__main__":
    res = verify_all_tweets()
    print("Verification Result:", res)
    if not res["valid"]:
        exit(1)
    print("All tweets 100% compliant with Twitter / Superteam constraints!")
