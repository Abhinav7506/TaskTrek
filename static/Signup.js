function signup(event) {
    event.preventDefault();
    const Name = document.getElementById('username').value;
    const Email = document.getElementById('email').value;
    const Password = document.getElementById('password').value;

    fetch('/api/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: Email,
            username: Name,
            password: Password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
    }})}