import React from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Test from './Test.js';
import Navbar from "./Navbar/Navbar.js";

const BasicExample = () => (
  <Router>
    <div>
      <Navbar />
      
      <hr />

      <Route exact path="/Home" component={Home} />
      <Route path="/Teams" component={Teams} />
      <Route path="/Compete" component={Compete} />
      <Route path="/Profile" component={Profile} />
      <Route path="/Store" component={Store} />
      <Route path="/Test" component={Test} />
    </div>
  </Router>
);

const Home = () => (
  <div>
    <h2>Home</h2>
  </div>
);

const Teams = () => (
  <div>
    <h2>Teams</h2>
  </div>
);
const Compete = () => (
  <div>
    <h2>Compete</h2>
  </div>
);
const Profile = () => (
  <div>
    <h2>Profile</h2>
  </div>
);
const Store = () => (
  <div>
    <h2>Store</h2>
  </div>
);


export default BasicExample;
