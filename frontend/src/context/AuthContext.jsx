import { createContext, useContext, useEffect, useState } from 'react'
import { api } from '../services/api'

const AuthContext = createContext(null)
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null); const [loading, setLoading] = useState(true)
  useEffect(() => { api.me().then(setUser).catch(() => setUser(null)).finally(() => setLoading(false)) }, [])
  const login = async (credentials) => { const loggedInUser = await api.login(credentials); setUser(loggedInUser); return loggedInUser }
  const logout = async () => { await api.logout().catch(() => {}); setUser(null) }
  return <AuthContext.Provider value={{ user, loading, login, logout }}>{children}</AuthContext.Provider>
}
export function useAuth() { return useContext(AuthContext) }