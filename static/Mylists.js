const addBtn=document.querySelector(".showlist");
const newNote=document.querySelector(".list");

addBtn.addEventListener('click',()=>{
    newNote.classList.toggle("show");
    newNote.style.top="140px";
})