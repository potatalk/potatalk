const songMessageService = (() => {
    // 클라이언트가 서버로 메시지를 전송하는 함수
    const clientSend = async (clientMessageText, callback) => {
        // 서버로 POST 요청을 보내고 응답을 기다림
        const response = await fetch(`/songLLM/song-chatbot/send/`, {
            // POST 방식으로 데이터를 전송
            method: 'POST',
            headers: {
                // 요청 본문이 JSON 형식임을 명시
                'Content-Type': 'application/json;charset=utf-8',
                // CSRF 보안을 위한 토큰 전달
                'X-CSRFToken': csrf_token
            },
            // 서버로 보낼 메시지를 JSON 형식으로 변환하여 요청 본문에 포함
            body: JSON.stringify({
                'clientMessageText': clientMessageText,
            })
        })

        // 서버로부터 받은 응답을 JSON으로 파싱 (서버가 보낸 메시지)
        const serverMessage = await response.json();

        // 콜백 함수가 존재하면 서버 응답을 콜백 함수로 전달하여 후속 작업 처리
        if (callback) {
            return callback(serverMessage);
        }

        return serverMessage
    }

    // 외부에서 clientSend 함수를 호출할 수 있도록 반환
    return {clientSend:clientSend}
})();