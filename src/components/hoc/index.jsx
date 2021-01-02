import React, { Component } from 'react'

class HOC extends Component {

    render() {
        return (
            <div>
                <h3>HOC</h3>
                <button onClick={this.incrementCount} className="btn btn-info">Clicked {this.state.count} time</button>
            </div>
        )
    }
}

export default HOC
