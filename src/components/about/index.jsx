import React, { Component } from 'react';

class AboutMe extends Component {

    state = {
        img: "https://res.cloudinary.com/mbrsagor/image/upload/v1601135422/fashion-ads-big_zs8qev.jpg",
        name: 'Mr.Jon deo',
        about: "I'm full-stack engineer.",
        isAactive: true
    }

    render() {
        return (
            <div>
                <h3>Name: {this.state.name ? this.state.name : 'No name found'}</h3>
                <p>About: {this.state.me || 'Unknown'}</p>
                <img src={this.state.img && this.state.img} className="img-fluid" alt="About Me Pic"/>
            </div>
        );
    }
}

export default AboutMe;
