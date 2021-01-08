> The repo basically `React.JS` simple random example for all every topic.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

#### `React Reducer` simple example

```javascript
import React, {useReducer} from 'react';


const initalData = 0;

const reducer = (state, action) => {
    switch (action.type) {
        case 'increment':
            return state + 1;
        case 'decrement':
            return state - 1;
        case 'reset':
            return 0;
        default: return state;
    }
}

const MyReducer = props => {

    const [count, dispatch] = useReducer(reducer, initalData);
    const [number, dispatch2] = useReducer(reducer, 10);

    return (
        <div>
            <h2>I am use Reducer</h2>
            <h3>Count: {count}</h3>
            <button onClick={() => dispatch({type: 'increment'})} className="btn btn-success btn-sm mr-2">+</button>
            <button onClick={() => dispatch({type: 'decrement'})} className="btn btn-success btn-sm mr-2">-</button>
            <button onClick={() => dispatch({type: 'reset'})} className="btn btn-danger btn-sm mr-2">(0)</button>
            <hr />
            <br />
            <h3>Count: {number}</h3>
            <button onClick={() => dispatch2({type: 'increment'})} className="btn btn-success btn-sm mr-2">+</button>
            <button onClick={() => dispatch2({type: 'decrement'})} className="btn btn-success btn-sm mr-2">-</button>
            <button onClick={() => dispatch2({type: 'reset'})} className="btn btn-danger btn-sm mr-2">(0)</button>
        </div>
    );
}

export default MyReducer;

```