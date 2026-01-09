function validateForm() {
    const name = document.querySelector('input[name="name"]').value.trim();
    const email = document.querySelector('input[name="email"]').value.trim();
    const rating = document.querySelector('select[name="rating"]').value;

    if (!name || !email || !rating) {
        alert("Please fill all required fields.");
        return false;
    }
    return true;
}
