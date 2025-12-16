# 🏦 V.A.U.L.T. (Verified Architecture for User Liability & Trust)

> **The Compliance Firewall for FinTech & Healthcare AI.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## ⚠️ The Problem
In regulated industries (Banking, Insurance, MedTech), "Hallucination" equals "Lawsuit."
* **Liability:** An AI promising "guaranteed returns."
* **Bad Advice:** An AI telling a user to "evade taxes" or "stop taking medication."
* **Non-Compliance:** An AI failing to read mandatory disclaimers.

## 🛡️ The Solution
**V.A.U.L.T.** is a specialized governance layer for LLMs. It enforces **"Liability-First"** security, blocking any response that sounds like unauthorized advice or a binding promise.

### The Architecture
1.  **Layer 1: The Door (Prompt Kernel)**
    * Enforces strict "No Advice" personas.
    * Mandates separation of "Analysis" (Intent Check) and "Result" (Public Speech).
2.  **Layer 2: The Alloy (Sanitizer)**
    * Quarantines user input in triple-quotes to prevent prompt injection.
3.  **Layer 3: The Tumblers (Validator)**
    * Uses **Semantic Regex Filtering** to catch forbidden terms (`guarantee`, `promise`, `risk-free`).
    * Blocks messages *before* the user sees them if compliance fails.

---

## 🚀 Quick Start
```python
from vault.overseer import VaultOverseer

# 1. Load your Product Knowledge
CONTEXT = "Account APY: 4.5%. Fees: $10/mo."

# 2. Initialize V.A.U.L.T.
guard = VaultOverseer(CONTEXT)

# 3. Protect your Chatbot
user_query = "Promise me I'll make a million dollars!"
safe_prompt = guard.construct_prompt(user_query)

# ... LLM Generates Response ...
# ... V.A.U.L.T. Validates Response ...
