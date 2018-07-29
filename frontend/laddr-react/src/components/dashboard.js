import React, { Component } from 'react';
import DashboardItem from './dashboardItem.js';
import '../css/dashboard.css';

class Dashboard extends Component {
    render() {
        return (
            <div className="dashboard">
                <DashboardItem message="hey"/>
            </div>
        )
    }
}

export default Dashboard;