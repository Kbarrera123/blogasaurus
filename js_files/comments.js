$(document).ready(() => {
  const commentContent = $('#comment-content');
  $('#comment-form').submit((event) => {
    event.preventDefault();
    $('#no-comments').remove();
    $('#comments')
        .append($('<div/>')
            .append($('<p><i>You wrote:</i></p>'))
            .append($('<p/>', {text: commentContent.val()})));
    commentContent.val('');
    commentContent.focus();
  });
});

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Chrome, Safari and Opera
    document.documentElement.scrollTop = 0; // For IE and Firefox
}
