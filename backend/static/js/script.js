const messagesContainer = document.getElementById('messages');

async function sendMessage() {
    const input = document.getElementById('userInput');
    const userMessage = input.value.trim();
    if (!userMessage) return;

    appendMessage('Você', userMessage, 'user');
    input.value = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: userMessage,
                assistant_id: 806
            })
        });

        const data = await response.json();

        const botReply = data.reply || data.error || 'Desculpe, não consegui entender.';

        appendMessage('FeedIA', botReply, 'bot');

    } catch (error) {
        appendMessage('FeedIA', 'Erro na conexão com a IA.', 'bot');
        console.error('Erro:', error);
    }
}

function appendMessage(sender, text, className) {
    const msg = document.createElement('div');
    msg.classList.add('message', className);
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    messagesContainer.appendChild(msg);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
