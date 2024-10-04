// 웹페이지 스크롤 관련 class 정의
const messageWrap = document.querySelector('.top-wrap');
const messageList = document.querySelector('.message-list');
const messageInput = document.querySelector('.bottom-message-input-textarea');
const messageSendButton = document.querySelector('.bottom-message-send-button');
const loading = document.querySelector('.loading');
let lastTimeString = '';

// 시간 포맷팅 함수
const timeFun = () => {
  const today = new Date();
  const options = { hour: '2-digit', minute: '2-digit', hour12: true };
  let timeString = new Intl.DateTimeFormat('ko-KR', options).format(today);
  return timeString.replace('AM', '오전').replace('PM', '오후');
};

// 클라이언트 메시지 HTML 생성 함수
const clientTextFun = (timeString, clientMessageText) => {
  return `
    <div class="middle-message-wrap">
      ${timeString !== lastTimeString ? `
        <div class="middle-message-time">${timeString}</div>
        <div class="middle-message-line"></div>
      ` : `<div class="middle-message-line"></div>`}
      <div class="client-message-container">
        <div class="client-message-box">
          <div class="client-message-section">
            <div class="client-message-all-wrap">
              <div class="client-message-all-container">
                <div class="client-message-left-margin">
                  <button class="client-message-delete-button hidden" type="button">
                    <svg class="client-message-delete-button-img" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24">
                      <path fill="currentColor" fill-rule="evenodd" d="M9.75 4.75A2.257 2.257 0 0 0 12 7a2.257 2.257 0 0 0 2.25-2.25A2.257 2.257 0 0 0 12 2.5a2.257 2.257 0 0 0-2.25 2.25m2.25 9.5A2.257 2.257 0 0 1 9.75 12 2.257 2.257 0 0 1 12 9.75 2.257 2.257 0 0 1 14.25 12 2.257 2.257 0 0 1 12 14.25m0 7.25a2.257 2.257 0 0 1-2.25-2.25A2.257 2.257 0 0 1 12 17a2.257 2.257 0 0 1 2.25 2.25A2.257 2.257 0 0 1 12 21.5" clip-rule="evenodd"></path>
                    </svg>
                  </button>
                </div>
                <div class="client-message-content-wrap">
                  <div class="client-message-content-container">
                    <div class="client-message-content-box">
                      <div id="client-message-text">${clientMessageText}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>`;
};

// 서버 메시지 HTML 생성 함수
const serverTextFun = (timeString, serverMessageText) => {
  return `
    <div class="middle-message-wrap">
      ${timeString !== lastTimeString ? `
        <div class="middle-message-time">${timeString}</div>
        <div class="middle-message-line"></div>
      ` : `<div class="middle-message-line"></div>`}
      <div class="server-message-container">
        <div class="server-message-box">
          <div class="server-message-section">
            <div class="server-message-name-box">
              <div class="server-message-name">potaTalk</div>
            </div>
            <div class="server-message-all-wrap">
              <div class="server-message-all-section">
                <div class="server-message-icon-section">
                  <div class="server-message-icon-wrap">
                    <div class="server-message-icon-box">
                      <img class="server-message-icon-img" width="30" height="30" src="https://cf.channel.io/thumb/200x200/pub-file/28129/63e35c5b4c0474bf7034/tmp-3602965324.webp" alt="">
                    </div>
                  </div>
                </div>
                <div class="server-message-content-wrap">
                  <div class="server-message-content-container">
                    <div class="server-message-text-wrap">
                      <div class="server-message-text-container">
                        <div id="server-message">${serverMessageText}</div>
                      </div>
                    </div>
                  </div>
                  <div class="server-message-right-margin"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>`;
};

// 로딩 함수
const setTimeon = () => {
  loading.classList.remove('hidden');
  messageInput.classList.add('disable');
  messageInput.blur();
  messageWrap.scrollTop = messageWrap.scrollHeight;
};

// 로딩 완료 후 서버 메시지 전송 함수
const setTimeoff = (serverTextString) => {
  setTimeout(() => {
    loading.classList.add('hidden');
    messageInput.classList.remove('disable');
    messageList.innerHTML += serverTextString;
    messageInput.focus();
    messageWrap.scrollTop = messageWrap.scrollHeight;
  }, 2000);
};

// 메세지 전송 함수
var sendMessageFun = async (clientMessageText) => {
    // 입력창 초기화
    messageInput.value = '';

    // 메세지 전송 시간 설정
    let timeString = timeFun();

    // 클라이언트 텍스트 정의
    let clientTextString = clientTextFun(timeString, clientMessageText);

    // 메세지 전송 시간 저장
    lastTimeString = timeString;

    // 클라이언트 메세지 전송
    messageList.innerHTML += clientTextString;

    // 서버로 전송하는 fetch 요청
    try {
        const response = await fetch(messageConnectUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            },
            body: JSON.stringify({
                'wine': clientMessageText,  // 서버에서 요구하는 데이터 형식에 맞게
            })
        });

        const responseText = await response.json();  // 응답을 JSON으로 변환
        console.log('서버 응답 JSON:', responseText);

        // 서버 응답에서 chatbot_response 가져오기
        const serverMessageText = responseText.data;  // 서버 응답에서 필요한 데이터를 가져옵니다.

        // 서버 텍스트 추가 정의
        let serverTextString = serverTextFun(timeString, serverMessageText);

        // 로딩 함수 실행
        setTimeon();
        // 로딩 종료 후 서버 메세지 전송
        setTimeoff(serverTextString);
    } catch (error) {
        console.error('서버 통신 중 오류 발생:', error);
        // 에러 메시지를 사용자에게 표시하는 로직 추가 가능
    }
};

// 화면 첫 로드 시 안내 메세지 시간 작성 함수
var firstMessageFun = () => {
  // 안내 메세지 시간
  const serverFirstMessage = document.querySelector(".server-first-message")

  // 메세지 시작 시간 설정
  let timestring = timeFun();

  // 메세지 전송 시간 저장
  lastTimeString = timestring

  // 메세지 시작 시간 표시
  serverFirstMessage.innerHTML += timestring;

}

// // 화면 첫 로드 시 안내 메세지 시간
firstMessageFun();


//-----------------------------------------------------------------------------------------------------------------
// enter 키로 메시지 입력
messageInput.addEventListener('keyup', (e) => {
  const clientMessageText = messageInput.value.trim();
  if (clientMessageText) {
    messageSendButton.classList.add('send-button-change');
    messageSendButton.classList.remove('disable');
    if (e.keyCode === 13) {
      e.preventDefault();  // 입력창 enter 입력 막기
      sendMessageFun(clientMessageText);  // 메시지 전송
    }
  } else {
    messageSendButton.classList.remove('send-button-change');
    messageSendButton.classList.add('disable');
  }
});

// 버튼 클릭으로 메시지 입력
messageSendButton.addEventListener('click', () => {
  const clientMessageText = messageInput.value.trim();
  if (clientMessageText) {
    messageSendButton.classList.add('send-button-change');
    messageSendButton.classList.remove('disable');
    sendMessageFun(clientMessageText);  // 메시지 전송
  } else {
    messageSendButton.classList.remove('send-button-change');
    messageSendButton.classList.add('disable');
  }
});
