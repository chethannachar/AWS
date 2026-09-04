import { useState } from 'react'
import { Link, Navigate, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { api } from '../services/api'
import { AuthLayout } from './Login'

export default function Register() {
  const { user } = useAuth(); const navigate = useNavigate(); const [form, setForm] = useState({ name: '', email: '', password: '' }); const [message, setMessage] = useState(''); const [error, setError] = useState(''); const [submitting, setSubmitting] = useState(false)
  if (user) return <Navigate to="/dashboard" replace />
  const submit = async (event) => { event.preventDefault(); setError(''); setMessage(''); setSubmitting(true); try { await api.register(form); setMessage('Account created. Redirecting to sign in...'); setTimeout(() => navigate('/login'), 900) } catch (err) { setError(err.message) } finally { setSubmitting(false) } }
  return <AuthLayout eyebrow="Start fresh" title="Create your account" footer={<>Already a member? <Link to="/login">Sign in</Link></>}><form onSubmit={submit} className="auth-form"><label>Full name<input type="text" required maxLength="100" autoComplete="name" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} /></label><label>Email address<input type="email" required autoComplete="email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} /></label><label>Password<input type="password" required minLength="8" autoComplete="new-password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} /></label>{message && <p className="form-message success" role="status">{message}</p>}{error && <p className="form-message error" role="alert">{error}</p>}<button className="primary-button" disabled={submitting}>{submitting ? 'Creating account...' : 'Create account'} <span aria-hidden="true">→</span></button></form></AuthLayout>
}