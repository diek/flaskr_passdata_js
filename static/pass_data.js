// a function to take in the list of data, created in app.py
// add option items to the dom using the values.
function displayData(in_data) {
  var selectWings = document.getElementById('chickenWings')
  var fragment = document.createDocumentFragment()
  for (i = 0; i < in_data.length; i++){
    var option = document.createElement("option");
    option.text = in_data[i];
    fragment.appendChild(option);
  }
  selectWings.appendChild(fragment);
}


