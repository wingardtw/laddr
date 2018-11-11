import React, { Component } from 'react';
import PlayerCard from '../FindPlayers/PlayerCard';

class PendingTabPanels extends Component {
    render() {
        return (
           <div className="pending_tab_panels">
               <div className="pending_tab__entries"></div>
               <div className="pending_tab__request"></div>
               <div className="pending_tab__player_card">
                   <PlayerCard />
               </div>
           </div>
        )
    }
}

export default PendingTabPanels;