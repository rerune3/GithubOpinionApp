var homeCallback = {};

homeCallback.postPostButtonCallback = function() {
  homeHandler.insertNewPost();
  location.reload();
};

homeCallback.postCommentButtonCallback = function() {
  var post_id = document.getElementById("post_view").name;
  homeHandler.insertNewComment(post_id);
};

homeCallback.askQuestionPostCallback = function() {
  var modal_elem = document.getElementById("modal_window");
  var form_elem = document.getElementById("post_form");
  modal_elem.style.display = "block";
  form_elem.style.display = "block";
};

homeCallback.modalWindowCallback = function(event) {
  if (event.target.id === "modal_window") {
    var modal_elem = document.getElementById("modal_window");
    // Set all children hidden.
    for (var i = 0; i < modal_elem.children.length; i++) {
      modal_elem.children[i].style.display = "none";
    } // end for
    // Set modal element to hidden after.
    modal_elem.style.display = "none";
    homeHelper.destroyComments();
  } // end if
};

homeCallback.viewButtonCallback = function(event) {
  var modal = document.getElementById("modal_window");
  var view_elem = document.getElementById("post_comment_view");
  var post_element = event.target.parentNode.parentNode;
  var post = homeHelper.extractPostHTMLInfoFromElement(post_element);

  homeHelper.constructAndAppendPostViewToDOM(post.post_id);

  modal.style.display = "block";
  view_elem.style.display = "block";

  homeHandler.retrieveCommentList(post);
};

homeCallback.httpPostAsyncCallback = function(response) {
  console.log("This shouldnt be a thing.");
};

homeCallback.insertNewPostCallback = function(response) {
  console.log("Insert new post callback.");
  console.log(response);
};

homeCallback.insertNewCommentCallback = function(response) {
  console.log("Insert new comment callback.");
  console.log(response);
};

homeCallback.deleteCommentCallback = function(response) {
  console.log("Delete comment callback.");
  console.log(response);
};

homeCallback.deletePostCallback = function(response) {
  console.log("Delete post callback.");
  console.log(response);
};

homeCallback.retrievePostCallback = function(response) {
  console.log("Retrieve post callback.");
  console.log(response);
};

homeCallback.retrievePostListCallback = function(response) {
  console.log("Retrieve post list callback.");
  console.log(response);

  var response_object = JSON.parse(response);
  if (!("post_list" in response_object)) {
    homeHelper.showMessageBox("No Feeds to Show...");
    return;
  }

  homeHelper.constructAndAppendPostsToDOM(response_object.post_list);
  homeHelper.hideMessageBox();
};

homeCallback.retrieveCommentListCallback = function(response) {
  console.log("Retrieve comment list callback.");

  var response_object = JSON.parse(response);
  homeHelper.constructAndAppendCommentsToDOM(response_object.comment_list);
  homeHelper.hideMessageBox();
};
