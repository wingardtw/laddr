import React, { Component } from 'react';


class Home extends Component {
    render() {
        return (
        <div className="container">
            <div className="landing__left">
                <h2 className="pageTitle fontsize2">Hand-crafted teams</h2>
                <p className="landing__copy">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam magnam veritatis sunt fugit nemo.</p>
                <button className="landing__cta btn--primary">Call to action</button>
            </div>
            <div className="landing__right">
                <img src={require("../../img/LaddrLogoFlat.svg")} alt=""/>
            </div>
        </div>
        )
    }
}

export default Home;