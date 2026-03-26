"""AI Integration Guide - Open Source APIs

This guide explains how to integrate open source AI services for SupportHub.
"""

# ==========================================
# OPTION 1: Hugging Face Inference API (RECOMMENDED)
# ==========================================
"""
Advantages:
✓ Free tier with good rate limits (500 calls/day)
✓ No GPU setup needed
✓ Pre-trained models available
✓ Production-ready API
✓ Easy to upgrade for scale

Setup:
1. Sign up: https://huggingface.co/settings/tokens
2. Get API key
3. Set in .env: HUGGINGFACE_API_KEY=your_key
4. Models available:
   - facebook/bart-large-mnli (Zero-shot classification)
   - sentence-transformers/all-MiniLM-L6-v2 (Semantic similarity)
   - distilbert-base-uncased (Text understanding)

Free Tier Limits:
- 500 API calls/day
- No credit card required
- Upgrade when needed

Cost (paid tier):
- $0.000006 per inference
- 1M inferences = ~$6
"""

# ==========================================
# OPTION 2: Ollama (Local, Fully Open Source)
# ==========================================
"""
Advantages:
✓ Completely free
✓ Runs locally (no cloud dependency)
✓ Full data privacy
✓ No API keys needed
✓ Works offline

Setup:
1. Install Ollama: https://ollama.ai
2. Download model: ollama pull llama2
3. Start: ollama serve
4. Update in ai/nlp_classifier.py:
   - Change API endpoint to localhost:11434
   - Use Ollama API format

Available Models:
- llama2 (Recommended)
- mistral
- neural-chat
- dolphin-mixtral

Note: First run requires model download (~5-10GB)
Performance: May be slower than cloud APIs on first request

Example integration:
```python
import requests

def classify_with_ollama(text: str):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama2',
            'prompt': f'Classify this harassment report: {text}',
            'stream': False
        }
    )
    return response.json()['response']
```
"""

# ==========================================
# OPTION 3: Together AI (Free Open Models)
# ==========================================
"""
Advantages:
✓ Free tier for open models
✓ No credit card (initially)
✓ Large model selection
✓ Good for development

Setup:
1. Sign up: https://www.together.ai/
2. Get API key
3. Set in .env: TOGETHER_API_KEY=your_key

Available Models:
- togethercomputer/llama-2-70b-chat
- togethercomputer/mistral-7b-instruct

Free Tier: Limited tokens, upgrade for production
"""

# ==========================================
# OPTION 4: OpenAI API (Premium but Best Quality)
# ==========================================
"""
Advantages:
✓ Highest quality models (GPT-4)
✓ Best understanding of context
✓ Pay-as-you-go pricing
✓ Minimal API key management

Setup:
1. Sign up: https://platform.openai.com
2. Add payment method (required)
3. Get API key
4. Set in .env: OPENAI_API_KEY=your_key

Pricing:
- GPT-4: $0.03/1K tokens (input)
- GPT-3.5: $0.0005/1K tokens
- For demo: <$1 per day

Recommended for demo after funding secured
"""

# ==========================================
# IMPLEMENTATION GUIDE
# ==========================================

"""
Current Implementation (Hybrid Approach):

1. Primary: Hugging Face API
   - Uses facebook/bart-large-mnli for zero-shot classification
   - Uses sentence-transformers for similarity matching
   - Fallback to mock data if API unavailable

2. Mock Data Fallback
   - Always works without API key
   - Keyword-based classification for demo
   - Realistic simulated results

3. Easy API Switching
   - All AI services in ai/ directory
   - Each has try/except with fallback
   - Can swap APIs without changing UI code

To switch APIs:

Step 1: Update ai/nlp_classifier.py
```python
def classify(self, text: str) -> Dict[str, float]:
    # Change API endpoint here
    response = requests.post(
        "YOUR_NEW_API_ENDPOINT",
        headers=self.headers,
        json=payload
    )
```

Step 2: Update .env
```
# Add new API key
NEW_API_KEY=your_key
```

Step 3: Test
```bash
python -c "from ai import NLPClassifier; c = NLPClassifier(); print(c.classify('test text'))"
```
"""

# ==========================================
# COMPARISON TABLE
# ==========================================

"""
┌─────────────────┬────────────┬──────────┬────────────┬─────────────┐
│ Service         │ Free Tier  │ Quality  │ Privacy    │ Speed       │
├─────────────────┼────────────┼──────────┼────────────┼─────────────┤
│ Hugging Face    │ 500/day    │ Good     │ Cloud      │ Fast        │
│ Ollama          │ Unlimited  │ Good     │ Local      │ Slow        │
│ Together AI     │ Limited    │ Good     │ Cloud      │ Fast        │
│ OpenAI (GPT-4)  │ Paid only  │ Excellent│ Cloud      │ Very Fast   │
│ LLaMA 2 API     │ Free       │ Good     │ Depends    │ Medium      │
└─────────────────┴────────────┴──────────┴────────────┴─────────────┘

Recommendation for Demo: Hugging Face (free, reliable, easy)
Recommendation for Production: OpenAI (best quality) or Ollama (privacy)
"""

# ==========================================
# COST ESTIMATION
# ==========================================

"""
For 100 reports/day:

Hugging Face (Paid after free tier):
- 100 classifications: 100 × $0.000006 = $0.0006/day
- Annual: ~$0.22

Together AI:
- Similar to Hugging Face: ~$0.20/year

OpenAI GPT-3.5:
- 100 classifications: ~$0.03/day
- Annual: ~$11

OpenAI GPT-4:
- 100 classifications: ~$0.06/day
- Annual: ~$22

Ollama (Local):
- $0 (just electricity)
- One-time download of model (~5-10GB)
"""

# ==========================================
# QUICK SETUP CHECKLIST
# ==========================================

"""
For Sponsor Demo:
□ Use Hugging Face (free tier)
□ OR use Ollama locally (no API key)
□ Mock data enabled by default
□ Switch between modes in .env
□ Test all UI flows
□ Screenshot key features

For Production Preparation:
□ Choose primary AI service
□ Set up paid account if needed
□ Configure API keys
□ Implement rate limiting
□ Add monitoring/alerting
□ Load test with expected volume
□ Plan for scale-out strategy
"""

# ==========================================
# MONITORING & OPTIMIZATION
# ==========================================

"""
Add to utils/monitoring.py:

import time
from functools import wraps

def monitor_ai_api(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start
            
            # Log success
            print(f"{func.__name__} completed in {duration:.2f}s")
            return result
            
        except Exception as e:
            # Log error and use fallback
            print(f"{func.__name__} failed: {e}")
            return None
    return wrapper

Usage:
@monitor_ai_api
def classify(self, text):
    ...
"""

# ==========================================
# TROUBLESHOOTING
# ==========================================

"""
Problem: API rate limit reached
Solution: 
  - Use Ollama for unlimited local processing
  - Or upgrade Hugging Face tier
  - Implement request queuing

Problem: API responses too slow
Solution:
  - Enable caching for repeated texts
  - Use async requests
  - Consider batch processing

Problem: API down/unavailable
Solution:
  - All services have mock data fallback
  - Current implementation handles gracefully
  - Dashboard still shows previous results

Problem: Privacy concerns with cloud APIs
Solution:
  - Use Ollama (runs locally, 100% private)
  - Or use self-hosted version of HF models
  - See deployment/self-hosted.md
"""

print(__doc__)
