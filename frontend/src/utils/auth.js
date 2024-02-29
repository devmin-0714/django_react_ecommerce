import Cookies from 'js-cookie'
import apiInstance from './axios'


export const register = async (username, email, password, password2) => {
    const axios = apiInstance

    try {
        const { data } = await axios.post('account/register/', {
            username,
            email,
            password,
            password2,
        }) 
        return { data, error: null }

    } catch (error) {
        return {
            data : null,
            error: error.response.data || '다시 확인해 주세요',
        }
    }
}

export const login = async (username, password) => {
    const axios = apiInstance

    try {
        const { data, status } = await axios.post('account/token/', {
            username,
            password,
        })

        if (status === 200) {
            Cookies.set('access_token', data.access, {
                expires: 1,
                secure: true,
            })

            Cookies.set('refresh_token', data.refresh, {
                expires: 7,
                secure: true,
            })
        }

        return { data, error: null}
    } catch (error) {
        return {
            data: null,
            error: error.response.data?.detail || '로그인에 실패하였습니다',
        }
    }
}

export const logout = () => {
    Cookies.remove('access_token')
    Cookies.remove('refresh_token')
}