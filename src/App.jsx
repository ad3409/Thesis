import react from 'react'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import NotFound from './pages/NotFound'
import Home from './pages/Home'
import Survey from './pages/Survey'
import ProtectedRoute from './components/ProtectedRoute'
import Evaluation from './pages/Evaluation'
import AIChat from './components/AIChat'

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route 
          path='/'
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path='/survey/:surveyId' element={<ProtectedRoute><Survey /></ProtectedRoute>} />
        <Route path='/evaluation/:evaluationId' element={<ProtectedRoute><Evaluation /></ProtectedRoute>} />
        <Route path='/login' element={<Login />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/register' element={<RegisterAndLogout />} />
        <Route path='/AIChat' element={<AIChat />} />
        <Route path='*' element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
