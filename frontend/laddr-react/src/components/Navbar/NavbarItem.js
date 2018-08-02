import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class NavbarItem extends Component {
    render() {
        return (
            <li>
                <Link to={"/" + this.props.link}>{this.props.link}</Link>
            </li>

        );
    }
}

export default NavbarItem;