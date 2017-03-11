var homeCallback = {};

homeCallback.postOpinionButtonCallback = function() {
  homeHandler.insertNewOpinion();
  location.reload();
};

homeCallback.postCommentButtonCallback = function() {
  var opinion_id = document.getElementById("opinion_view").name;
  homeHandler.insertNewComment(opinion_id);
};

homeCallback.askQuestionPostCallback = function() {
  var modal_elem = document.getElementById("modal_window");
  var form_elem = document.getElementById("opinion_form");
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
  var view_elem = document.getElementById("opinion_comment_view");
  var opinion_element = event.target.parentNode.parentNode;
  var opinion = homeHelper.extractOpinionHTMLInfoFromElement(opinion_element);

  homeHelper.constructAndAppendOpinionViewToDOM(opinion.opinion_id);

  modal.style.display = "block";
  view_elem.style.display = "block";

  homeHandler.retrieveCommentList(opinion);
};

homeCallback.httpPostAsyncCallback = function(response) {
  console.log("This shouldnt be a thing.");
};

homeCallback.insertNewOpinionCallback = function(response) {
  console.log("Insert new opinion callback.");
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

homeCallback.deleteOpinionCallback = function(response) {
  console.log("Delete opinion callback.");
  console.log(response);
};

homeCallback.retrieveOpinionCallback = function(response) {
  console.log("Retrieve opinion callback.");
  console.log(response);
};

homeCallback.retrieveOpinionListCallback = function(response) {
  console.log("Retrieve opinion list callback.");
  console.log(response);

  var response_object = JSON.parse(response);
  homeHelper.constructAndAppendOpinionsToDOM(response_object.opinion_list);
  homeHelper.hideMessageBox();
};

homeCallback.retrieveCommentListCallback = function(response) {
  console.log("Retrieve comment list callback.");

  var response_object = JSON.parse(response);
  homeHelper.constructAndAppendCommentsToDOM(response_object.comment_list);
  homeHelper.hideMessageBox();
};
