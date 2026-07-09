const socket = new WebSocket('ws://localhost:8000/ws');
const messagesDiv = document.getElementById('messages');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const statusDiv = document.getElementById('status');

function getTime () {
  const now = new Date();
  return now.getHours() + ':' + String(now.getMinutes()).padStart(2, '0');
}

function addMessage (text, type) {
  const div = document.createElement('div');
  div.className = 'message ' + type;
  div.innerHTML = '<div>' + text + '</div><div class="time">' + getTime() + '</div>';
  messagesDiv.appendChild(div);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

socket.onopen = function () {
  statusDiv.textContent = 'Connected';
  statusDiv.className = 'status connected';
  sendBtn.disabled = false;
};

socket.onclose = function () {
  statusDiv.textContent = 'Disconnected';
  statusDiv.className = 'status disconnected';
  sendBtn.disabled = true;
};

socket.onmessage = function (event) {
  addMessage(event.data, 'received');
};

function sendMessage () {
  const text = messageInput.value.trim();
  if (text === '') return;
  addMessage(text, 'sent');
  socket.send(text);
  messageInput.value = '';
}

sendBtn.addEventListener('click', sendMessage);

messageInput.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') sendMessage();
});

sendBtn.disabled = true;
