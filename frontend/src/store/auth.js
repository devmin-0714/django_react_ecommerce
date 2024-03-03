import { create } from 'zustand'

import { mountStoreDevtool } from 'simple-zustand-devtools'

const useAuthStore = create((set, get) => ({
    // user
    allUserData: null,
    user: () => ({
        user_id: get().allUserData?.user_id || null,
        username: get().allUserData?.username || null,
    }),
    setUser: (user) => set({ allUserData: user }),
    
    // loading
    loading: false,
    setLoading: (loading) => set({ loading }),
    isLoggedIn: () => get().allUserData !== null,
}))

if (import.meta.env.DEV) {
    mountStoreDevtool('Store', useAuthStore)
}

export { useAuthStore }