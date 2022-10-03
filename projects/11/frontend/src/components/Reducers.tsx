import * as constants from "./Constants";

// Reducer - "переключатель состояний хранилища(глобальное хранилище данных (состояний) - redux)"
export function CounterReducer (state = {}, action: { type: string; payload: any }) {
    switch (
      action.type // switch ("LOAD")
    ) {
      case "LOAD": {
        return { load: true, data: undefined, error: undefined };
      }
      case constants.SUCCESS: {
        return { load: false, data: action.payload, error: undefined }; // action.payload = await axios.get('/token').data
      }
      case "ERROR": {
        return { load: false, data: undefined, error: "Произошла ошибка" }; // error: true
      }
      // ...
      // case "RESET"
      // case "ANOTHER_ERROR"
      // case "CUSTOM"
      // ...
      default: {
        return state; // стандарт !!
      }
    }
  }
  
  export function TokenReducer (state = {}, action: { type: string; payload: any }) {
      switch (
        action.type // switch ("LOAD")
      ) {
        case constants.LOAD_TOKEN: {
          return { load: true, data: undefined, error: undefined };
        }
        case constants.SUCCESS_TOKEN: {
          return { load: false, data: action.payload, error: undefined }; // action.payload = await axios.get('/token').data
        }
        case constants.ERROR_TOKEN: {
          return { load: false, data: undefined, error: "Произошла ошибка" }; // error: true
        }
        // ...
        // case "RESET"
        // case "ANOTHER_ERROR"
        // case "CUSTOM"
        // ...
        default: {
          return state; // стандарт !!
        }
      }
    }