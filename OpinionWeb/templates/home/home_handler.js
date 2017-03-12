var homeHandler = {};

homeHandler.insertNewPost = function() {
  var postInputElement = document.getElementById("post_input");
  var tagsInputWrapperElement = document.getElementById("tags_input_wrapper");

  var author = "SomeUser";

  if (postInputElement.value === "")
    return;

  var postObj = {
    author: author,
    text: postInputElement.value + "",
    post_id: "",
    timestamp_sec: parseInt(Date.now() / 1000, 10)
  };

  var data = JSON.stringify(postObj);
  var requestType = JSON.stringify(define.request_types.INSERT_NEW_POST);

  var requestPackage = {
    'request_type': requestType,
    'post': data
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/home?' + params;

  helper.httpPostAsync(url, homeCallback.insertNewPostCallback, null);

  postInputElement.value = "";
};

homeHandler.insertNewComment = function(postID) {
  var commentInputElement = document.getElementById("comment_input");
  var author = "SomeCommenter";

  if (commentInputElement.value === "")
    return;

  var commentObj = {
    author: author,
    text: commentInputElement.value + "",
    comment_id: "",
    post_id: postID,
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

homeHandler.deletePost = function() {

};

homeHandler.deleteComment = function() {

};

homeHandler.retrievePost = function() {

};

homeHandler.retrievePostList = function() {
  var postListRequest = {
    size: 50,
    tags: [],
  };

  var data = JSON.stringify(postListRequest);
  var requestType = JSON.stringify(define.request_types.RETRIEVE_POST_LIST);

  var requestPackage = {
    'request_type': requestType,
    'post_list_request': data
  };

  var params = helper.constructURLParams(requestPackage);
  var url = window.location.origin + '/home?' + params;

  homeHelper.showMessageBox("Loading Feed...");
  helper.httpGetAsync(url, homeCallback.retrievePostListCallback, null);
};

homeHandler.retrieveCommentList = function(post) {
  var commentListRequest = {
    post_id: post.post_id,
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
