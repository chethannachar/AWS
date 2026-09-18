import { Navigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export default function Dashboard() {
  const { user, loading, logout } = useAuth()
  if (loading) return <div className="loading-screen">Loading your account...</div>; if (!user) return <Navigate to="/login" replace />
  return <main className="dashboard"><header className="topbar"><div className="brand-mark">A<span>/</span>O</div><button className="text-button" onClick={logout}>Sign out <span aria-hidden="true">↗</span></button></header><section className="dashboard-content"><p className="eyebrow">Authenticated</p><section className="welcome-section" aria-labelledby="welcome-heading"><h1 id="welcome-heading">Welcome back, <em>{user.name}</em>!</h1></section><div className="account-detail"><span className="detail-label">Signed in as</span><div><strong>{user.email}</strong></div></div></section></main>
}