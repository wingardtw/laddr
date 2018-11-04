import React, { Component } from 'react';
import Page from '../Page';
import PageContent from '../PageContent';

class Home extends Component {
    render() {
        return (
            <Page
                title="Home"
                subtitle="this is the home dashboard">
                <PageContent>
                    <div className="home__news">
                        <div className="home__news__item"></div>
                        <h2 className="home__news__title">This is news on the homepage</h2>
                    </div>
                    <div className="home__activity">
                        <p className="home__activity__title">Recent activity</p>
                        <div className="home__activity__area">
                            this is stuff
                        </div>
                    </div>
                    <div className="home__next_game">
                        <p>next game:</p>
                        <p>54 minutes with Lorem</p>
                    </div>
                    <div className="home__cta">
                        <p className="home__cta__copy">
                            Need a new duo partner?
                        </p>
                        <button className="home__cta__btn">TEAM UP</button>
                    </div>
                </PageContent>
            </Page>
        )
    }
}

export default Home;