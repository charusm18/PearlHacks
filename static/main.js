// Emotion Radar Trial Script 
// https://www.chartjs.org/docs/latest/charts/radar.html 

$(document.getElementById("c")).click(function() {
    $(document.getElementById("col")).toggleClass("rotate");
});

$(document.getElementById("c1")).click(function() {
    $(document.getElementById("col1")).toggleClass("rotate");
});

$(document.getElementById("c2")).click(function() {
    $(document.getElementById("col2")).toggleClass("rotate");
});




// console.log(myData)
let ctx = document.getElementById('emotion').getContext('2d');

// Global Options
Chart.defaults.global.defaultFontFamily = "'josefin-regular'";

// Aesthetic Variables
const myLabels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
const myColors = ['pink', 'yellow', 'blue', 'green', 'purple']

let emotionChart = new Chart(ctx, {
    type: 'radar', // bar, horizontalBar, pie, line, donut, radar, polarArea
    data: {
        labels: myLabels,
        datasets: [{
            label: 'Intensity',
            data: myData,
            borderWidth: 2,
            backgroundColor: "rgba(200,0,0,0.2)",
            borderColor: '#B56576',
            hoverBorderWidth: 3,
            hoverBorderColor: '#B56576',
            hoverRadius: 10,
            pointHitRadius: 15,
            pointHoverBackgroundColor: 'white'
        }]
    },
    options: {
        title: {
            display: false,
            text: 'Emotion',
            fontSize: 25
        },
        legend: {
            display: false,
            position: 'right',
            labels: {
                fontColor: 'black'
            }
        },
        scale: {
            angleLines: {
                display: false
            },
            ticks: {
                suggestedMin: 0,
                suggestedMax: 10,
                fontSize: 10,
                stepSize: 1,
                showLabelBackdrop: false
            },
            pointLabels: {
                fontSize: 22
            }
        },
        layout: {
            padding: {
                left: 50,
                right: 0,
                bottom: 0,
                top: 0
            }
        },
        tooltips: { // thing that shows up when you hover
            enabled: true,
            callbacks: {
                title: (tooltipItem, data) => data.labels[tooltipItem[0].index]
            }
        },
        responsive: false
    }
});
