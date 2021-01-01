import React, { Component } from 'react'

export default class Counter extends Component {

    state = {
      name: "Counter",
      count: 0
    };

    increment = () => {
      this.setState({ count: this.state.count + 1 });
    };

    resetHandler = () => {
      this.setState({ count: 0 });
    };


    render() {
        return (
            <div>
                <h2>{this.state.name} : {this.state.count}</h2>
                <button onClick={this.increment} className="btn btn-success btn-sm mr-2">+</button>
                <button onClick={() =>(this.setState({count:this.state.count-1}))} className="btn btn-success btn-sm mr-2">-</button>
                <button onClick={this.resetHandler} className="btn btn-danger btn-sm mr-2">~/</button>
            </div>
        )
    }
}
