import React, { Component } from 'react';
import { Link } from "react-router-dom";

import './Header.css';

class Header extends Component {
 
    render() {
	return (
	    <header>
	      <div className="header title">
		<Link to="/"><h1>SeqUDAS</h1></Link>
	      </div>
	    </header>
	);
    }
}

export default Header;
