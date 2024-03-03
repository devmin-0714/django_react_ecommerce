import { useAuthStore } from '../../store/auth'

const Home = () => {
  const [isLoggedIn, user] = useAuthStore((state) => [
    state.isLoggedIn,
    state.user,
  ])

  return (
    <div>
      {isLoggedIn() ? <LoggedInView user={user()} /> : <LoggedOutView />}
    </div>
  )
}

const LoggedInView = ({ user }) => {
  return (
    <div>
      로그인 : 
      {user.user_id}
      {user.username}
    </div>
  )
}

export const LoggedOutView = () => {
  return (
    <div>
      로그아웃
    </div>
  )
}

export default Home