// ==========================================
// API BASE URL
// ==========================================

const API_URL = "https://metricmind-fpgk.onrender.com";

// ==========================================
// LOAD DASHBOARD CARDS
// ==========================================

async function loadDashboard() {

    try {

        // --------------------------------------
        // Total Sales
        // --------------------------------------

        const salesResponse =
            await fetch(`${API_URL}/total-sales`);

        const salesData =
            await salesResponse.json();

        if (salesData.total_sales !== undefined) {

            document.getElementById("sales").innerHTML =
                "₹ " + Number(
                    salesData.total_sales
                ).toFixed(2);

        }


        // --------------------------------------
        // Total Profit
        // --------------------------------------

        const profitResponse =
            await fetch(`${API_URL}/total-profit`);

        const profitData =
            await profitResponse.json();

        if (profitData.total_profit !== undefined) {

            document.getElementById("profit").innerHTML =
                "₹ " + Number(
                    profitData.total_profit
                ).toFixed(2);

        }


        // --------------------------------------
        // Total Orders
        // --------------------------------------

        const ordersResponse =
            await fetch(`${API_URL}/total-orders`);

        const ordersData =
            await ordersResponse.json();

        if (ordersData.total_orders !== undefined) {

            document.getElementById("orders").innerHTML =
                ordersData.total_orders;

        }

    }

    catch (error) {

        console.error(
            "Dashboard error:",
            error
        );

    }

}


// ==========================================
// TOP PRODUCTS
// ==========================================

async function loadTopProducts() {

    try {

        const response =
            await fetch(
                `${API_URL}/top-products`
            );

        const data =
            await response.json();

        const table =
            document.querySelector(
                "#productTable tbody"
            );

        table.innerHTML = "";

        for (const product in data) {

            table.innerHTML += `
                <tr>
                    <td>${product}</td>
                    <td>
                        ₹ ${Number(
                            data[product]
                        ).toFixed(2)}
                    </td>
                </tr>
            `;

        }

    }

    catch (error) {

        console.error(
            "Top products error:",
            error
        );

    }

}


// ==========================================
// SALES BY REGION
// ==========================================

async function loadRegionChart(
    region = "All"
) {

    try {

        const response =
            await fetch(
                `${API_URL}/sales-by-region?region=${encodeURIComponent(region)}`
            );

        const data =
            await response.json();

        const labels =
            Object.keys(data);

        const values =
            Object.values(data);

        const canvas =
            document.getElementById(
                "salesChart"
            );

        if (
            window.salesChart
            instanceof Chart
        ) {

            window.salesChart.destroy();

        }

        const ctx =
            canvas.getContext("2d");

        window.salesChart =
            new Chart(
                ctx,
                {

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

                }
            );

    }

    catch (error) {

        console.error(
            "Region chart error:",
            error
        );

    }

}


// ==========================================
// REGION FILTER
// ==========================================

document
    .getElementById("regionFilter")
    .addEventListener(
        "change",
        function () {

            loadRegionChart(
                this.value
            );

        }
    );


// ==========================================
// PROFIT BY CATEGORY
// ==========================================

async function loadProfitChart() {

    try {

        const response =
            await fetch(
                `${API_URL}/profit-by-category`
            );

        const data =
            await response.json();

        const labels =
            Object.keys(data);

        const values =
            Object.values(data);

        const canvas =
            document.getElementById(
                "profitChart"
            );

        if (
            window.profitChart
            instanceof Chart
        ) {

            window.profitChart.destroy();

        }

        const ctx =
            canvas.getContext("2d");

        window.profitChart =
            new Chart(
                ctx,
                {

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

                }
            );

    }

    catch (error) {

        console.error(
            "Profit chart error:",
            error
        );

    }

}


// ==========================================
// MONTHLY SALES
// ==========================================

async function loadMonthlySalesChart() {

    try {

        const response =
            await fetch(
                `${API_URL}/monthly-sales`
            );

        const data =
            await response.json();

        const labels =
            Object.keys(data);

        const values =
            Object.values(data);

        const canvas =
            document.getElementById(
                "monthlySalesChart"
            );

        if (
            window.monthlySalesChart
            instanceof Chart
        ) {

            window.monthlySalesChart.destroy();

        }

        const ctx =
            canvas.getContext("2d");

        window.monthlySalesChart =
            new Chart(
                ctx,
                {

                    type: "line",

                    data: {

                        labels: labels,

                        datasets: [{

                            label: "Monthly Sales",

                            data: values,

                            borderColor: "#2196F3",

                            backgroundColor:
                                "rgba(33,150,243,0.2)",

                            fill: true,

                            tension: 0.4

                        }]

                    },

                    options: {

                        responsive: true,

                        scales: {

                            y: {

                                beginAtZero: true

                            }

                        }

                    }

                }
            );

    }

    catch (error) {

        console.error(
            "Monthly sales error:",
            error
        );

    }

}


// ==========================================
// AI CHATBOT
// ==========================================

async function askAI() {

    const question =
        document.getElementById(
            "question"
        ).value;


    if (question.trim() === "") {

        alert(
            "Please enter a question."
        );

        return;

    }


    document.getElementById(
        "answer"
    ).innerHTML =
        "🤖 Thinking...";


    try {

        const response =
            await fetch(
                `${API_URL}/ask-ai`,
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body: JSON.stringify({

                        question:
                            question

                    })

                }
            );


        const data =
            await response.json();


        document.getElementById(
            "answer"
        ).innerHTML =
            data.answer ||
            "No answer received.";

    }

    catch (error) {

        console.error(
            "AI error:",
            error
        );

        document.getElementById(
            "answer"
        ).innerHTML =
            "❌ Error connecting to AI.";

    }

}


// ==========================================
// LOGOUT
// ==========================================

function logout() {

    localStorage.removeItem(
        "loggedIn"
    );

    window.location.href =
        "login.html";

}


// ==========================================
// INITIAL DASHBOARD LOAD
// ==========================================

loadDashboard();

loadTopProducts();

loadRegionChart();

loadProfitChart();

loadMonthlySalesChart();