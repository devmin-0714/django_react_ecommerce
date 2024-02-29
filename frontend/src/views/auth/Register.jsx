import { useState } from 'react';
import { register } from '../../utils/auth';
import { Link, useNavigate } from 'react-router-dom';

function Register() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    const resetForm = () => {
        setUsername('');
        setEmail('');
        setPassword('');
        setPassword2('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const { error } = await register(username, email, password, password2);
        if (error) {
            alert(JSON.stringify(error));
        } else {
            navigate('/');
            resetForm();
        }
    };

    return (
        <>
            <main className="" style={{ marginBottom: 100, marginTop: 50 }}>
                <div className="container">
                    <section className="">
                        <div className="row d-flex justify-content-center">
                            <div className="col-xl-5 col-md-8">
                                <div className="card rounded-5">
                                    <div className="card-body p-4">
                                        <h3 className="text-center">회원가입</h3>
                                        <br />

                                        <div className="tab-content">
                                            <div
                                                className="tab-pane fade show active"
                                                id="pills-login"
                                                role="tabpanel"
                                                aria-labelledby="tab-login"
                                            >
                                                <form onSubmit={handleSubmit}>
                                                    <div className="form-outline mb-4">
                                                        <label className="form-label" htmlFor="UserName">
                                                            사용자ID
                                                        </label>
                                                        <input
                                                            type="text"
                                                            id="username"
                                                            onChange={(e) => setUsername(e.target.value)}
                                                            placeholder="UserName"
                                                            required
                                                            className="form-control"

                                                        />
                                                    </div>
                                                    <div className="form-outline mb-4">
                                                        <label className="form-label" htmlFor="loginName">
                                                            이메일
                                                        </label>
                                                        <input
                                                            type="email"
                                                            id="email"
                                                            onChange={(e) => setEmail(e.target.value)}
                                                            placeholder="abc@gmail.com"
                                                            required
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
                                                            onChange={(e) => setPassword(e.target.value)}
                                                            placeholder="Password"
                                                            className="form-control"
                                                        />
                                                    </div>
                                                    <div className="form-outline mb-4">
                                                        <label className="form-label" htmlFor="loginPassword">
                                                            비밀번호 재확인
                                                        </label>
                                                        <input
                                                            type="password"
                                                            id="confirm-password"
                                                            onChange={(e) => setPassword2(e.target.value)}
                                                            placeholder="Confirm Password"
                                                            required
                                                            className="form-control"
                                                        />
                                                    </div>
                                                    <p className='fw-bold text-danger'>
                                                        {password2 !== password ? 'Passwords do not match' : ''}
                                                    </p>

                                                    <button className='btn btn-primary w-100' type="submit">
                                                        <>
                                                            <span className="mr-2">회원가입</span>
                                                            <i className="fas fa-user-plus" />
                                                        </>
                                                    </button>

                                                    <div className="text-center">
                                                        <p className='mt-4'>
                                                            이미 계정이 가지고 계십니까? <Link to="/login">로그인</Link>
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
        </>


    );
}

export default Register;
