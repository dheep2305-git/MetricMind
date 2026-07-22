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
async function loadTopProducts(){

    let response = await fetch("http://127.0.0.1:8000/top-products");

    let data = await response.json();

    let table = document.querySelector("#productTable tbody");

    table.innerHTML = "";

    for(let product in data){

        table.innerHTML += `
        <tr>
            <td>${product}</td>
            <td>₹ ${data[product].toFixed(2)}</td>
        </tr>
        `;
    }

}

loadTopProducts();
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