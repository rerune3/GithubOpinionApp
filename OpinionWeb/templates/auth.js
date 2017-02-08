onSignInWithGoogle = function(loginInfo) {
  var path = window.location;
  httpPostAsync(path, function() {},
    JSON.stringify(loginInfo.getBasicProfile()));
  window.location.pathname = "home";
}
