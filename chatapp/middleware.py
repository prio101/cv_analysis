from django.core.cache import cache
import time
# Token bucket settings
TOKEN_BUCKET_CAPACITY = 10  # Maximum 10 requests per minute
TOKEN_REFILL_RATE = 10 / 60  # 10 tokens per minute

def get_tokens(chat_session_id):
    """Fetch the current token count for a session, refill if necessary."""
    bucket_key = f"chat_tokens_{chat_session_id}"
    last_refill_key = f"last_refill_{chat_session_id}"

    tokens = cache.get(bucket_key, TOKEN_BUCKET_CAPACITY)
    last_refill = cache.get(last_refill_key, time.time())

    # Calculate the new token count based on time passed
    time_since_last = time.time() - last_refill
    new_tokens = min(TOKEN_BUCKET_CAPACITY, tokens + (time_since_last * TOKEN_REFILL_RATE))

    # Store updated values in cache
    cache.set(bucket_key, new_tokens, timeout=60)  # Expire in 60 seconds
    cache.set(last_refill_key, time.time(), timeout=60)

    return new_tokens

def use_token(chat_session_id):
    """Attempt to use a token, return True if allowed, False otherwise."""
    tokens = get_tokens(chat_session_id)
    if tokens >= 1:
        cache.set(f"chat_tokens_{chat_session_id}", tokens - 1, timeout=60)
        return True
    return False
