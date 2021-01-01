import React, { Component } from 'react';

class Lifting extends Component {

    constructor(props) {
        super(props);
        this.state = {temperature: ''};
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange = e => {
        this.setState({temperature: e.target.value})
    }

    render() {
        return (
            <div>
                <div className="form-group">
                    <label htmlFor="name">Enter your name</label>
                    <input type="text"
                        className="form-control"
                        placeholder="Enter your name"
                        id="name"
                        value={this.state.temperature}
                        onChange={this.handleChange} 
                    />
               </div>
            </div>
        );
    }
}

export default Lifting;
