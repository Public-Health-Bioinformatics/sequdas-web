import React, { Component } from "react";
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-balham.css';

class Table extends Component {
    constructor(props) {
	super(props);

	this.state = {
	    columnDefs: [
		{headerName: "Sequencer", field: "sequencer"},
                {headerName: "Run ID", field: "run_id"},
                {headerName: "Cluster Density (k/mm^2)", field: "cluster_density"},
                {headerName: "Clusters PF (%)", field: "clusters_passed_filter_percent"}
	    ]
	};
    }
    componentDidMount() {
	const fetchSequenceRuns = async () => {
	    const response = await fetch('/api/sequenceruns/');
	    const value = await response.json();
	    return value;
	} 
	const fetchSequencerId = async (sequenceruns) => {
	    const updatedSequenceRuns = await Promise.all(sequenceruns.map(
		async (sequencerun) => Object.assign(sequencerun, {sequencer: await fetch(new URL(sequencerun.sequencer).pathname)
								   .then(result => result.json())
								   .then(result => result.sequencer_id)})
	    ))
	    return updatedSequenceRuns;
	}
	fetchSequenceRuns()
	    .then(sequenceruns => fetchSequencerId(sequenceruns))
	    .then(rowData => this.setState({rowData}))
    }
    render() {
	return (
	    <div
              className="ag-theme-balham"
              style={{
                  height: "500px",
                  width: "800px",
                  align: "left"
              }}
              >
              <AgGridReact
                enableSorting={true}
                rowSelection="single"
	        columnDefs={this.state.columnDefs}
                rowData={this.state.rowData}>
              </AgGridReact>
            </div>
        );
    }
}

export default Table;
