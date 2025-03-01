document.getElementById('speakButton').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/speak', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
