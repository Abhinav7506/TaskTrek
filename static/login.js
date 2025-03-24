function login(event){
    event.preventDefault();
    const Name=document.getElementById('username').value
    const Password=document.getElementById('password').value

    fetch('/api/login',{
        method:'POST',
        headers: {
            'Content-Type':"application/json"
        },
        body:JSON.stringify({
            username:Name,
            password:Password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect){
            window.location.href=data.redirect;
        }
    })
}
