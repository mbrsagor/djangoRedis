import React, { Component } from 'react';
import Counter from './components/counter';
import AboutMe from './components/about';
import Clock from './components/clock';
import Conditional from './components/conditional';
import Lifting from './components/lifting';

class App extends Component {

    render() {
        return (
            <div className="container">
                <div className="row mb-3 mt-3">
                    <div className="col-md-4">
                        
                    </div>
                    <div className="col-md-4">
                        <Lifting />
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-3">
                        <Conditional />
                    </div>
                    <div className="col-md-3">
                        <Counter />
                    </div>
                    <div className="col-md-3">
                        <AboutMe />
                    </div>
                    <div className="col-md-3">
                        <Clock />
                    </div>
                </div>
            </div>
        );
    }
}

export default App;
