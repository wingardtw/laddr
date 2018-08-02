import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class NavbarItem extends Component {
    render(){
        return (
            <li className="navbar__item">
                <Link to={"/" + this.props.link}>
                {this.props.linkTitle}</Link>
            </li>
        )
    }

}

export default NavbarItem;
