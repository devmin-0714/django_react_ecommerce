import { Route, Routes, BrowserRouter } from 'react-router-dom'
import apiInstance from './utils/axios'
import StoreHeader from './views/base/StoreHeader'
import StoreFooter from './views/base/StoreFooter'
import Home from './views/shop/Home'
import Register from './views/auth/Register'
import Login from './views/auth/Login'
import Logout from './views/auth/Logout'

function App() {
    const axios = apiInstance

    return (
        <BrowserRouter>
            <StoreHeader />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path='/register' element={<Register />} />
                <Route path='/login' element={<Login />} />
                <Route path='/logout' element={<Logout />} />
            </Routes>
            <StoreFooter />
        </BrowserRouter>
    )
}

export default App