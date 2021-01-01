import React, { Component } from 'react';
import Profile from './profile';
import Login from './login';

class Auth extends Component {

    constructor(props) {
        super(props)
        this.state = {
            IsLogin: false,
            name: "Bozlur Rosid Sagor",
            profession: "Full-stack software engineer"
        }

    }

    loginHandler = () => {
        this.setState({
            IsLogin: true
        })
    }

    logoutHandlar = () => {
        this.setState({IsLogin:false})
    }

    render() {
        return (
            <div className="mt-2">
                {this.state.IsLogin === true ? <Profile name={this.state.name} profession={this.state.profession} logoutHandlar={this.logoutHandlar} /> : <Login loginHandler={this.loginHandler} />}
            </div>
        )
    }
}

export default Auth;
