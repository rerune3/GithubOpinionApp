httpGetCallback = function(responseText) {
  var response = JSON.parse(responseText);
  var opinions = response.opinions;

  if (opinions == null)
    return;

  var divElement = document.getElementById("opinion_feed");

  var text = "";
  for (var i = 0; i < opinions.length; i++) {
    text += "<p> " + opinionToString(opinions[i]) + " </p>";
  }

  divElement.innerHTML = text;
}

httpPostCallback = function(responseText) {
  console.log(responseText);
}
