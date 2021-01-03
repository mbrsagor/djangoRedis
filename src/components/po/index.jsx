import React, { Component } from 'react'

class PerformOptimization extends Component {

    constructor(props) {
        super(props)
        this.state = {count: 1}
    }
    
    // shouldComponentUpdate(nextProps, nextState) {
    //     if (this.props.color !== nextProps.color) {
    //         return true
    //     }

    //     if(this.state.count !== nextState.count) {
    //         return true
    //     }
    //     return false;
    // }

    render() {
        return (
            <div>
                <h2>Perform Optimization</h2>
                <button
                    color={this.props.color}
                    onClick={() => this.setState(state => ({count:state.count +1}))}
                    className="btn btn-primary btn-sm">
                    Count: {this.state.count}
                </button>
            </div>
        )
    }
}

export default PerformOptimization
