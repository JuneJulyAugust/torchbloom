import '@testing-library/jest-dom/vitest'

const storage: Record<string, string> = {}

Object.defineProperty(window, 'localStorage', {
  configurable: true,
  value: {
    clear: () => {
      for (const key of Object.keys(storage)) {
        delete storage[key]
      }
    },
    getItem: (key: string) => storage[key] ?? null,
    removeItem: (key: string) => {
      delete storage[key]
    },
    setItem: (key: string, value: string) => {
      storage[key] = value
    },
  },
})
