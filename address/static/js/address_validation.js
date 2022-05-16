function validate() {
  let uname = document.getElementById("uname");
  let phone = document.getElementById("phone");
  let email = document.getElementById("email");
  let address = document.getElementById("address");
  let place = document.getElementById("place");
  let email_pattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
  let phone_pattern = /^[6-9]\d{9}$/;

  // Name
  if (uname.value == "") {
    document.getElementById("name_err").innerHTML = "*Please fill this field";
    document.getElementById("name_err").style.color = "red";
    uname.style.borderColor = "red";
    return false;
  } else {
    document.getElementById("name_err").innerHTML = "";
    document.getElementById("uname").style.borderColor = "";
  }

  // Phone
  if (phone.value == "") {
    document.getElementById("phone_err").innerHTML = "*Please fill this field";
    document.getElementById("phone_err").style.color = "red";
    phone.style.borderColor = "red";
    return false;
  } else {
    document.getElementById("phone_err").innerHTML = "";
    document.getElementById("phone").style.borderColor = "";
  }

  // Phone pattern
  if (phone.value.match(phone_pattern)) {
    document.getElementById("phone_err").innerHTML = "";
    document.getElementById("phone").style.borderColor = "";
  } else {
    document.getElementById("phone_err").innerHTML =
      "*Enter a valid phone number";
    document.getElementById("phone_err").style.color = "red";
    document.getElementById("phone").style.borderColor = "red";
    return false;
  }

  // Email
  if (email.value == "") {
    document.getElementById("email_err").innerHTML = "*Please fill this field";
    document.getElementById("email_err").style.color = "red";
    email.style.borderColor = "red";
    return false;
  } else {
    document.getElementById("email_err").innerHTML = "";
    document.getElementById("email").style.borderColor = "";
  }

  // Email pattern
  if (email.value.match(email_pattern)) {
    document.getElementById("email_err").innerHTML = "";
    document.getElementById("email").style.borderColor = "";
  } else {
    document.getElementById("email_err").innerHTML = "*Enter a valid email";
    document.getElementById("email_err").style.color = "red";
    document.getElementById("email").style.borderColor = "red";
    return false;
  }

  // Place
  if (place.value == "") {
    document.getElementById("place_err").innerHTML = "*Please fill this field";
    document.getElementById("place_err").style.color = "red";
    place.style.borderColor = "red";
    return false;
  } else {
    document.getElementById("place_err").innerHTML = "";
    document.getElementById("place").style.borderColor = "";
  }

  // Address
  if (address.value == "") {
    document.getElementById("address_err").innerHTML =
      "*Please fill this field";
    document.getElementById("address_err").style.color = "red";
    address.style.borderColor = "red";
    return false;
  } else {
    document.getElementById("address_err").innerHTML = "";
    document.getElementById("address").style.borderColor = "";
  }
}
