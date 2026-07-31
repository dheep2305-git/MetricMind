async function loadDashboard() {

    // Total Sales
    let salesResponse = await fetch("http://127.0.0.1:8000/total-sales");
    let salesData = await salesResponse.json();
    document.getElementById("sales").innerHTML =
        "₹ " + salesData.total_sales.toFixed(2);

    // Total Profit
    let profitResponse = await fetch("http://127.0.0.1:8000/total-profit");
    let profitData = await profitResponse.json();
    document.getElementById("profit").innerHTML =
        "₹ " + profitData.total_profit.toFixed(2);

    // Total Orders
    let ordersResponse = await fetch("http://127.0.0.1:8000/total-orders");
    let ordersData = await ordersResponse.json();
    document.getElementById("orders").innerHTML =
        ordersData.total_orders;
}

loadDashboard();

async function loadTopProducts() {

    let response = await fetch("http://127.0.0.1:8000/top-products");

    let data = await response.json();

    let table = document.querySelector("#productTable tbody");

    table.innerHTML = "";

    for (let product in data) {
        table.innerHTML += `
        <tr>
            <td>${product}</td>
            <td>₹ ${data[product].toFixed(2)}</td>
        </tr>
        `;
    }
}

loadTopProducts();

async function loadRegionChart(region = "All") {

    let response = await fetch(`http://127.0.0.1:8000/sales-by-region?region=${region}`);

    let data = await response.json();

    let labels = Object.keys(data);
    let values = Object.values(data);

    let canvas = document.getElementById("salesChart");

    if (window.salesChart instanceof Chart) {
        window.salesChart.destroy();
    }

    let ctx = canvas.getContext("2d");

    window.salesChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Sales",
                data: values,
                backgroundColor: [
                    "#4CAF50",
                    "#2196F3",
                    "#FFC107",
                    "#F44336"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            }
        }
    });
}

loadRegionChart();

document.getElementById("regionFilter").addEventListener("change", function () {

    let selectedRegion = this.value;
    loadRegionChart(selectedRegion);

});

async function loadProfitChart() {

    let response = await fetch("http://127.0.0.1:8000/profit-by-category");

    let data = await response.json();

    let labels = Object.keys(data);
    let values = Object.values(data);

    let ctx = document.getElementById("profitChart").getContext("2d");

    new Chart(ctx, {
        type: "pie",
        data: {
            labels: labels,
            datasets: [{
                label: "Profit",
                data: values,
                backgroundColor: [
                    "#4CAF50",
                    "#2196F3",
                    "#FFC107"
                ]
            }]
        },
        options: {
            responsive: true
        }
    });
}

loadProfitChart();

async function loadMonthlySalesChart() {

    let response = await fetch("http://127.0.0.1:8000/monthly-sales");

    let data = await response.json();

    let labels = Object.keys(data);
    let values = Object.values(data);

    let ctx = document.getElementById("monthlySalesChart").getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Monthly Sales",
                data: values,
                borderColor: "#2196F3",
                backgroundColor: "rgba(33,150,243,0.2)",
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

loadMonthlySalesChart();