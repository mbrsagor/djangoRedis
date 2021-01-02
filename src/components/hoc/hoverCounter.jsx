import React, { Component } from 'react';
// import {withCounter} from './hoc_component';

class HoverCounter extends Component {

    render() {
        return (
            <div>
                <h3>On Mouse Over</h3>
                <button onMouseOver={this.props.increment} className="btn btn-info">hover {this.props.count} time</button>
            </div>
        )
    }
}

export default HoverCounter
