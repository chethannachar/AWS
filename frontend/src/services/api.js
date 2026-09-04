const API_URL = (import.meta.env.VITE_API_URL || 'http://localhost:5000').replace(/\/$/, '')

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, { credentials: 'include', headers: { 'Content-Type': 'application/json', ...options.headers }, ...options })
  const data = await response.json().catch(() => ({}))
  if (!response.ok) throw new Error(data.detail || 'Something went wrong. Please try again.')
  return data
}

export const api = { register: (payload) => request('/api/auth/register', { method: 'POST', body: JSON.stringify(payload) }), login: (payload) => request('/api/auth/login', { method: 'POST', body: JSON.stringify(payload) }), me: () => request('/api/auth/me'), logout: () => request('/api/auth/logout', { method: 'POST' }) }