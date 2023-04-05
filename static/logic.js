var chart=null;

d3.json('/heatmap').then(function(heatmap){

    console.log(heatmap);

    var selector=d3.select('#selector');
    var countries=Object.keys(heatmap);
    for (let i=0; i<countries.length; i++){
        selector.append('option')
                .text(countries[i])
                .property('value', countries[i])
    };
    // console.log(countries);
    function plotCountry(countryName){
        console.log(countryName);
        //set the data
        let currentCountryName=countryName
        let currentCountry=heatmap[currentCountryName];
        console.log(currentCountry);

        var data = [
            {x: "manufacturing", value: parseFloat(currentCountry['manufacturing'])},
            {x: "agriculture", value: parseFloat(currentCountry['agriculture'])},
            {x: "industry", value: parseFloat(currentCountry['industry'])},
            {x: "services", value: parseFloat(currentCountry['services'])},
        ];

        anychart.onDocumentReady(function() {
            if (chart!=null){
                // chart.clear();
                // chart.config.data = data;
                chart.data(data);
                chart.title(`${currentCountryName}'s GDP Contributions`);
                // chart.update();
            } else {
                // create the chart
                chart = anychart.pie();

                // set the chart title
                chart.title(`${currentCountryName}'s GDP Contributions`);

                // add the data
                chart.data(data);

                // display the chart in the container
                chart.container('container_angel');
                chart.draw();
            };
        });
    }

    plotCountry('Afghanistan');

    selector.on('change', function(){
        let countrySelected=selector.property('value')
        plotCountry(countrySelected);
    });
})