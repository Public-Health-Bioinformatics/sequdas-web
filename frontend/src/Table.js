import React, { Component } from "react";
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-balham.css';

class Table extends Component {
    constructor(props) {
	super(props);

	this.state = {
	    columnDefs: [
                {headerName: "Run ID", field: "run_id"},
                {headerName: "Cluster Density (k/mm^2)", field: "cluster_density"},
                {headerName: "Clusters PF (%)", field: "clusters_passed_filter_percent"}
	    ]
	};
    }
    componentDidMount() {
	fetch('/api/sequenceruns/')
	    .then(result => result.json())
	    .then(rowData => this.setState({rowData}));
    }
    render() {
	return (
	    <div
              className="ag-theme-balham"
              style={{
                  height: "500px",
                  width: "600px",
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
