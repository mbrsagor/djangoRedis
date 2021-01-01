import React, { Component } from 'react'

class Clock extends Component {

    constructor(props) {
        super(props);
        this.state = {
            date: new Date(),
            isToggleOn: true
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState(state => ({
            isToggleOn: !state.isToggleOn
        }));
    }

    render() {
        return (
            <div>
                <h1>Hello, world!</h1>
                <h2>It is {this.state.date.toLocaleTimeString()}</h2>
                <a onClick={()=>alert("Hello developer")} href="#0">Click Me</a>
                <button onClick={this.handleClick}>
                    {this.state.isToggleOn ? 'ON' : 'OFF'}
                </button>
            </div>
        )
    }
}

export default Clock;
