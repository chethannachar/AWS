import { useEffect, useState } from 'react'
import { Navigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { api } from '../services/api'

export default function Dashboard() {
  const { user, loading, logout } = useAuth(); const [cicdStatus, setCicdStatus] = useState('Checking CI/CD deployment...'); const [cicdMessage, setCicdMessage] = useState('')
  useEffect(() => { if (user) api.cicdTest().then(({ message }) => { setCicdMessage(message); setCicdStatus('CI/CD endpoint reached successfully.') }).catch(() => { setCicdMessage(''); setCicdStatus('CI/CD endpoint could not be reached.') }) }, [user])
  if (loading) return <div className="loading-screen">Loading your account...</div>; if (!user) return <Navigate to="/login" replace />
  return <main className="dashboard"><header className="topbar"><div className="brand-mark">A<span>/</span>O</div><button className="text-button" onClick={logout}>Sign out <span aria-hidden="true">↗</span></button></header><section className="dashboard-content"><p className="eyebrow">Your private space</p><h1>Good to see you,<br /><em>{user.name}</em>.</h1><div className="account-detail"><span className="detail-label">Account details</span><div><strong>{user.email}</strong><span>Member since {new Date(user.created_at).toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' })}</span></div></div><div className="account-detail"><span className="detail-label">Deployment status</span><div><strong>{cicdStatus}</strong>{cicdMessage && <span>{cicdMessage}</span>}</div></div></section></main>
}