import React, { Component } from 'react';

class Lifting extends Component {

    constructor(props) {
        super(props);
        this.state = {
            name: '',
            email: ''
        };
        // this.handleChange = this.handleChange.bind(this);
        // this.submitHandler = this.submitHandler.bind(this);
    }

    handleChange = e => {
        this.setState({name: e.target.value})
    }

    submitHandler = event => {
        console.log({name: this.state.name});
        event.preventDefault();
    }

    render() {
        return (
            <div>
                <form onSubmit={this.submitHandler}>
                    <div className="form-group">
                        <label htmlFor="name">Enter your name</label>
                        <input type="text"
                            className="form-control"
                            placeholder="Enter your name"
                            id="name"
                            name="name"
                            value={this.state.name}
                            onChange={this.handleChange} 
                        />
                    </div>
                    <button type="submit" className="btn btn-success btn-sm">Save</button>
                </form>
            </div>
        );
    }
}

export default Lifting;
