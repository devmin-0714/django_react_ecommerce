import { useState } from 'react';
import { login } from '../../utils/auth';
import { Link } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();

        const { error } = await login(username, password);

        if (error) {
            alert(error);
        }

    };

    return (
        <section>
            <main className="" style={{ marginBottom: 100, marginTop: 50 }}>
                <div className="container">
                    {/* Section: Login form */}
                    <section className="">
                        <div className="row d-flex justify-content-center">
                            <div className="col-xl-5 col-md-8">
                                <div className="card rounded-5">
                                    <div className="card-body p-4">
                                        <h3 className="text-center">로그인</h3>
                                        <br />

                                        <div className="tab-content">
                                            <div
                                                className="tab-pane fade show active"
                                                id="pills-login"
                                                role="tabpanel"
                                                aria-labelledby="tab-login"
                                            >
                                                <form onSubmit={handleLogin}>
                                                    <div className="form-outline mb-4">
                                                        <label className="form-label" htmlFor="Full Name">
                                                            사용자 ID
                                                        </label>
                                                        <input
                                                            type="text"
                                                            id="username"
                                                            name="username"
                                                            value={username}
                                                            onChange={(e) => setUsername(e.target.value)}
                                                            className="form-control"

                                                        />
                                                    </div>

                                                    <div className="form-outline mb-4">
                                                        <label className="form-label" htmlFor="loginPassword">
                                                            비밀번호
                                                        </label>
                                                        <input
                                                            type="password"
                                                            id="password"
                                                            name="password"
                                                            value={password}
                                                            onChange={(e) => setPassword(e.target.value)}
                                                            className="form-control"
                                                        />
                                                    </div>

                                                    <button className='btn btn-primary w-100' type="submit">
                                                            <span className="mr-2">로그인</span>
                                                            <i className="fas fa-sign-in-alt" />
                                                    </button>

                                                    <div className="text-center">
                                                        <p className='mt-4'>
                                                            회원가입 계정이 없으신가요? <Link to="/register">회원가입</Link>
                                                        </p>
                                                    </div>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </main>
        </section>
    );
};

export default Login;