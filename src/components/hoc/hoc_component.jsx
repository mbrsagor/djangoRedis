import React, { Component } from 'react';

const withCounter = (HocComponent) => {
    class CommonComponent extends Component {

    constructor(props) {
        super(props)
        this.state = {
            count: 0
        }
    }

    increment = () =>{
        this.setState({count:this.state.count + 1})
    }
    render() {
        return <HocComponent count={this.state.count} increment={this.increment}/>
        }
    }
    
    return CommonComponent;
}

export default withCounter;
