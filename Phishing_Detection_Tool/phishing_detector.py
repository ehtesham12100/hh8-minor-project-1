from urllib.parse import urlparse
from datetime import datetime
import whois
import requests

# ---------------- GOOGLE SAFE BROWSING ----------------
API_KEY = "YOUR_API_KEY_HERE"   # KEEP THIS SECRET

def check_google_safe_browsing(url):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    payload = {
        "client": {
            "clientId": "phishing-detection-project",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    try:
        response = requests.post(
            endpoint,
            params={"key": API_KEY},
            json=payload,
            timeout=5
        )
        return response.json()
    except:
        return {}

# ---------------- RULE-BASED LOGIC ----------------
def extract_domain(url):
    return urlparse(url).netloc.lower()

def has_suspicious_words(domain):
    suspicious_words = ["login", "secure", "verify", "update", "account"]
    return any(word in domain for word in suspicious_words)

def has_lookalike_chars(domain):
    lookalike_chars = ['0', '1']
    return any(ch in domain for ch in lookalike_chars)

def get_domain_age(domain):
    try:
        info = whois.whois(domain)
        created = info.creation_date
        if isinstance(created, list):
            created = created[0]
        return (datetime.now() - created).days
    except:
        return None

def rule_based_detection(url):
    score = 0
    domain = extract_domain(url)
    print("Domain:", domain)

    if "-" in domain:
        score += 1

    if has_suspicious_words(domain):
        score += 1

    if has_lookalike_chars(domain):
        score += 1

    age = get_domain_age(domain)

    if age is None:
        print("WHOIS data unavailable (ignored)")
    else:
        print("Domain age (days):", age)
        if age < 180:
            score += 2

    return score   # ✅ FIXED

# ---------------- MAIN PROGRAM ----------------
url = input("Enter the URL: ").strip()

rule_score = rule_based_detection(url)
google_result = check_google_safe_browsing(url)

if "matches" in google_result:
    print("⚠ Google Safe Browsing: Threat detected")
    print("⚠ PHISHING URL")
else:
    if rule_score >= 3:
        print("⚠ PHISHING URL")
    else:
        print("✅ SAFE URL")
