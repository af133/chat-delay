// Fungsi Registrasi
async function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;

    const response = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    alert(data.message);
}

// Fungsi Login
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    if (data.success) {
        window.location.href = 'delay-chat.html';
    } else {
        alert('Login gagal');
    }
}

// Fungsi Delay Chat
async function scheduleMessage() {
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;
    const scheduleTime = document.getElementById('schedule-time').value;

    const response = await fetch('/api/delay_chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone, message, scheduleTime })
    });
    const data = await response.json();
    alert(data.message);
}
