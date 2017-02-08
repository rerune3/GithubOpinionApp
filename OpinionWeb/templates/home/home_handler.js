var homeHandler = {};

homeHandler.insertNewOpinion = function() {
  var opinion_input_elem = document.getElementById("opinion_input");
  var tags_input_wrapper_elem = document.getElementById("tags_input_wrapper");

  var author = "SomeUser";

  if (opinion_input_elem.value === "")
    return;

  var opinionObj = {
    author: author,
    text: opinion_input_elem.value + "",
    opinion_id: Date(),
    timestamp_sec: parseInt(Date.now() / 1000, 10)
  };

  var data = JSON.stringify(opinionObj);
  var request_type = JSON.stringify(define.request_types.INSERT_NEW_OPINION);

  var request_package = {
    'request_type': request_type,
    'opinion': data
  };

  var params = helper.constructURLParams(request_package);
  var url = window.location.origin + '/home?' + params;

  helper.httpPostAsync(url, homeCallback.insertNewOpinionCallback, null);

  opinion_input_elem.value = "";
}

homeHandler.insertNewComment = function() {

}

homeHandler.deleteOpinion = function() {

}

homeHandler.deleteComment = function() {

}

homeHandler.retrieveOpinion = function() {

}

homeHandler.retrieveOpinionList = function() {
  var opinionListRequest = {
    size: 50,
    tags: [],
  };

  var data = JSON.stringify(opinionListRequest);
  var request_type = JSON.stringify(define.request_types.RETRIEVE_OPINION_LIST);

  var request_package = {
    'request_type': request_type,
    'opinion_list_request': data
  };

  var params = helper.constructURLParams(request_package);
  var url = window.location.origin + '/home?' + params;

  helper.httpPostAsync(url, homeCallback.retrieveOpinionListCallback, null);
}
