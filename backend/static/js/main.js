$('#open-mobile-menu').click(function() {
    $('.mobile-menu').slideToggle()
    $('#close-mobile-menu').toggle()
})

$('#close-mobile-menu').click(function() {
    $('#close-mobile-menu').toggle()
    $('.mobile-menu').slideToggle()
})

$('.filters button').click(function() {
    $('.active').removeClass('active')
    $(this).addClass('active')
})
$('.filters button').click(function() {
    $('.active').removeClass('active')
    $(this).addClass('active')
})
$('.alert-salary').click(function () {
    $('.hidden-graphics_salary').toggle()
})

$('.alert-square').click(function () {
    $('.hidden-graphics_square').toggle()
})

$('.alert-savings').click(function () {
    $('.hidden-graphics_savings').toggle()
})

//graphics

//!salary
function salary(type_e, data_e, labels_e, data_man, data_woman, from, to, parts) {
    var ctx_salary_mw = document.getElementById('salary_mw');


    var myChart_salary = new Chart(ctx_salary_mw, {
        type: 'line',
    })

    myChart_salary.reset()
    var labels_o = []
    data_o = []
    data_man_o = []
    data_woman_o = []

    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {
        var myChart_salary = new Chart(ctx_salary_mw, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                        label: 'Woman',
                        data: data_woman,
                        borderColor: "blue",
                        borderWidth: 1
                    },
                    {
                        label: 'Man',
                        data: data_man,
                        borderColor: 'red',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });
    }
    if (type_e == 'wh') {
        var myChart_salary = new Chart(ctx_salary_mw, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                    label: 'Whole',
                    data: data_e,
                    borderColor: 'red',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });

    }

    if (type_e == 'parts') {
        datasets_m = []
        colors = ['#B80000', '#B8A800', '#B8FF00', '#B8FF0B', '#B8FFDF', '#B8FF43', '#B8FFEB', '#B839EB', '#0039EB', '#003907', '#594C21', '#522A1A', '#542A35', '#FBF28A', '#009D83', '#BD6D61']

        for (var i = 0; i <= parts.length; i++) {
            if (parts[i] != undefined) {
                datasets_m.push(

                    {
                        label: parts[i],
                        data: data_e[i],
                        borderColor: colors[i],
                        borderWidth: 1
                    }

                )
            }

        }
        var myChart_salary = new Chart(ctx_salary_mw, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: datasets_m,
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });


    }

}
//!CARS
function cars(type_e, data_e, labels_e, data_man, data_woman, from, to, parts) {
    var labels_o = []
    data_o = []
    data_man_o = []
    data_woman_o = []

    var ctx_cars = document.getElementById('cars');
    var myChart_cars = new Chart(ctx_cars, {})
    myChart_cars.reset()

    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {
        var myChart_cars = new Chart(ctx_cars, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                        label: 'Woman',
                        data: data_woman,
                        borderColor: "blue",
                        borderWidth: 1
                    },
                    {
                        label: 'Man',
                        data: data_man,
                        borderColor: 'red',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });
    }
    if (type_e == 'wh') {
        var myChart_cars = new Chart(ctx_cars, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                    label: 'Whole',
                    data: data_e,
                    borderColor: 'red',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });
    }

    if (type_e == 'parts') {
      console.log("HERE@")
        datasets_m = []
        colors = ['#B80000', '#B8A800', '#B8FF00', '#B8FF0B', '#B8FFDF', '#B8FF43', '#B8FFEB', '#B839EB', '#0039EB', '#003907', '#594C21', '#522A1A', '#542A35', '#FBF28A', '#009D83', '#BD6D61']

        for (var i = 0; i <= parts.length; i++) {
            if (parts[i] != undefined) {
                datasets_m.push(

                    {
                        label: parts[i],
                        data: data_e[i],
                        borderColor: colors[i],
                        borderWidth: 1
                    }

                )
            }

        }


        var myChart_cars = new Chart(ctx_cars, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: datasets_m,
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });


    }
}
//!SQUARE
function flat(type_e, data_e, labels_e, data_man, data_woman, from, to, parts) {
    var labels_o = []
    data_o = []
    data_man_o = []
    data_woman_o = []
    var ctx_square = document.getElementById('square');
    var myChart_square = new Chart(ctx_square, {})
    myChart_square.reset()

    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {

        var myChart_square = new Chart(ctx_square, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                        label: 'Woman',
                        data: data_woman,
                        borderColor: "blue",
                        borderWidth: 1
                    },
                    {
                        label: 'Man',
                        data: data_man,
                        borderColor: 'red',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });
    }
    if (type_e == 'wh') {
        var yChart_square = new Chart(ctx_square, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                    label: 'Whole',
                    data: data_e,
                    borderColor: 'red',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });
    }

    if (type_e == 'parts') {
        datasets_m = []
        colors = ['#B80000', '#B8A800', '#B8FF00', '#B8FF0B', '#B8FFDF', '#B8FF43', '#B8FFEB', '#B839EB', '#0039EB', '#003907', '#594C21', '#522A1A', '#542A35', '#FBF28A', '#009D83', '#BD6D61']

        for (var i = 0; i <= parts.length; i++) {
            if (parts[i] != undefined) {
                datasets_m.push(

                    {
                        label: parts[i],
                        data: data_e[i],
                        borderColor: colors[i],
                        borderWidth: 1
                    }

                )
            }

        }


        var yChart_square = new Chart(ctx_square, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: datasets_m,
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });


    }
}


//savings

function savings(type_e, data_e, labels_e, data_man, data_woman, from, to, parts) {
    var labels_o = []
    data_o = []
    data_man_o = []
    data_woman_o = []

    var ctx_savings = document.getElementById('savings');
    var myChart_savings = new Chart(ctx_savings, {})
    myChart_savings.reset()


    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {

        var myChart_savings = new Chart(ctx_savings, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                        label: 'Woman',
                        data: data_woman,
                        borderColor: "blue",
                        borderWidth: 1
                    },
                    {
                        label: 'Man',
                        data: data_man,
                        borderColor: 'red',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                },
                legend: {
                    onClick: (e) => null
                }
            }
        });
    }
    if (type_e == 'wh') {
        var myChart_savings = new Chart(ctx_savings, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: [{
                    label: 'Whole',
                    data: data_e,
                    borderColor: 'red',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });
    }

    if (type_e == 'parts') {
        datasets_m = []
        colors = ['#B80000', '#B8A800', '#B8FF00', '#B8FF0B', '#B8FFDF', '#B8FF43', '#B8FFEB', '#B839EB', '#0039EB', '#003907', '#594C21', '#522A1A', '#542A35', '#FBF28A', '#009D83', '#BD6D61']

        for (var i = 0; i <= parts.length; i++) {
            if (parts[i] != undefined) {
                datasets_m.push(

                    {
                        label: parts[i],
                        data: data_e[i],
                        borderColor: colors[i],
                        borderWidth: 1
                    }

                )
            }

        }


        var myChart_savings = new Chart(ctx_savings, {
            type: 'line',
            data: {
                labels: labels_o,
                datasets: datasets_m,
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }],
                }
            }
        });


    }
}
