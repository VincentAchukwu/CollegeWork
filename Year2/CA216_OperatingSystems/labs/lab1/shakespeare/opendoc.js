// Open a new window for a document -- sized appropriately
function openDOC(url) {
  var ua = navigator.userAgent;
  // open a new window ...
  doc = window.open("","doc");
  // ... and fill it with the requested page
  doc.location.href = url
  doc.focus();
  return false
}

