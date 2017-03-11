var homeHelper = {};

homeHelper.constructAndAppendOpinionsToDOM = function(opinion_list) {
  var stream_panel_elem = document.getElementById("stream_panel");
  var base_post_elem = document.getElementsByClassName("opinion_post")[0];
  var new_post_elem = null;

  for (var i = 0; i < opinion_list.length; i++) {
    var opinion = opinion_list[i];
    new_post_elem = base_post_elem.cloneNode(true);
    var children = new_post_elem.children;

    for (var j = 0; j < children.length; j++) {
      var child = children[j];
      if (child.className === "post_author") {
        child.innerHTML = "<b> Post By: </b>" + opinion.author;
      } else if (child.className === "post_text") {
        child.innerText = opinion.text;
      } else if (child.className === "post_date") {
        var date = new Date(opinion.timestamp_sec * 1000);
        child.innerHTML = "<b> Posted on: </b>" + date.toLocaleString();
      } else if (child.className === "post_buttons") {
        // Add listener to buttons for new posts.
        var buttons = child.children;
        for (var k = 0; k < buttons.length; k++) {
          var button = buttons[k];
          button.id = opinion.opinion_id;
          if (button.className === "like_button") {

          } else if (button.className === "dislike_button") {

          } else if (button.className === "view_button") {
            button.addEventListener("click", homeCallback.viewButtonCallback);
          }
        } // end for
      }
    } // end for
    new_post_elem.id = opinion.opinion_id;
    new_post_elem.style.display = "block";
    stream_panel_elem.appendChild(new_post_elem);
  } // end for

};

homeHelper.constructAndAppendOpinionViewToDOM = function(opinion_id) {
  var opin_comm_view = document.getElementById("opinion_comment_view");
  var base_post_elem = document.getElementById("opinion_view");
  var opinion_element = document.getElementById(opinion_id);

  var opinion = homeHelper.extractOpinionHTMLInfoFromElement(opinion_element);
  var children = base_post_elem.children;

  base_post_elem.name = opinion_id;
  for (var j = 0; j < children.length; j++) {
    var child = children[j];
    if (child.className === "view_post_author") {
      child.innerHTML = opinion.author;
    } else if (child.className === "view_post_text") {
      child.innerText = opinion.text;
    } else if (child.className === "view_post_date") {
      child.innerHTML = opinion.date;
    } else if (child.className === "view_post_buttons") {
      // Do nothing for now.
    }
  } // end for
  base_post_elem.style.display = "block";
}

homeHelper.constructAndAppendCommentsToDOM = function(commentList) {
  if (commentList == null || commentList.length == 0) {
    return;
  }

  var commentViewContainer = document.getElementById("opinion_comment_view");
  var opinionID = commentList[0].opinion_id;

  var newPostElem = null;
  var basePostElem = document.getElementsByClassName("comment_view")[0];
  for (var i = 0; i < commentList.length; i++) {
    var comment = commentList[i];
    newPostElem = basePostElem.cloneNode(true);
    var children = newPostElem.children;

    newPostElem.id = comment.comment_id;
    for (var j = 0; j < children.length; j++) {
      var child = children[j];
      if (child.className === "view_comment_author") {
        child.innerHTML = "<b> Comment Author: </b>" + comment.author;
      } else if (child.className === "view_comment_text") {
        child.innerText = comment.text;
      } else if (child.className === "view_comment_date") {
        var date = new Date(comment.timestamp_sec * 1000);
        child.innerHTML = "<b> Posted on: </b>" + date.toLocaleString();
      } else if (child.className === "view_comment_buttons") {
        // Add listener to buttons for new posts.
        var buttons = child.children;
        for (var k = 0; k < buttons.length; k++) {
          var button = buttons[k];
          button.id = comment.comment_id;
          if (button.className === "view_like_button") {
          } else if (button.className === "view_dislike_button") {
          }
        } // end for
      }
    } // end for

    newPostElem.id = comment.comment_id;
    newPostElem.className = "live_comment";
    commentViewContainer.insertBefore(newPostElem,
      commentViewContainer.children[commentViewContainer.children.length - 1]);
    newPostElem.style.display = "block";
  } // end for
};

homeHelper.destroyComments = function() {
  var liveComments = document.getElementsByClassName("live_comment");

  if (!liveComments || liveComments.length === 0) {
    return;
  }

  var parent = liveComments[0].parentNode;
  while (liveComments.length > 0) {
    parent.removeChild(liveComments[0]);
  }
};

homeHelper.extractOpinionHTMLInfoFromElement = function(opinion_elem) {
  // author, text, likes, dislikes, timestamp_sec
  var opinion_html = {
    opinion_id: "",
    author: "",
    text: "",
    likes: "",
    dislikes: "",
    date: ""
  };
  var children = opinion_elem.children;

  opinion_html.opinion_id = opinion_elem.id;
  for (var j = 0; j < children.length; j++) {
    child = children[j];
    if (child.className === "post_author") {
      opinion_html.author = child.innerHTML;
    } else if (child.className === "post_text") {
      opinion_html.text = child.innerHTML;
    } else if (child.className === "post_date") {
      opinion_html.date = child.innerHTML;
    } else if (child.className === "post_buttons") {
      // Do nothing for now.
    }
  } // end for

  return opinion_html;
};

homeHelper.showMessageBox = function(message) {
  var messageBox = document.getElementById("message_box");
  var messageBoxText = document.getElementById("message_box_text");
  messageBoxText.innerText = message;
  messageBox.style.display = "block";
};

homeHelper.hideMessageBox = function() {
  var messageBox = document.getElementById("message_box");
  var messageBoxText = document.getElementById("message_box_text");
  messageBoxText.innerText = "";
  messageBox.style.display = "none";
};
