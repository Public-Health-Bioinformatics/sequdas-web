import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import Header from "./Header";
import Login from "./Login";
import Table from "./Table";

class App extends Component {
    render() {
	return (
	    <Router>
	      <div className="App">
		<Header />
		<Route exact path="/" component={Table} />
		<Route exact path='/login/' component={Login} />
	      </div>
	    </Router>
	);
    }
}

export default App;
