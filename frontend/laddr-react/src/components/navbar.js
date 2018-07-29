import React, { Component } from 'react';
import '../css/navbar.css';
import logo from '../img/LaddrLogoFlat.svg';

class Navbar extends Component {
  render() {
    return (
      <nav className="navbar">
          <ul className="navbar__list">
            <li className="navbar__item">            
                <img src={logo} className="logo" alt="logo" />
            </li>
            <li className="navbar__item"><a href="#" className="navbar__link">Home</a></li>
            <li className="navbar__item"><a href="#" className="navbar__link">Teams</a></li>
            <li className="navbar__item"><a href="#" className="navbar__link">Compete</a></li>
            <li className="navbar__item"><a href="#" className="navbar__link">Profile</a></li>
            <li className="navbar__item"><a href="#" className="navbar__link">Store</a></li>
          </ul>
      </nav>
    );
  }
}

export default Navbar;