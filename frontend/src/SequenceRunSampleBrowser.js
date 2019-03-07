import React, { Component } from 'react';

import MiseqSequenceRunTable from "./MiseqSequenceRunTable";
import MiseqSampleTable from "./MiseqSampleTable";

import './SequenceRunSampleBrowser.css';

class SequenceRunSampleBrowser extends Component {
    render() {
	return (
	      <div className="rowContainer">
		<MiseqSequenceRunTable />
		<MiseqSampleTable />
	      </div>
	);
    }
}

export default SequenceRunSampleBrowser;
