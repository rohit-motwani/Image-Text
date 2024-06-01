document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('paste', function (event) {
        const items = (event.clipboardData || event.originalEvent.clipboardData).items;
        for (let item of items) {
            if (item.type.startsWith('image/')) {
                const file = item.getAsFile();
                const reader = new FileReader();
                reader.onload = function (event) {
                    const base64Image = event.target.result;
                    fetch('/upload_paste', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ image: base64Image })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.extracted_text) {
                            document.getElementById('result').innerHTML = `
                                <div class="result">
                                    <h2>Extracted Text:</h2>
                                    <textarea rows="10" readonly>${data.extracted_text}</textarea>
                                </div>
                            `;
                        } else {
                            alert('Failed to extract text.');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('An error occurred while processing the image.');
                    });
                };
                reader.readAsDataURL(file);
            }
        }
    });
});
