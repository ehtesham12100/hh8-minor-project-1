# hh8-minor-project-1
Python-based phishing detection tool using WHOIS and Google Safe Browsing API.
# Phishing Detection Tool

## Project Description
This project is a Python-based phishing detection tool developed as part of Minor Project 1.
The tool analyzes URLs to identify phishing websites by checking suspicious patterns,
domain age using WHOIS API, and real-time verification using Google Safe Browsing API.

The goal of this project is to help users detect malicious links before visiting them.

---

## Features
- URL structure analysis
- Detection of suspicious keywords and typosquatting patterns
- Look-alike character detection (e.g., paypa1 instead of paypal)
- Domain age verification using WHOIS API
- Real-time phishing detection using Google Safe Browsing API

---

## Tools & Technologies Used
- Python
- python-whois (WHOIS API)
- Google Safe Browsing API
- Requests library
- GitHub for version control

---
## Security Note
Used my own Google Safe Browsing API key for real-time phishing detection.  
For security reasons, the API key is not committed to the repository.
use own API
## How to Run the Project

1. Install Required Libraries
```bash
pip install python-whois requests
2. Run the Program
python phishing_detector.py
3.enter url

##Output Example
SAFE URL → The website is considered safe
PHISHING URL → The website is detected as phishing
