import React from 'react';

const Login = props => {
    return (
        <div>
            <h2>Please Login</h2>
            <button onClick={props.loginHandler} className="btn btn-success btn-sm">Login</button>
        </div>
    );
}

export default Login;
