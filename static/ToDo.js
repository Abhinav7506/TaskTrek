const tasks=document.querySelector(".container");
const addBtn=document.querySelector("main span button");

addBtn.addEventListener('click',()=>{
    
    console.log("btn clicked")
    const newTask=document.createElement("div");
    newTask.classList.add("todo");

    const singleCheck=document.createElement("input");
    singleCheck.classList.add("todo_checkbox");
    singleCheck.id="status";
    singleCheck.type="checkbox";


    const singleInput=document.createElement("input");
    singleInput.classList.add("todo_value");
    singleInput.id="task";
    singleInput.type="text";
    singleInput.placeholder="Enter your Task";

    newTask.appendChild(singleCheck);
    newTask.appendChild(singleInput);
    tasks.appendChild(newTask);

});