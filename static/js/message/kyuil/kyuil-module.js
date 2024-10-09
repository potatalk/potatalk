const chatService = (() => {
    const write = async (input) => {
        const response = await fetch("/kyuilLLM/kyuil/input/", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'X-CSRFToken': csrf_token
            },
            body: JSON.stringify(input)
        });
    }

    const getList = async (callback) => {
        const response = await fetch(`/kyuilLLM/kyuil/output/`);
        const replies = await response.json();
        if(callback){
            return callback(replies);
        }
        return replies;
    }

    return {write: write, getList: getList}
})();
















