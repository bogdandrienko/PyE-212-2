import axios from "axios";
import * as actions from "../components/Actions";


export function GetStaticFile(file) {
  return `/static${file}`;
}

export function CreateArrayFromInt(count = 1, limit = 10, view=10) {
  const pages_count = count/ limit;
  let pages = [];
  for (let i = 1; i <= pages_count; i += 1) {
    pages.push(i);
  }

  return pages.slice(0, view);
}

export async function ActionClearReact(
  url,
  method = "GET",
  data = {},
  timeout = 3000
) {
  const formData = new FormData();
  Object.keys(data).forEach(function (key) {
    formData.append(key.toString(), data[key]);
  });
  const config = {
    url: url,
    method: method,
    data: formData,
    timeout: timeout,
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  };
  const response = await axios(config);
  return response;
}

export function ActionRedux(
  url,
  method = "GET",
  data = {},
  timeout = 3000
) {
  return async function (dispatch) {

    try{


    // dispatch({ type: CONST_TOP_BOOKS_LOAD }); // ЗАГРУЗКА

    const formData = new FormData();
    Object.keys(data).forEach(function (key) {
      formData.append(key.toString(), data[key]);
    });


    const config = {
      url: url,
      method: method,
      data: formData,
      timeout: timeout,
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    };
    const response = await axios(config);

    // dispatch({type: CONST_TOP_BOOKS_DATA, payload: response.data}) // ДАННЫЕ ПРИШЛИ
    
  } catch(error){
    // dispatch({type: CONST_TOP_BOOKS_FAIL}) // Ошибка на клиенте
  }
  };
}

// export function ActionConstructor

export function ConstructorCR(name="string") {
  /* Конструктор для уникальных переменных в react-redux */
  return {
    load: `load ${name}`, // "load Constant_TopBooks"
    data: `data ${name}`, // "data Constant_TopBooks"
    error: `error ${name}`,
    fail: `fail ${name}`,
    reset: `reset ${name}`,
  }
}

export function ConstructorRR(
  constant = {
    load: undefined,
    data: undefined,
    error: undefined,
    fail: undefined,
    reset: undefined,
  }
) {
  return function (state = {}, action = null) {
    switch (action.type) {
      case constant.load:
        return {
          load: true
        };
      case constant.data:
        return {
          load: false,
          data: action.payload,
        };
      case constant.error:
        return {
          load: false,
          error: "Ошибка на сервере",
        };
      case constant.fail:
        return {
          load: false,
          fail: "Ошибка на клиенте",
        };
      case constant.reset:
        return {
          load: false,
        };
      default:
        return state;
    }
  };
}

export function ConstructorActionRedux(
  url=`/`,
  method="GET",
  data={},
  timeout=3000,
  constant = {
    load: undefined,
    data: undefined,
    error: undefined,
    fail: undefined,
    reset: undefined,
  }
){
return async function (dispatch, getState) {
  try {
    dispatch({ type: constant.load });  // ВКЛЮЧАЕМ СОСТЯНИЕ ЗАГРУЗКИ ДЛЯ ЭТОГО topBooks

    // const {
    //   token: {data: token}
    // } = getState();

    const token = localStorage.getItem("token")

    const formData = new FormData();
    Object.keys(data).forEach(function (key) {
      formData.append(key.toString(), data[key]);
    });
    const config = {
      url: url,
      method: method,
      data: formData,
      timeout: timeout,
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
    const response = await axios(config);

    // console.log("response", response)
    // console.log("status", response.status)

    if (response.status === 200) {
      dispatch({ type: constant.data, payload: response.data });
    } else {
      dispatch({ type: constant.error });
    }
  } catch (error) {
    switch (error.response.status) {
      case 401:
        // UNAUTHORIZED
        actions.Logout();
        break;
      case 402:
        //
        break;
      case 403:
        //
        break;
      case 404:
        // NOT FOUND
        dispatch({ type: constant.reset });
        break;
      default:
        dispatch({ type: constant.fail });
        break;
    }
  }
}

}

export function Sleep(func, timeDelay=3000){
  setTimeout(()=> {
    func()
  }, timeDelay)

  // setInterval
}
