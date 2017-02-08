var homeCallback = {}

homeCallback.postButtonCallback = function() {
  homeHandler.insertNewOpinion();
  location.reload();
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
  } // end if
};

homeCallback.viewButtonCallback = function(event) {
  var modal = document.getElementById("modal_window");
  var view_elem = document.getElementById("opinion_comment_view");
  modal.style.display = "block";
  view_elem.style.display = "block";
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
  var stream_panel_elem = document.getElementById("stream_panel");
  var base_post_elem = document.getElementsByClassName("opinion_post")[0];
  var new_post_elem = null;
  var response_object = JSON.parse(response);

  for (var i = 0; i < response_object.opinion_list.length; i++) {
    opinion = response_object.opinion_list[i];
    new_post_elem = base_post_elem.cloneNode(true);
    children = new_post_elem.children;

    for (var j = 0; j < children.length; j++) {
      child = children[j];
      if (child.className === "post_author") {
        child.innerHTML = "<b> Posted By: </b>" + opinion.author;
      } else if (child.className === "post_text") {
        child.innerText = opinion.text;
      } else if (child.className === "post_date") {
        date = new Date(opinion.timestamp_sec * 1000);
        child.innerHTML = "<b> Posted on: </b>" + date.toLocaleString();
      }
    }

    new_post_elem.id = opinion.opinion_id;
    new_post_elem.style.display = "";
    stream_panel_elem.appendChild(new_post_elem);
  } // end for
};
