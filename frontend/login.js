function login() {

    const username =
        document.getElementById("username").value.trim();

    const password =
        document.getElementById("password").value.trim();


    if (
        username === "Dheepikha seenuvasan" &&
        password === "12345"
    ) {

        // Save login status
        localStorage.setItem("loggedIn", "true");

        // Save username
        localStorage.setItem("username", username);

        // Go to dashboard
        window.location.href = "index.html";

    } else {

        document.getElementById("errorMessage").innerHTML =
            "❌ Invalid Username or Password.";

    }

}