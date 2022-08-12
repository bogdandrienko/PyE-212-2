import axios from "axios";

export function GetStaticFile(file) {
  return `/static${file}`;
}

export function CreateArrayFromInt(count = 1, limit = 10) {
  const pages_count = limit / count;
  console.log("pages_count", pages_count);

  let pages = [];
  for (let i = 1; i <= pages_count; i += 1) {
    pages.push(i);
  }
  return pages;
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

export function ConstructorConstantRedux(name="string") {
  /* Конструктор для уникальных переменных в react-redux */
  return {
    load: `load ${name}`, // "load Constant_TopBooks"
    data: `data ${name}`, // "data Constant_TopBooks"
    error: `error ${name}`,
    fail: `fail ${name}`,
    reset: `reset ${name}`,
  }
}

export function ConstructorReducerRedux(
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
    if (response.status === 200) {
      dispatch({ type: constant.data, payload: response.data });
    } else {

      // в случае неудачной аутентификации 
      // (авторизации) нужно перекидывать пользователя на страницу входа

      dispatch({ type: constant.error });
    }
  } catch (error) {
    dispatch({ type: constant.fail });
  }
}

}