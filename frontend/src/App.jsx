import { useState, useEffect } from 'react'
import axios from 'axios';


function App() {
    const username = 'min1'
    const email = 'min1@min.com'
    const password = 'min123456'
    const password2 = 'min123456'

    useEffect(() => {
        axios.post('http://127.0.0.1:8000/api/account/register/', {
                username,
                email,
                password,
                password2,
            });
    }, [])

    return (
        <>
            <div>test</div>
        </>
    )
}

export default App