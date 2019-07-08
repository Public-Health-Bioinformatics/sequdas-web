import React, { Component } from "react";
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-balham.css';

class MiseqSampleTable extends Component {
    constructor(props) {
	super(props);

	this.state = {
	    columnDefs: [
		{headerName: "Sample ID", field: "sample_id"},
	    ]
	};
    }
    componentDidMount() {
	const fetchSequenceRuns = async () => {
	    const response = await fetch('/api/miseqsamples/');
	    const value = await response.json();
	    return value;
	} 
	fetchSequenceRuns()
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

export default MiseqSampleTable;
