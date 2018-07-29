import React, { Component } from 'react';
import '../css/dashboardItem.css';

class DashboardItem extends Component {
    render() {
        return (
            <div className="dashboardItem">
                {this.props.message}
            </div>
        )
    }
}

export default DashboardItem;