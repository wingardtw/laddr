import React, { Component } from 'react';
import Page from '../Page';
import PageContent from '../PageContent';
import PlayerCard from './PlayerCard';

class FindPlayers extends Component {
    render() {
        return (
            <Page
                title="Find Players"
                subtitle="Showing curated matches">
                <PageContent>
                    <div className="matches__attributes">
                    <div className="matches__card__info">
                                <ul className="matches__card__attributes matches__card__attributes--side">
                                    <li className="matches__card__attribute">Rank</li>
                                    <li className="matches__card__attribute">Role</li>
                                    <li className="matches__card__attribute">Region</li>
                                    <li className="matches__card__attribute">Language</li>
                                    <li className="matches__card__attribute">Bio</li>
                                </ul>
                            </div>
                    </div>
                    <div className="matches__container">
                        <PlayerCard 
                            username="Lorem"
                            rank="Gold IV"
                            role="top"
                            region="NA"
                            language="EN"
                            bio="this is a story all about how"
                        />
                        <PlayerCard 
                            username="Ipsum"
                            rank="Gold IV"
                            role="top"
                            region="NA"
                            language="EN"
                            bio="this is a story all about how"
                        />
                        <PlayerCard 
                            username="Dolor"
                            rank="Gold IV"
                            role="top"
                            region="NA"
                            language="EN"
                            bio="this is a story all about how"
                        />

                    </div>
                </PageContent>
            </Page>
        )
    }
}

export default FindPlayers;