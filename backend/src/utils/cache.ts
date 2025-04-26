type CacheEntry<T> = {
  value: T;
  expires: number;
};

class SimpleCache<T = any> {
  private store = new Map<string, CacheEntry<T>>();

  constructor(private ttlMs: number = 3600 * 1000) {
    this.startCleanup();
  }

  get(key: string): T | undefined {
    const cached = this.store.get(key);
    if (!cached) return undefined;
    if (Date.now() > cached.expires) {
      this.store.delete(key);
      return undefined;
    }
    return cached.value;
  }

  set(key: string, value: T, ttlMs: number = this.ttlMs) {
    this.store.set(key, { value, expires: Date.now() + ttlMs });
  }

  clear() {
    this.store.clear();
  }

  private startCleanup(interval: number = 300000 /* 5 minutes */) {
    setInterval(() => this.cleanupExpired(), interval);
  }

  private cleanupExpired() {
    const now = Date.now();
    for (const [key, entry] of this.store.entries()) {
      if (now > entry.expires) {
        this.store.delete(key);
      }
    }
  }
}

export const cache = new SimpleCache();
