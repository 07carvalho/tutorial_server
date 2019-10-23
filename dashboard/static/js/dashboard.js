$(document).ready(function() {
    var ctx = document.getElementById('myChart');
    console.log(REPORT_DATA);
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: REPORT_DATA.c,
            datasets: [{
                label: 'Total Values',
                data: REPORT_DATA.d,
            }]
        },
    });

    var progValues = $(".progress-value");
    progValues.each(function() {
        var value = $(this).attr('data-value')
        $(this).animate({width: value + '%'}, 10);
    });

    setTimeout(function() {
        window.location.reload(true);
    }, 300000);
});