function diary(event){
    event.preventDefault();
    const Title = document.querySelector('.Topic input').value;
    const Entry = document.getElementById('content').value;

    if (!Title || !Entry) {
        alert("Please fill out both the topic and diary content!");
        return;}

    fetch('/api/diary',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            Topic: Title,
            content: Entry
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response received:", data);
        if (data.error) {
            alert(`Error: ${data.error}`);
        } else {
            alert(data.message);
            loadDiaries();
        }
})}
document.querySelector('.save').addEventListener('click', diary);


function loadDiaries() {
    fetch('/api/get_diary')
    .then(response => response.json())
    .then(data => {
        console.log("Diaries:", data);
        
        const historyDiv = document.querySelector('.history');
        historyDiv.innerHTML = "<h1>MY DIARIES</h1>"; 

        if (data.error) {
            historyDiv.innerHTML += `<p>Error: ${data.error}</p>`;
            return;
        }

        data.forEach(diary => {
            const diaryElement = document.createElement('div');
            diaryElement.classList.add('diary-entry');
            diaryElement.innerHTML = `
                <h2 class="diary-title" data-topic="${diary}">${diary}</h2>
            `;
            historyDiv.appendChild(diaryElement);
            diaryElement.addEventListener('click', () => loadDiaryContent(diary));
        });
    })}

    function loadDiaryContent(topic) {
        fetch(`/api/display_diary?Topic=${encodeURIComponent(topic)}`)
        .then(response => response.json())
        .then(data => {
            console.log("Diary Content:", data);
    
            if (data.error) {
                alert("Error fetching diary content!");
                return;
            }
    
            document.querySelector('.Topic input').value = topic;
            document.getElementById('content').value = data.content;
        });
    }
    
    document.addEventListener('DOMContentLoaded', loadDiaries);   
document.addEventListener('DOMContentLoaded', loadDiaries);