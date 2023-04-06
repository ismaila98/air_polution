function navigate() {
  var selectedValue = document.getElementById("heatmap-selector").value;
  if (selectedValue) {
    window.location.href = selectedValue;
  }
}
