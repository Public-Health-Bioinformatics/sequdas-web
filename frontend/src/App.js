import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";

import Header from "./Header";
import Login from "./Login";
import SequenceRunSampleBrowser from "./SequenceRunSampleBrowser";

class App extends Component {
    render() {
	return (
	    <Router>
	      <div className="App">
		<Header />
		<Route exact path="/" component={SequenceRunSampleBrowser} />
		<Route exact path='/login/' component={Login} />
	      </div>
	    </Router>
	);
    }
}

export default App;
