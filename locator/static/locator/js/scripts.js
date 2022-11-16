function confirmDeletePost() {
    const forms = document.querySelectorAll("#formDeletePost");

    for (const form of forms) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const confirmed = confirm("Tem certeza que gostaria de deletar este post?");
            if (confirmed) {
                form.submit();
            }
        });
    }
}

function confirmFoundPost() {
    const forms = document.querySelectorAll("#formFoundPost");

    for (const form of forms) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const confirmed = confirm("Realmente encontrou seu animal perdido?");
            if (confirmed) {
                form.submit();
            }
        });
    }
}

confirmDeletePost();
confirmFoundPost();
