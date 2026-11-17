const profileForm = document.getElementById("profileForm");

if (profileForm) {
  profileForm.addEventListener("submit", (event) => {
    const name = document.getElementById("name").value.trim();
    if (!name) {
      event.preventDefault();
      alert("Please enter your name.");
    }
  });
}
