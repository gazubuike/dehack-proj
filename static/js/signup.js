const modal = document.querySelector(".signup");
const overlay = document.querySelector(".overlay");
const btnClose = document.querySelector(".closesignup");
const btnClose2 = document.querySelector(".closesignup2");
const btnOpenModal = document.querySelectorAll(".signupbtn");

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

for (let i = 0; i < btnOpenModal.length; i++)
  btnOpenModal[i].addEventListener("click", openModal);

btnClose.addEventListener("click", closeModal);
btnClose2.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});