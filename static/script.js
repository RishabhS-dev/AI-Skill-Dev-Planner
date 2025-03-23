async function getRecommendations() {
    const interest = document.getElementById("interest").value.trim();
    const outputDiv = document.getElementById("output");

    if (!interest) {
        outputDiv.innerHTML = "<p style='color: red;'>Please enter an interest.</p>";
        return;
    }

    outputDiv.innerHTML = "<p>🔄 Generating recommendations...</p>";

    try {
        const response = await fetch("http://127.0.0.1:5000/api/recommend", {  // ✅ Full API URL
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ interest: interest })
        });

        console.log("Response status:", response.status); // Debugging

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        console.log("Response data:", data); // Debugging

        if (data.recommendations) {
            outputDiv.innerHTML = `<p>✅ Recommendations:</p><p>${data.recommendations.replace(/\n/g, "<br>")}</p>`;
        } else {
            outputDiv.innerHTML = "<p style='color: red;'>⚠️ Error fetching recommendations.</p>";
        }
    } catch (error) {
        console.error("Fetch error:", error); // Debugging
        outputDiv.innerHTML = `<p style='color: red;'>❌ An error occurred: ${error.message}</p>`;
    }
}
