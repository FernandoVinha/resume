
console.log("teste" );




    fetch('http://127.0.0.1:8000/relatorio_users', {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

    var ctx2 = document.getElementById("chart-line").getContext("2d");


   new Chart(ctx2, {
     type: "line",
     data: {
       labels: data.labels,
       datasets: [{
         label: "Mobile apps",
         tension: 0,
         borderWidth: 0,
         pointRadius: 5,
         pointBackgroundColor: "rgba(255, 255, 255, .8)",
         pointBorderColor: "transparent",
         borderColor: "rgba(255, 255, 255, .8)",
         borderColor: "rgba(255, 255, 255, .8)",
         borderWidth: 4,
         backgroundColor: "transparent",
         fill: true,
         data: data.data,
         maxBarThickness: 6

       }],
     },
     options: {
       responsive: true,
       maintainAspectRatio: false,
       plugins: {
         legend: {
           display: false,
         }
       },
       interaction: {
         intersect: false,
         mode: 'index',
       },
       scales: {
         y: {
           grid: {
             drawBorder: false,
             display: true,
             drawOnChartArea: true,
             drawTicks: false,
             borderDash: [5, 5],
             color: 'rgba(255, 255, 255, .2)'
           },
           ticks: {
             display: true,
             color: '#f8f9fa',
             padding: 10,
             font: {
               size: 14,
               weight: 300,
               family: "Roboto",
               style: 'normal',
               lineHeight: 2
             },
           }
         },
         x: {
           grid: {
             drawBorder: false,
             display: false,
             drawOnChartArea: false,
             drawTicks: false,
             borderDash: [5, 5]
           },
           ticks: {
             display: true,
             color: '#f8f9fa',
             padding: 10,
             font: {
               size: 14,
               weight: 300,
               family: "Roboto",
               style: 'normal',
               lineHeight: 2
             },
           }
         },
       },
     },
   });
})


 var ctx = document.getElementById("users").getContext("2d");

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["w", "T", "W", "T", "F", "S", "S"],
        datasets: [{
          label: "Sales",
          tension: 0.4,
          borderWidth: 0,
          borderRadius: 4,
          borderSkipped: false,
          backgroundColor: "rgba(255, 255, 255, .8)",
          data: [50, 20, 10, 22, 50, 10, 40],
          maxBarThickness: 6
        }, ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: false,
              borderDash: [5, 5],
              color: 'rgba(255, 255, 255, .2)'
            },
            ticks: {
              suggestedMin: 0,
              suggestedMax: 500,
              beginAtZero: true,
              padding: 10,
              font: {
                size: 14,
                weight: 300,
                family: "Roboto",
                style: 'normal',
                lineHeight: 2
              },
              color: "#fff"
            },
          },
          x: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: false,
              borderDash: [5, 5],
              color: 'rgba(255, 255, 255, .2)'
            },
            ticks: {
              display: true,
              color: '#f8f9fa',
              padding: 10,
              font: {
                size: 14,
                weight: 300,
                family: "Roboto",
                style: 'normal',
                lineHeight: 2
              },
            }
          },
        },
      },
    });