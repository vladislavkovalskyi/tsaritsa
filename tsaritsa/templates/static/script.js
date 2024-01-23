
document.getElementById('send-button').addEventListener('click', function (event) {
    event.preventDefault(); // предотвращаем отправку формы по умолчанию
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        // Отправка сообщения на сервер
        fetch('/send_message', {
            method: 'POST',
            body: JSON.stringify({ message: userInput }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                // Обработка ответа, если нужно
                console.log(data);
            });

        // Добавление сообщения в чат
        var chatOutput = document.getElementById('chat-output');
        var messageDiv = document.createElement('div');
        messageDiv.textContent = 'Вы: ' + userInput;
        chatOutput.appendChild(messageDiv);

        document.getElementById('user-input').value = ''; // Очистка поля ввода
        document.getElementById('user-input').focus(); // Установка фокуса на поле ввода
    }
});
