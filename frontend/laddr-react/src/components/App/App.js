import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Home from "../Home/Home"
import Teams from "../Teams/Teams"
import Profile from "../Profile/Profile"
import Navigation from '../Navigation/Navigation';

class App extends Component {
  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <div className="wrapper">
            <Navigation />
            <div className="route__container">
              <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/Teams" component={Teams} />
                <Route path="/Profile" component={Profile} />
              </Switch>
            </div>
          </div>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
