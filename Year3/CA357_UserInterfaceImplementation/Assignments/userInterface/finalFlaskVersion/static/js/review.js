var main = function() {
  // only "Post" button will have this
  // (i.e. prevents all buttons having "disabled" state)
  $('.review-post').click(function() {
    var post = $('.status-box').val();
    $('<li>').text(post).prependTo('.posts');
    $('.status-box').val('');
    $('.counter').text('140');
    $('.review-post').addClass('disabled'); 
  });
  
  $('.status-box').keyup(function() {
    var postLength = $(this).val().length;
    var charactersLeft = 140 - postLength;
    $('.counter').text(charactersLeft);
  
    if(charactersLeft < 0) {
      $('.review-post').addClass('disabled'); 
    }
    else if(charactersLeft == 140) {
      $('.review-post').addClass('disabled');
    }
    else {
      $('.review-post').removeClass('disabled');
    }
  });
  
  $('.review-post').addClass('disabled');
}

$(document).ready(main);