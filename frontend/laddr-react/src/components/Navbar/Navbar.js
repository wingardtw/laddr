import React from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import NavbarItem from "./NavbarItem";
import Teams from "../Teams/Teams";
import Profile from "../Profile/Profile"
import Home from "../Home/Home"

const Navbar = () => (
  <Router>
    <nav>
      <ul>
        <NavbarItem link="" linkTitle="Home" />
        <NavbarItem link="Teams" linkTitle="Teams" />
        <NavbarItem link="Profile" linkTitle="Profile" />
      </ul>

      <hr />

      <Route exact path="/" component={Home} />
      <Route path="/Teams" component={Teams} />
      <Route path="/Profile" component={Profile} />
    </nav>
  </Router>
);

export default Navbar;
