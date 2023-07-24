const postLinks = document.querySelectorAll('.post-link');
const postContentDiv = document.querySelector('#post-content');



postLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        const postId = this.dataset.id;
        fetch(`/blog/api/posts/${postId}/`)
            .then(response => response.json())
            .then(data => {
                let mainContent = `<h2>${data.title}</h2>
                                   <p>${data.content}</p>`;

                let videoContent = '';
                if (data.youtube_video_id) {
                    videoContent = `<iframe width="560" height="315" src="https://www.youtube.com/embed/${data.youtube_video_id}" frameborder="0" allowfullscreen></iframe>`;
                }

                let footerContent = `<p>Author: ${data.author.username}</p>
                                     <p>Date: ${data.date_posted}</p>`;

                let completeContent = mainContent + videoContent + footerContent;

                postContentDiv.innerHTML = completeContent;
            });
    });
});


document.getElementById("send-button").addEventListener("click", function(){
    var message = document.getElementById("message-input").value;
    document.getElementById("message-input").value = '';
    fetch('api/chat/?message=' + message)
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Log the response data
        var messageDisplay = document.getElementById("gpt-display");
        var p = document.createElement('p');
        p.textContent = data.response;
        messageDisplay.appendChild(p);
        document.getElementById("message-input").value = '';
    });
});
// this function is used to create "enter" keypress listener so enter will work instead of clicking

document.getElementById("message-input").addEventListener("keypress", function(event){
    if(event.key === 'Enter'){
        document.getElementById("send-button").click();
    }
});

//to keep the link highlited in the left-side bar for titles 

$(document).ready(function() {
    $('#sidebar ul li a').click(function() {
        $('#sidebar ul li a').removeClass('selected');
        $(this).addClass('selected');
    });
});

