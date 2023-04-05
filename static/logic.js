d3.json('/data').then((data)=>console.log(data));

anychart.onDocumentReady(function() {

//set the data
var data = [
    {x: "manufacturing", value: 16.5},
    {x: "agriculture", value: 14674252},
    {x: "industry", value: 30.7},
    {x: "services", value: 53.3},
];

// create the chart
var chart = anychart.pie();

// set the chart title
chart.title("Ecuador's GDP Contributions");

// add the data
chart.data(data);

// display the chart in the container
chart.container('container');
chart.draw();

});