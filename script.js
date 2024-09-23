function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (message) {
        addMessage("ഞാൻ: " + message);
        // Here, you would send the message to your backend or API and get the response.
        // For now, we simulate a response.
        simulateResponse(message);
        input.value = ""; // Clear input field
    }
}

function addMessage(text) {
    const messagesDiv = document.getElementById("messages");
    const newMessage = document.createElement("div");
    newMessage.textContent = text;
    messagesDiv.appendChild(newMessage);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to bottom
}

function simulateResponse(userMessage) {
    // Simulated responses. Replace with your API call to get real responses.
    const responses = [
        "എന്റെ പ്രായം 1000 വർഷമാണ്.",
        "ഞാനാണ് മാവേലി, സ്നേഹത്തോടെ വന്നിരിക്കുന്നു.",
        "ഓണം സന്തോഷത്തിന്റെ സീസൺ ആണ്!"
    ];
    const randomResponse = responses[Math.floor(Math.random() * responses.length)];
    setTimeout(() => {
        addMessage("മാവേലി: " + randomResponse);
    }, 1000);
}
