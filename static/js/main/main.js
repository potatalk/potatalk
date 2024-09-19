// hambuger click action
const hamburgerIcon = document.querySelector(".list-icon-box");
const hamburgerModalBox = document.querySelector(".modal-box");
const hamburgerIconAria = document.querySelector(".list-icon");
// banner mouse action
const bannerFlicking = document.querySelector(".banner-flicking");
const bannerImages = document.querySelectorAll(".banner-image");
const imageWidth = bannerImages[0].clientWidth; // 슬라이드 이미지의 너비

let isAnimating = false;
let currentIndex = 1; // 첫 번째 복사본 이후로 시작
let isDragging = false;
let startX = 0;
let currentX = 0;
let initialTranslateX = 0;

// banner arrow click action
const leftArrow = document.querySelector(".left-arrow-box");
const rightArrow = document.querySelector(".right-arrow-box");
const animationDelay = 800;

// banner total count action
const totalSlides = bannerImages.length - 1;
const currentSlideElement = document.getElementById("current-slide");
const bannerLinks = Array.from(bannerImages).map((image) => image.querySelector("a"));

// ------------------------------------------------------------------------

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

// 2. banner count action

// 슬라이드 카운트 업데이터 함수

const updateSlideCount = () => {
    let displayIndex = currentIndex;

    // 무한 슬라이드를 위한 인덱스 조정
    if (currentIndex === 0) {
        displayIndex = bannerImages.length - 2; // 실제 마지막 슬라이드 (복사된 슬라이드 제외)
    } else if (currentIndex === bannerImages.length - 1) {
        displayIndex = 1; // 실제 첫 번째 슬라이드 (복사된 슬라이드 제외)
    }

    // 배열 범위 초과 방지를 위해 displayIndex 확인
    if (displayIndex < 0 || displayIndex >= bannerLinks.length) {
        console.error("Invalid index:", displayIndex);
        return; // 배열 범위 초과 시 함수를 종료하여 오류 방지
    }

    const currentSlide = bannerLinks[displayIndex]; // a 태그 선택

    if (currentSlide) {
        const slideClass = currentSlide.classList[1]; // class에서 'slide-1', 'slide-2' 등 가져오기
        const slideNumber = slideClass.split("-")[1]; // 'slide-1'에서 숫자 '1' 추출

        // 현재 슬라이드 번호 업데이트
        currentSlideElement.textContent = slideNumber;
    } else {
        console.error("Slide not found for index:", displayIndex);
    }
};

// 3. slide banner action

// 슬라이드 위치 업데이트
const updateTransform = (translateX, animate = true) => {
    if (animate) {
        bannerFlicking.style.transition = "transform 0.6s ease"; // 속도 조정 (0.3s -> 0.6s)
    } else {
        bannerFlicking.style.transition = "none";
    }
    bannerFlicking.style.transform = `translateX(${translateX}px)`;

    // 슬라이드가 이동 중일 때 카운트 업데이트를 지연
    updateSlideCount();
};

// 경계를 넘을 때 애니메이션 없이 첫 번째 또는 마지막으로 이동
const checkBoundarySlides = () => {
    if (currentIndex >= bannerImages.length - 1) {
        // 마지막 슬라이드에서 첫 번째로 이동
        setTimeout(() => {
            currentIndex = 1; // 실제 첫 번째 이미지
            updateTransform(-currentIndex * imageWidth, false); // 애니메이션 없이 즉시 이동
        }, 100); // 슬라이드 전환 후 잠시 대기 후 처리
    } else if (currentIndex <= 0) {
        // 첫 번째 슬라이드에서 마지막 슬라이드로 이동
        setTimeout(() => {
            currentIndex = bannerImages.length - 2; // 실제 마지막 이미지
            updateTransform(-currentIndex * imageWidth, false); // 애니메이션 없이 즉시 이동
        }, 100); // 슬라이드 전환 후 잠시 대기 후 처리
    }
};

// 마우스 클릭 시작
bannerFlicking.addEventListener("mousedown", (e) => {
    if (isAnimating) return;
    startX = e.clientX;
    initialTranslateX = -currentIndex * imageWidth;
    isDragging = true;
    updateTransform(initialTranslateX, false); // 애니메이션 없이 시작
});

// 마우스 이동 (드래그 중)
bannerFlicking.addEventListener("mousemove", (e) => {
    if (!isDragging || isAnimating) return;
    currentX = e.clientX;
    const moveX = currentX - startX;
    const translateX = initialTranslateX + moveX;
    updateTransform(translateX, false); // 애니메이션 없이 이동
});

// 마우스 클릭 해제 (드래그 끝)
bannerFlicking.addEventListener("mouseup", () => {
    if (!isDragging) return;
    isDragging = false;
    isAnimating = true;

    const moveX = currentX - startX;

    // 드래그한 거리가 절반 이상이면 슬라이드 이동
    if (moveX > imageWidth / 2) {
        currentIndex--;
    } else if (moveX < -imageWidth / 2) {
        currentIndex++;
    }

    updateTransform(-currentIndex * imageWidth);

    // 슬라이드가 끝나면 경계를 체크
    setTimeout(() => {
        checkBoundarySlides();
        isAnimating = false;
    }, 300); // 애니메이션 시간이 끝난 후 경계 체크
});

// 드래그가 끝나지 않고 영역을 벗어났을 경우 대비
bannerFlicking.addEventListener("mouseleave", () => {
    if (isDragging) {
        bannerFlicking.dispatchEvent(new MouseEvent("mouseup"));
    }
});

// 터치 이벤트 추가 (모바일 대응)
bannerFlicking.addEventListener("touchstart", (e) => {
    startX = e.touches[0].clientX;
    initialTranslateX = -currentIndex * imageWidth;
    isDragging = true;
    updateTransform(initialTranslateX, false);
});

bannerFlicking.addEventListener("touchmove", (e) => {
    if (!isDragging || isAnimating) return;
    currentX = e.touches[0].clientX;
    const moveX = currentX - startX;
    const translateX = initialTranslateX + moveX;
    updateTransform(translateX, false);
});

bannerFlicking.addEventListener("touchend", () => {
    bannerFlicking.dispatchEvent(new MouseEvent("mouseup"));
});

// 브라우저 크기 변경에 대응하는 슬라이드 이동 처리
window.addEventListener("resize", () => {
    const imageWidth = bannerImages[0].clientWidth; // 브라우저 크기 변화에 따라 이미지 크기 재설정
    const translateX = -currentIndex * imageWidth;
    updateTransform(translateX, false); // 크기 변경 후 슬라이드 위치 재조정
});

// 초기 설정: 첫 번째 슬라이드로 이동
updateTransform(-currentIndex * imageWidth, false);

// 4(2). arrow click action

// 연속 버튼 클릭 방지
const disableClickTemporarity = () => {
    isAnimating = true; // 클릭 비활성화
    setTimeout(() => {
        isAnimating = false; // 일정 시간 후 다시 클릭 가능
    }, animationDelay);
};

// 왼쪽 화살표 클릭 시
leftArrow.addEventListener("click", (e) => {
    if (isAnimating) return;
    disableClickTemporarity(); // 클릭 비활성화
    // isAnimating = true;
    currentIndex--;

    updateTransform(-currentIndex * imageWidth); // 왼쪽으로 한 칸 이동

    // 슬라이드가 끝나면 경계를 체크
    setTimeout(() => {
        checkBoundarySlides();
    }, 600); // 애니메이션 시간이 끝난 후 체크
});

// 오른쪽 화살표 클릭 시
rightArrow.addEventListener("click", (e) => {
    if (isAnimating) return;
    disableClickTemporarity(); // 클릭 비활성화
    // isAnimating = true;
    currentIndex++;

    updateTransform(-currentIndex * imageWidth); // 오른쪽으로 한 칸 이동

    // 슬라이드가 끝나면 경계를 체크
    setTimeout(() => {
        checkBoundarySlides();
    }, 600); // 애니메이션 시간이 끝난 후 체크
});
