function togglePasswordVisibility(button) {
  var passwordField = button.parentNode.querySelector('input[type="password"]');
  
  if (passwordField.getAttribute('type') === 'password') {
    passwordField.setAttribute('type', 'text');
    button.textContent = 'Ocultar';
  } else {
    passwordField.setAttribute('type', 'password');
    button.textContent = 'Mostrar';
  }
}
