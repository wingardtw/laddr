import React from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import NavbarItem from "./NavbarItem";
import Teams from "../Teams/Teams";
import Profile from "../Profile/Profile"
import Home from "../Home/Home"
import Login from "../Login/Login"
import "./Navbar.css"

const Navbar = () => (
  <Router>
    <nav className="navbar">
      <ul className="navbar__list">
        <NavbarItem link="" linkTitle="Home" />
        <NavbarItem link="Teams" linkTitle="Teams" />
        <NavbarItem link="Profile" linkTitle="Profile" />
        <NavbarItem link="Login" linkTitle="Login" />

      </ul>

      <hr />

      <Route exact path="/" component={Home} />
      <Route path="/Teams" component={Teams} />
      <Route path="/Profile" component={Profile} />
      <Route path="/login" component={Login} />
    </nav>
  </Router>
);

export default Navbar;
