type CacheEntry<T> = {
  value: T;
  expires: number;
};

class SimpleCache<T = any> {
  private store = new Map<string, CacheEntry<T>>();

  constructor(private ttlMs: number = 3600 * 1000) {}

  get(key: string): T | undefined {
    const cached = this.store.get(key);
    if (!cached) return undefined;
    if (Date.now() > cached.expires) {
      this.store.delete(key);
      return undefined;
    }
    return cached.value;
  }

  set(key: string, value: T) {
    this.store.set(key, { value, expires: Date.now() + this.ttlMs });
  }

  clear() {
    this.store.clear();
  }
}

export const cache = new SimpleCache();
