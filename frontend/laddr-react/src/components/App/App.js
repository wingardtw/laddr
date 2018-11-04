import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Landing from '../Landing/Landing';
import Home from '../Pages/Home/Home';
import FindPlayers from '../Pages/FindPlayers/FindPlayers';
import PendingMatches from '../Pages/PendingMatches/PendingMatches';
import Teams from '../Pages/Teams/Teams';

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
      <div className="app">
        <Route exact path="/" component={Landing}/>
        <Route path="/home" component={Home}/>
        <Route path="/find-players" component={FindPlayers}/>
        <Route path="/pending-matches" component={PendingMatches}/>
        <Route path="/teams" component={Teams}/>
      </div>
    );
  }
}

export default App;
