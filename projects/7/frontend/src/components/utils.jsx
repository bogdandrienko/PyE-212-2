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

export function ActionWithRedux(
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
