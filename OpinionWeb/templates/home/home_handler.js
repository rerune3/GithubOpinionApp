var homeHandler = {};

homeHandler.insertNewOpinion = function() {
  var opinionInputElement = document.getElementById("opinion_input");
  var tagsInputWrapperElement = document.getElementById("tags_input_wrapper");

  var author = "SomeUser";

  if (opinionInputElement.value === "")
    return;

  var opinionObj = {
    author: author,
    text: opinionInputElement.value + "",
    opinion_id: "",
    timestamp_sec: parseInt(Date.now() / 1000, 10)
  };

  var data = JSON.stringify(opinionObj);
  var requestType = JSON.stringify(define.request_types.INSERT_NEW_OPINION);

  var requestPackage = {
    'request_type': requestType,
    'opinion': data
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/home?' + params;

  helper.httpPostAsync(url, homeCallback.insertNewOpinionCallback, null);

  opinionInputElement.value = "";
};

homeHandler.insertNewComment = function(opinionID) {
  var commentInputElement = document.getElementById("comment_input");
  var author = "SomeCommenter";

  if (commentInputElement.value === "")
    return;

  var commentObj = {
    author: author,
    text: commentInputElement.value + "",
    comment_id: "",
    opinion_id: opinionID,
    timestamp_sec: parseInt(Date.now() / 1000, 10)
  };

  var data = JSON.stringify(commentObj);
  var requestType = JSON.stringify(define.request_types.INSERT_NEW_COMMENT);

  var requestPackage = {
    "request_type": requestType,
    "comment": data
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + "/home?" + params;

  helper.httpPostAsync(url, homeCallback.insertNewCommentCallback, null);

  commentInputElement.value = "";
};

homeHandler.deleteOpinion = function() {

};

homeHandler.deleteComment = function() {

};

homeHandler.retrieveOpinion = function() {

};

homeHandler.retrieveOpinionList = function() {
  var opinionListRequest = {
    size: 50,
    tags: [],
  };

  var data = JSON.stringify(opinionListRequest);
  var requestType = JSON.stringify(define.request_types.RETRIEVE_OPINION_LIST);

  var requestPackage = {
    'request_type': requestType,
    'opinion_list_request': data
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/home?' + params;

  homeHelper.showMessageBox("Loading Feed...");
  helper.httpGetAsync(url, homeCallback.retrieveOpinionListCallback, null);
};

homeHandler.retrieveCommentList = function(opinion) {
  var commentListRequest = {
    opinion_id: opinion.opinion_id,
    size: 50
  };

  var data = JSON.stringify(commentListRequest);
  var request_type = JSON.stringify(define.request_types.RETRIEVE_COMMENT_LIST);

  var request_package = {
    "request_type": request_type,
    "comment_list_request": data
  };

  var params = helper.constructURLParams(request_package);
  var url = window.location.origin + '/home?' + params;

  homeHelper.showMessageBox("Loading Comments...");
  helper.httpGetAsync(url, homeCallback.retrieveCommentListCallback, null);
};
