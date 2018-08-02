import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import NavbarItem from './NavbarItem';

class Navbar extends Component {
    render() {
        return (
            <ul>
                <NavbarItem link="Home" />
                <NavbarItem link="Teams" />
                <NavbarItem link="Compete" />
                <NavbarItem link="Profile" />
                <NavbarItem link="Store" />
            </ul>
        );
    }
}

export default Navbar;