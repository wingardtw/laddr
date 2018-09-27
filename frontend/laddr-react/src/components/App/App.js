import React, { Component } from 'react';
import './App.css';
import Main from '../Main/Main';


class App extends Component {
  state = {
    isLoggedIn:false
  }
  handleLogin = ()=> {
    this.setState(prevState => ({
      isLoggedIn: !prevState.isLoggedIn
    }))
  }

  render() {
    return (
      <Main />
    );
  }
}

export default App;
