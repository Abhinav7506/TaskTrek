const addBtn=document.querySelector(".addNote");
const newNote=document.querySelector(".note");

addBtn.addEventListener('click',()=>{
    newNote.classList.toggle("show");
    newNote.style.top="140px";
})



function new_note(event){
    console.log("Submitting new note...");
    event.preventDefault();

    const content=document.getElementById('new_note').value;

    fetch('/api/notes', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({
            note: content
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response received:", data);
        if (data.error) {
            alert(`Error: ${data.error}`);
        } else {
            alert(data.message);
            window.location.href = data.redirect;
        }
    })}

document.querySelector(".form").addEventListener("submit", new_note);


