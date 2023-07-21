var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  var x = document.getElementsByClassName("step");
  x[n].style.display = "block";

  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }

  if (n == (x.length - 1)) {
    // Hide next button and show submit button
    document.getElementById("nextBtn").style.display = "none";
    document.getElementById("submitBtn").style.display = "inline";
  } else {
    // Show next button and hide submit button
    document.getElementById("nextBtn").style.display = "inline";
    document.getElementById("submitBtn").style.display = "none";
  }

  fixStepIndicator(currentTab);
}

function nextPrev(n) {
  var x = document.getElementsByClassName("step");

  if (n == 1 && !validateForm()) return false;

  x[currentTab].style.display = "none";

  currentTab = currentTab + n;

  if (currentTab >= x.length) {
    document.getElementById("signUpForm").submit();
    return false;
  }

  showTab(currentTab);
}

function validateForm() {
  var x, y, i, valid = true;
  x = document.getElementsByClassName("step");
  y = x[currentTab].getElementsByTagName("input");

  return valid;
}

function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("stepIndicator");

  for (i = 0; i < x.length; i++) {
    if (i <= n) {
      x[i].classList.add("active");
    } else {
      x[i].classList.remove("active");
    }
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

function handle3CChange() {
  var citizenResultSelect = document.getElementById('id_citizen_1');
  var otherCountryField = document.getElementById('id_other_country_1');
  var ethnicityField = document.getElementById('id_ethnicity_1');

  if (citizenResultSelect.value === 'Yes') {
    otherCountryField.removeAttribute('readonly');
    ethnicityField.setAttribute('readonly', 'readonly');
  } else if (citizenResultSelect.value === 'No') {
    ethnicityField.removeAttribute('readonly');
    otherCountryField.setAttribute('readonly', 'readonly');
  } else {
    otherCountryField.setAttribute('readonly', 'readonly');
    ethnicityField.setAttribute('readonly', 'readonly');
  }
}

function handle3EChange() {
  var childrenBorned = document.getElementById('id_children_borned_1');
  var childrenStillLiving = document.getElementById('id_children_still_living_1');
  var childrenALive = document.getElementById('id_children_alive_specificdate_1');
  
  console.log(childrenBorned.value);
  if (childrenBorned.value === '00') {
    childrenStillLiving.removeAttribute('readonly');
    childrenALive.removeAttribute('readonly');
    
  } else {
    childrenStillLiving.setAttribute('readonly', 'readonly');
    childrenALive.setAttribute('readonly', 'readonly');
    
  }
}

function handle3FChange() {
  var buildingType = document.getElementById('id_type_of_building_7');
  var buildingTypeSpecify = document.getElementById('id_type_of_building_specify');
  var acquisitionHouse = document.getElementById('id_acquisition_of_housing_5');
  var acquisitionHouseSpecify = document.getElementById('id_acquisition_of_housing_specify');
  
  if (buildingType.checked) {
    buildingTypeSpecify.removeAttribute('readonly');
  } else {
    buildingTypeSpecify.setAttribute('readonly', 'readonly');
  }

  if (acquisitionHouse.checked) {
    acquisitionHouseSpecify.removeAttribute('readonly');
  } else {
    acquisitionHouseSpecify.setAttribute('readonly', 'readonly');
  }


}