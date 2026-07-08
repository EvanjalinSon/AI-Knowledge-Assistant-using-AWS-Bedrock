const API_URL = "https://6mdd8sp7rf.execute-api.ap-south-1.amazonaws.com/chat";

async function askQuestion() {

    const questionBox = document.getElementById("question");
    const chatBox = document.getElementById("chatBox");

    const question = questionBox.value.trim();

    if (question === "") return;

    chatBox.innerHTML += `
        <div class="message">
            <div class="user">👤 You</div>
            <div>${question}</div>
        </div>
    `;

    questionBox.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const result = await response.json();

        chatBox.innerHTML += `
            <div class="message">
                <div class="ai">🤖 AI Assistant</div>
                <div>${result.answer}</div>
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }
    catch (error) {

        chatBox.innerHTML += `
            <div class="message">
                <div class="ai">❌ Error</div>
                <div>${error.message}</div>
            </div>
        `;

    }

}