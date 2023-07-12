var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  var x = document.getElementsByClassName("step");
  
  // Display the specified tab of the form
  x[n].style.display = "block";
  
  // Fix the Previous/Next buttons
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  
  // Run a function that will display the correct step indicator
  fixStepIndicator(n);
  
  // Update the Next button based on the current tab
  updateNextButton(n);
}

function nextPrev(n) {
  var x = document.getElementsByClassName("step");
  
  // Exit the function if any field in the current tab is invalid
  if (n == 1 && !validateForm()) return false;
  
  // Hide the current tab
  x[currentTab].style.display = "none";
  
  // Increase or decrease the current tab by 1
  currentTab = currentTab + n;
  
  // If you have reached the end of the form
  if (currentTab >= x.length) {
    // Replace the Next button with a Submit button
    document.getElementById("nextBtn").style.display = "none";
    document.getElementById("submitBtn").style.display = "inline";
    return false;
  }
  
  // Otherwise, display the correct tab
  showTab(currentTab);
}

function validateForm() {
  var x, y, i, valid = true;
  x = document.getElementsByClassName("step");
  y = x[currentTab].getElementsByClassName("needVal");
  
  // A loop that checks every input field in the current tab
  for (i = 0; i < y.length; i++) {
    // If a field is empty
    if (y[i].value == "") {
      // Add an "invalid" class to the field
      y[i].className += " invalid";
      // Set the current valid status to false
      valid = false;
    }
  }
  
  // If the valid status is true, mark the step as finished and valid
  if (valid) {
    document.getElementsByClassName("stepIndicator")[currentTab].className += " finish";
  }
  
  return valid; // Return the valid status
}

function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("stepIndicator");
  
  // This function removes the "active" class of all steps
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  
  // Add the "active" class on the current step
  x[n].className += " active";
}

function updateNextButton(n) {
  var nextBtn = document.getElementById("nextBtn");
  
  // Update the Next button based on the current tab
  if (n == (x.length - 1)) {
    nextBtn.innerHTML = "Submit";
  } else {
    nextBtn.innerHTML = "Next";
  }
}

function handleResultChange() {
  var resultSelect = document.getElementById('id_result_1');
  var descriptionField = document.getElementById('id_result_description_1');
  
  if (resultSelect.value === '5') {
      descriptionField.removeAttribute('readonly');
  } else {
      descriptionField.setAttribute('readonly', 'readonly');
  }
}