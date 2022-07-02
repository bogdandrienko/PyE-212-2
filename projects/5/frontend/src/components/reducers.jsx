

async function LoginReducer(){
    return function(state={}, action=null){
        switch (action.type) {
            case "LOGIN_LOAD_CONSTANT":
                return {load: true};
            case "LOGIN_DATA_CONSTANT":
                return {load: false, data: action.payload};
            case "LOGIN_ERROR_CONSTANT":
                return {load: "ошибка на сервере"};
            case "LOGIN_FAIL_CONSTANT":
                return {fail: "ошибка на клиенте"};
            default:
                return state;
        }
    };
}

export default LoginReducer;