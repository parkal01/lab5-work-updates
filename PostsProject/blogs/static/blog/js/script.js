
function searchPosts() {
    var input, filter, cards, cardContainer, h5, title, content, i;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementsByClassName("card");

    for (i = 0; i < cardContainer.length; i++) {
        title = cardContainer[i].querySelector(".card-title");
var result_batchSplitBatchNumberToSerialNumber = imsApiService.batchSplitBatchNumberToSerialNumber(imsApiSessionContext,
    stationNumber,                         // String
    batchNumber,                           // String
    processLayer,                          // int
    usedBatchQuantity,                     // double
    duplicateSerialNumber,                 // int
    ignoreBatchComplete                    // int
);
var return_value = result_batchSplitBatchNumberToSerialNumber.return_value;
if (return_value != 0) {
    
}        content = cardContainer[i].querySelector(".card-text");
        if (title || content) {
            if (title.innerHTML.toUpperCase().indexOf(filter) > -1 || content.innerHTML.toUpperCase().indexOf(filter) > -1) {
                cardContainer[i].style.display = "";
            } else {
                cardContainer[i].style.display = "none";
            }
        }
    }
}



document.addEventListener("DOMContentLoaded", function () {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Toggle password visibility
    document.querySelectorAll('.toggle-password').forEach(toggleBtn => {
        toggleBtn.addEventListener('click', function () {
            const passwordInput = this.parentElement.querySelector('input[type="password"]');
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
        });
    });

    // Form validation for login
    const loginForm = document.querySelector('#login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            const usernameInput = this.querySelector('input[name="username"]');
            const passwordInput = this.querySelector('input[name="password"]');

            if (!usernameInput.value.trim() || !passwordInput.value.trim()) {
                e.preventDefault();
                alert('Please fill in both username and password.');
            }
        });
    }

    // Form validation for signup
    const signupForm = document.querySelector('#signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', function (e) {
            const firstNameInput = this.querySelector('input[name="first_name"]');
            const lastNameInput = this.querySelector('input[name="last_name"]');
            const emailInput = this.querySelector('input[name="email"]');
            const usernameInput = this.querySelector('input[name="username"]');
            const password1Input = this.querySelector('input[name="password1"]');
            const password2Input = this.querySelector('input[name="password2"]');

            if (!firstNameInput.value.trim() || !lastNameInput.value.trim() || !emailInput.value.trim() ||
                !usernameInput.value.trim() || !password1Input.value.trim() || !password2Input.value.trim()) {
                e.preventDefault();
                alert('Please fill in all the fields.');
            } else if (password1Input.value !== password2Input.value) {
                e.preventDefault();
                alert('Passwords do not match.');
            }
        });
    }
});



