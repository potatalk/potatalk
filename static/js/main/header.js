// hambuger click action
const hamburgerIcon = document.querySelector(".list-icon-box");
const hamburgerModalBox = document.querySelector(".modal-box");
const hamburgerIconAria = document.querySelector(".list-icon");

// 1. hambuger click action
function toggleModal(e) {
    if (hamburgerIcon.contains(e.target)) {
        if (hamburgerModalBox.style.display == "block") {
            hamburgerModalBox.style.display = "none";
            hamburgerIconAria.setAttribute("aria-expanded", "false"); // aria-expanded를 false로 설정
        } else {
            hamburgerModalBox.style.display = "block";
            hamburgerIconAria.setAttribute("aria-expanded", "true"); // aria-expanded를 true로 설정
        }
    } else if (!hamburgerModalBox.contains(e.target)) {
        hamburgerModalBox.style.display = "none";
        hamburgerIconAria.setAttribute("aria-expanded", "false"); // aria-expanded를 false로 설정
    }
}

document.addEventListener("click", toggleModal);