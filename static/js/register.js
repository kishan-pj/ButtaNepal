var state = false;
function showPassword() {
    if (state) {
        document.getElementById("password-field").setAttribute("type", "password");
        document.getElementById("eyeopen").setAttribute("src", "/static/image/eye-closed.svg");
        state = false;
    } else {
        document.getElementById("password-field").setAttribute("type", "text");
        document.getElementById("eyeopen").setAttribute("src", "/static/image/eye.svg");
        state = true;
    }
}
