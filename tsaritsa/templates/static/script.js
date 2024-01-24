console.log("hello world");
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const userInput = document.getElementById('user-input');
    const chatOutput = document.getElementById('chat-output');
    chatOutput.innerHTML = '';
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const userMessage = userInput.value.trim();
        if (userMessage !== '') {
            sendMessage(userMessage);
            userInput.value = '';
        }
    });

    function sendMessage(message) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/send_message', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                updateChat(response.chat_history);
            }
        };
        const data = 'user_input=' + encodeURIComponent(message);
        xhr.send(data);
    }

    function updateChat(messages) {
        chatOutput.innerHTML = '';

        messages.forEach(function (message) {
            const paragraph = document.createElement('p');
            paragraph.textContent = message.content;
            chatOutput.appendChild(paragraph);
        });
    }
});
