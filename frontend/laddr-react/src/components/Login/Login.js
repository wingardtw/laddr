import React, { Component } from 'react';

function LoginButton(props) {
    return (
      <button onClick={props.onClick}>
        Login
      </button>
    );
  }
  
  function LogoutButton(props) {
    return (
      <button onClick={props.onClick}>
        Logout
      </button>
    );
  }
  
  

class Login extends Component {

    constructor(props) {
        super(props);
        this.handleLoginClick = this.handleLoginClick.bind(this);
        this.handleLogoutClick = this.handleLogoutClick.bind(this);
        this.state = {isLoggedIn: false};
    }

    handleLoginClick() {
        this.setState({isLoggedIn: true});
    }

    handleLogoutClick() {
        this.setState({isLoggedIn: false});
    }

    render() {
        const isLoggedIn = this.state.isLoggedIn;
        let button, welcome;

        if (isLoggedIn) {
            button = <LogoutButton onClick={this.handleLogoutClick} />;
            welcome = "Welcome back!"
        } else {
            button = <LoginButton onClick={this.handleLoginClick} />;
            welcome = "Please log in."
        }
        

        return (
            <div className="container">
                <h1>
                    {welcome}
                </h1>
                {button}
            </div>
        )
    }
}

export default Login;