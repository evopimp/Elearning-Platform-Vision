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
    var conversationArea = document.getElementById("Conv-Container"); // use a single container for the whole conversation

    // Create a paragraph for the user's message and append it to the conversation area
    var userMessage = document.createElement('p');
    userMessage.classList.add('user-message'); // Add a class to style user messages differently
    userMessage.innerHTML = message;
    conversationArea.appendChild(userMessage);

    document.getElementById("message-input").value = '';
    fetch('api/chat/?message=' + message)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            var aiMessage = document.createElement('p');
            aiMessage.classList.add('ai-message'); // Add a class to style AI messages differently
            var responseText = data.response.replace(/\./g, '.<br>').replace(/\:/g, ':<br>');
            aiMessage.innerHTML = responseText;
            conversationArea.appendChild(aiMessage);
        });
});


// document.getElementById("send-button").addEventListener("click", function(){
//     var message = document.getElementById("message-input").value;
//     var userMessage = document.getElementById("user-message");
//     var grpah = document.createElement('p');
//     grpah.innerHTML = message;
//     userMessage.appendChild(grpah);
//     console.log(userMessage);

//     document.getElementById("message-input").value = '';
//     fetch('api/chat/?message=' + message)
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);  // Log the response data
//         var messageDisplay = document.getElementById("gpt-text");
//         var p = document.createElement('p');
//         var responseText = data.response.replace(/\./g, '.<br>').replace(/\:/g, ':<br>');

//         p.innerHTML = responseText;

//         messageDisplay.appendChild(p);

//     });
// });


// this function is used to create "enter" keypress listener so enter will work instead of clicking

document.getElementById("message-input").addEventListener("keypress", function(event){
    if(event.key === 'Enter'){
        document.getElementById("send-button").click();
    }
});

//to keep the link highlited in the left-side bar for the lessons tiltle 

$(document).ready(function() {
    $('#sidebar ul li a').click(function() {
        $('#sidebar ul li a').removeClass('selected');
        $(this).addClass('selected');
    });
});

