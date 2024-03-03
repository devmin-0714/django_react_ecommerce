import { useAuthStore } from '../store/auth'
import axios from './axios'
import jwt_decode from 'jwt-decode'
import Cookies from 'js-cookie'
import Swal from 'sweetalert2';

const Toast = Swal.mixin({
    toast: true,
    position: 'top',
    showConfirmButton: false,
    timer: 1500,
    timerProgressBar: true,
});

export const register = async (username, email, password, password2) => {
    try {
        const { data } = await axios.post('account/register/', {
            username,
            email,
            password,
            password2,
        })

        await login(username, password)

        Toast.fire({
            icon: 'success',
            title: '회원가입에 성공하였습니다'
        });

        return { data, error: null }

    } catch (error) {
        return {
            data : null,
            error: error.response.data || '회원가입에 실패하였습니다',
        }
    }
}

export const login = async (username, password) => {
    try {
        const { data, status } = await axios.post('account/token/', {
            username,
            password,
        })

        if (status === 200) {
            setAuthUser(data.access, data.refresh)

            Toast.fire({
                icon: 'success',
                title: '로그인에 성공하였습니다'
            });
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
    useAuthStore.getState().setUser(null)

    Toast.fire({
        icon: 'success',
        title: '로그아웃 되었습니다'
    });
}

export const setAuthUser = (access_token, refresh_token) => {
    Cookies.set('access_token', access_token, {
        expires: 1,
        secure: true,
    })

    Cookies.set('refresh_token', refresh_token, {
        expires: 7,
        secure: true,
    })

    const user = jwt_decode(access_token) ?? null

    if (user) {
        useAuthStore.getState().setUser(user)
    }
    useAuthStore.getState().setLoading(false)
}

export const getRefreshToken = async () => {
    const refresh_token = Cookies.get('refresh_token')
    const response = await axios.post('account/token/refresh', {
        refresh: refresh_token,
    })

    return response.data
}

export const isAccessTokenExpired = (access_token) => {
    try {
        const decodedToken = jwt_decode(access_token)
        return decodedToken.expires < Date.now() / 1000

    } catch (error) {
        return true
    }
}

export const setUser = async () => {
    const access_token = Cookies.get('access_token')
    const refresh_token = Cookies.get('refresh_token')

    if (!access_token || !refresh_token) {
        return
    }

    if (isAccessTokenExpired(access_token)) {
        const response = await getRefreshToken(refresh_token)
        setAuthUser(response.access, response.refresh)
    } else {
        setAuthUser(access_token, refresh_token)
    }
}