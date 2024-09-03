// app.js
function updateData() {
  fetch("https://api.yourcloudservice.com/latest-data")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("flow-rate").textContent =
        data.flow_rate.toFixed(2);
      document.getElementById("leak-status").textContent = data.leak_detected
        ? "Yes"
        : "No";
    });
}

setInterval(updateData, 10000); // Update every 10 seconds
