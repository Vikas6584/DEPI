/*const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatBox = document.getElementById('chat-box');

chatForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const message = userInput.value;
  userInput.value = '';
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/chatbot');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = () => {
    const response = JSON.parse(xhr.responseText).response;
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.innerHTML = `
      <img src="assets/chatbot.jpg" alt="Chatbot Avatar" class="chatbot-image">
      <p>${response}</p>
    `;
    chatBox.appendChild(messageElement);
  };
  xhr.send(`user_input=${message}`);
});*/

// const form = document.getElementById('chat-form');
// const userInput = document.getElementById('user_input');
// const chatBox = document.querySelector('.chat-box');

// form.addEventListener('submit', (event) => {
//     event.preventDefault();
//     const userMessage = userInput.value;
//     console.log('User Message:', userMessage);
//     //userInput.value = '';
//     console.log('User Message1:', userMessage);
//     const message = document.createElement('div');
//     message.classList.add('message');
//     message.innerHTML = `
//         <img src="assets/user.jpg" alt="User Avatar" class="user-image">
//         <p>${userMessage}</p>
//     `;
//     chatBox.appendChild(message);
//     fetch('/chatbot', {
//         method: 'POST',
//         body: new FormData(form)
//     })
//     .then(response => response.json())
//     .then(data => {
//         const message = document.createElement('div');
//         message.classList.add('message');
//         console.log(data.response);
//         message.innerHTML = `
//             <img src="static/chatbot.jpg" alt="Chatbot Avatar" class="chatbot-image">
//             <p>${data.response}</p>
//         `;
//         chatBox.appendChild(message);
//     });
// });

// const form = document.getElementById('chat-form');
// const userInput = document.getElementById('user_input');
// const chatBox = document.querySelector('.chat-box');

// form.addEventListener('submit', (event) => {
//     event.preventDefault();
//     const userMessage = userInput.value;
//     console.log('User Message:', userMessage);
//     fetch('/chatbot', {
//         method: 'POST',
//         body: new FormData(form)
//     })
//     .then(response => response.json())
//     .then(data => {
//         const message = document.createElement('div');
//         message.classList.add('message');
//         console.log(data.response);
//         message.innerHTML = `
//             <img src="static/chatbot.jpg" alt="Chatbot Avatar" class="chatbot-image">
//             <p>${data.response}</p>
//         `;
//         chatBox.appendChild(message);
//         userInput.value = '';
//     });
// });


const form = document.getElementById('chat-form');
const userInput = document.getElementById('user_input');
const chatBox = document.querySelector('.chat-box');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const userMessage = userInput.value;
    console.log('User Message:', userMessage);
    fetch('/chatbot', {
        method: 'POST',
        body: new FormData(form)
    })
    .then(response => response.json())
    .then(data => {
        const message = document.createElement('div');
        message.classList.add('message');
        console.log(data.response);
        message.innerHTML = `
            <img src="static/chatbot.jpg" alt="Chatbot Avatar" class="chatbot-image">
            <p>${data.response}</p>
        `;
        chatBox.appendChild(message);
        userInput.value = '';
        
        // Speak the response
        speakResponse(data.response);
    });
});

// Function to speak the response
function speakResponse(response) {
    // Create a new speech synthesis object
    const speech = new SpeechSynthesisUtterance();
    
    // Set the text to be spoken
    speech.text = response;
    
    // Speak the text
    window.speechSynthesis.speak(speech);
}
