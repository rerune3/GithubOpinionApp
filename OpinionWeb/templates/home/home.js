var home = {};

window.onload = function() {
  // var request = {};
  // request.type = 'USER';
  // httpGetAsync(window.location.href, function(response) {
  //   console.log("yo");
  // }, JSON.stringify(request));
  home.setupListeners();
  homeHandler.retrievePostList();
};

home.setupListeners = function() {
  var elem = document.getElementById("post_button");
  elem.addEventListener("click", homeCallback.postPostButtonCallback);

  var elem = document.getElementById("comment_post_button");
  elem.addEventListener("click", homeCallback.postCommentButtonCallback);

  elem = document.getElementById("ask_question_post");
  elem.addEventListener("click", homeCallback.askQuestionPostCallback);

  elem = document.getElementById("modal_window");
  elem.addEventListener("click", homeCallback.modalWindowCallback);

  elem = document.getElementsByClassName("view_button");
  for (var i = 0; i < elem.length; i++) {
    elem[i].addEventListener("click", homeCallback.viewButtonCallback);
  }
};
