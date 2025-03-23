const addBtn=document.querySelector(".addNote");
const newNote=document.querySelector(".note");

addBtn.addEventListener('click',()=>{
    newNote.classList.toggle("show");
    newNote.style.top="140px";
})