document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);
    var name = formData.get('name');
    var comment = formData.get('comment');
    var rating = formData.get('rating');

    // Simulate submitting data to server (not implemented in this example)
    console.log('Name:', name);
    console.log('Comment:', comment);
    console.log('Rating:', rating);

    // Update chart
    updateChart(rating);
});

function updateChart(rating) {
    var chartData = {
        labels: ['Excellent', 'Good', 'Average', 'Below Average', 'Poor'],
        datasets: [{
            label: 'Feedback',
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
            data: [0, 0, 0, 0, 0] // Initialize with zeros
        }]
    };

    // Increment the corresponding rating count
    switch (rating) {
        case 'Excellent':
            chartData.datasets[0].data[0]++;
            break;
        case 'Good':
            chartData.datasets[0].data[1]++;
            break;
        case 'Average':
            chartData.datasets[0].data[2]++;
            break;
        case 'Below Average':
            chartData.datasets[0].data[3]++;
            break;
        case 'Poor':
            chartData.datasets[0].data[4]++;
            break;
        default:
            break;
    }

    var ctx = document.getElementById('barChart').getContext('2d');
    var barChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            responsive: true,
            legend: {
                display: false
            },
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        stepSize: 1
                    }
                }]
            }
        }
    });
}
