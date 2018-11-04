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
                        <p className="home__next_game__title">next game:</p>
                        <p className="home__next_game__copy">54 minutes with Lorem</p>
                    </div>
                    <div className="home__cta">
                        <p className="home__cta__copy">
                            Need a new duo partner?
                        </p>
                        <button className="home__cta__btn btn--primary">TEAM UP</button>
                    </div>
                    <div className="test"></div>
                </PageContent>
            </Page>
        )
    }
}

export default Home;