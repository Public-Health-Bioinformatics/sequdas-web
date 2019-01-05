import React, { Component } from 'react';
import ReactDOM from "react-dom";
import { Switch, Route } from 'react-router-dom';
import { BrowserRouter } from 'react-router-dom';

import Header from "./Header"
import Table from "./Table";

class App extends Component {
    render() {
	return (
                <div>
                  <Header />
                  <Table />
                </div>	
	);
    }
}

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;
