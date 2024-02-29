import React from 'react'
import { Link } from 'react-router-dom';


function StoreHeader() {
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container">
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" >
                                    계정
                                </a>
                            </li>
                        </ul>
                        <Link className="btn btn-primary me-2" to="/logout">Logout</Link>
                        <Link className="btn btn-primary me-2" to="/login">Login</Link>
                        <Link className="btn btn-primary me-2" to="/register">Register</Link>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default StoreHeader