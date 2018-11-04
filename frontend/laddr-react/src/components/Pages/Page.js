import React, { Component } from 'react';
import Nav from '../Nav/Nav'
import PageHeader from './PageHeader';
import Searchbar from './Searchbar';
import PageContent from './PageContent';


class Page extends Component {
    render() {
        return (
            <div className="container">
                <Searchbar />
                <Nav />
                <div className="page__stage">
                    <PageHeader 
                        title={this.props.title}
                        subtitle={this.props.subtitle}
                    />
                    {this.props.children}
                </div>
            </div>
        )
    }
}

export default Page;