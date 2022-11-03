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

confirmDeletePost();
