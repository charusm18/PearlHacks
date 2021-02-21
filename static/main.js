// Emotion Radar Trial Script 
// https://www.chartjs.org/docs/latest/charts/radar.html 

// console.log(myData)
let ctx = document.getElementById('emotion').getContext('2d');

// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';

// Aesthetic Variables
const myLabels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
const myColors = ['pink', 'yellow', 'blue', 'green', 'purple']

let emotionChart = new Chart(ctx, {
    type: 'radar', // bar, horizontalBar, pie, line, donut, radar, polarArea
    data: {
        labels: myLabels,
        datasets: [{
            label: 'Scale: 1-10',
            data: myData,
            backgroundColor: myColors,
            borderWidth: 3,
            borderColor: 'black',
            hoverBorderWidth: 3,
            hoverBorderColor: 'black'
        }]
    },
    options: {
        title: {
            display: true,
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
                suggestedMax: 10
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
        tooltips: { // hover thing
            enabled: true
        },
        responsive: false,
    }
});
