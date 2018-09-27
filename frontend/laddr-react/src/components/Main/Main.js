import React, { Component } from "react";
import { BrowserRouter as Router, Route} from "react-router-dom";
import Home from "../Home/Home"
import Navbar from '../App/Navbar';

class Main extends Component {
  render() {
    return (
      <Router>
        <div className="main">
          <header className="header">
            <Navbar />
          </header>
          <div className="content">
            <Route path="/" exact component={Home}/>
          </div>

        </div>
      </Router>
    );
  }
}
 
export default Main;