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


//graphics

//!salary
function salary(type_e, data_e, labels_e, data_man, data_woman, from, to, parts) {
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
        var ctx_salary_mw = document.getElementById('salary_mw');
        var myChart = new Chart(ctx_salary_mw, {
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
        var salary_mw = document.getElementById('salary_mw');
        var myChart = new Chart(salary_mw, {
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


        var ctx_salary_mw = document.getElementById('salary_mw');
        var myChart = new Chart(ctx_salary_mw, {
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

    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {
        var ctx_cars = document.getElementById('cars');
        var myChart = new Chart(ctx_cars, {
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
        var ctx_cars = document.getElementById('cars');
        var myChart = new Chart(ctx_cars, {
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


        var ctx_cars = document.getElementById('cars');
        var myChart = new Chart(ctx_cars, {
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

    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {
        var ctx_square = document.getElementById('square');
        var myChart = new Chart(ctx_square, {
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
        var ctx_square = document.getElementById('square');
        var myChart = new Chart(ctx_square, {
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


        var ctx_square = document.getElementById('square');
        var myChart = new Chart(ctx_square, {
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

    for (var i = 0; i <= labels_e.length; i++) {
        if (labels_e[i] <= to & labels_e[i] >= from) {
            labels_o.push(labels_e[i])
        }
    }

    if (type_e == 'mw') {
        var ctx_savings = document.getElementById('savings');
        var myChart = new Chart(ctx_savings, {
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
        var ctx_savings = document.getElementById('savings');
        var myChart = new Chart(ctx_savings, {
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


        var ctx_savings = document.getElementById('savings');
        var myChart = new Chart(ctx_savings, {
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


$("#whithout").click(function() {
    var mode = 'wh'
    window.mode = mode

    from = window.from
    to = window.to




    savings(mode, [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, null)

    flat(mode, [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, null)

    cars(mode, [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, null)

    salary(mode, [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, null)
})
$("#genders").click(function() {
    mode = 'mw'
    from = window.from
    to = window.to

    window.mode = mode
    savings(mode, null, [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [40, 21, 23, 32, 12, 43, 43, 43, 21, 23, 21], [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], from, to, null)
    flat(mode, null, [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [40, 21, 23, 32, 12, 43, 43, 43, 21, 23, 21], [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], from, to, null)
    cars(mode, null, [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [40, 21, 23, 32, 12, 43, 43, 43, 21, 23, 21], [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], from, to, null)
    salary(mode, null, [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [40, 21, 23, 32, 12, 43, 43, 43, 21, 23, 21], [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40], from, to, null)
})

$("#parts").click(function() {
    mode = 'parts'
    window.mode = mode

    from = window.from
    to = window.to

    savings('parts', [
        [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40],
        [20, 21, 60, 30, 51, 26, 41, 39, 22, 28, 40]
    ], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, ['a', 'b'])
    flat('parts', [
        [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40],
        [20, 21, 60, 30, 51, 26, 41, 39, 22, 28, 40]
    ], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, ['a', 'b'])
    cars('parts', [
        [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40],
        [20, 21, 60, 30, 51, 26, 41, 39, 22, 28, 40]
    ], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, ['a', 'b'])
    salary('parts', [
        [10, 20, 30, 40, 25, 32, 44, 33, 32, 32, 40],
        [20, 21, 60, 30, 51, 26, 41, 39, 22, 28, 40]
    ], [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], null, null, from, to, ['a', 'b'])
})
