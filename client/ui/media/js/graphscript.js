// {% load staticfiles %}

// function renderCharts(){
	// setInterval(function renderAll(){
	// 	createChart();
	// var sampledata="testoutput.json";
	// obj = JSON.parse('{"t130816043436": "367", "t130816043427": "369", "t130816043431": "365"}');

	// alert(obj.t130816043436);
	// }, 2000);
	// createChart2();

// }




function createChart()
        {
            //Get the context of the canvas element we want to select
            var ctx = document.getElementById("myChart2").getContext("2d");
 
            //Create the data object to pass to the chart
            var data = {
                labels : ["January","February","March","April","May","June","July"],
                datasets : [
                            {
                                fillColor : "rgba(220,220,220,0.5)",
                                strokeColor : "rgba(220,220,220,1)",
                                data : [65,59,90,81,56,55,40]
                            },
                            {
                                fillColor : "rgba(151,187,205,0.5)",
                                strokeColor : "rgba(151,187,205,1)",
                                data : [28,48,40,19,96,27,100]
                            }
                           ]
                      };
 
            //The options we are going to pass to the chart
            options = {
                barDatasetSpacing : 15,
                barValueSpacing: 10
            };
 
            //Create the chart
            new Chart(ctx).Bar(data, options);
        }

function createChart2()
{
	// Get context
	var ctx=$("#myChart").get(0).getContext("2d");
	// Data
	var data = {
		labels : ["January","February","March","April","May","June","July"],
		datasets : [
			{
				fillColor : "rgba(220,220,220,0.5)",
				strokeColor : "rgba(220,220,220,1)",
				pointColor : "rgba(220,220,220,1)",
				pointStrokeColor : "#fff",
				data : [65,59,90,81,56,55,40]
			},
			{
				fillColor : "rgba(151,187,205,0.5)",
				strokeColor : "rgba(151,187,205,1)",
				pointColor : "rgba(151,187,205,1)",
				pointStrokeColor : "#fff",
				data : [28,48,40,19,96,27,100]
			}
		]
	};
	// Options to be passed in.
	options ={

	};
	// Create line chart
	linechart = new Chart(ctx).Line(data, options);

}