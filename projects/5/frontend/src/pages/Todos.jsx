import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";

// todos:
// первичные данные: [] DEFAULT | STATE | INITIAL
// при запуске загрузки: load: True LOAD
// при неудачном старте загрузки: fail: "Fail message" FAIL
// при удачном окончании загрузки: load: False, data: [...] DATA
// при неудачном окончании загрузки: error: "Error message" ERROR
// при сбросе данных: [] RESET

export const TODOS_LOAD = "TODOS_LOAD_CONSTANT";
export const TODOS_DATA = "TODOS_DATA_CONSTANT";
export const TODOS_ERROR = "TODOS_ERROR_CONSTANT";
export const TODOS_FAIL = "TODOS_FAIL_CONSTANT";
export const TODOS_RESET = "TODOS_RESET_CONSTANT";

export function GetTodosReducer(state = {}, action = null) {
  switch (action.type) {
    case TODOS_LOAD:
      return { load: true, data: undefined, error: undefined };
    case TODOS_DATA:
      return { load: false, data: action.payload, error: undefined };
    case TODOS_ERROR:
      return { load: undefined, error: "ошибка на сервере" };
    case TODOS_FAIL:
      return { load: undefined, fail: "ошибка на клиенте" };
    case TODOS_RESET:
      return { load: undefined, data: undefined, error: undefined};
    default:
      return state;
  }
}

export const GetTodosAction = () => async (dispatch, getState) => {
  try {
    dispatch({ type: TODOS_LOAD });

    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/todo/`,
      data: null,
    };
    const response = await axios(config);
    const { data } = response;

    if (data) {
      dispatch({ type: TODOS_DATA, payload: data });
    } else {
      dispatch({ type: TODOS_ERROR });
    }
  } catch (error) {
    console.log(error);
    dispatch({
      type: TODOS_FAIL,
      payload: error,
    });
  }
};

export function Todos() {
  const dispatch = useDispatch();
  const GetTodosStore = useSelector((state) => state.GetTodosStore);
  const {
    load: load,
    data: data,
    error: error,
    fail: fail,
    reset: reset,
  } = GetTodosStore;

  useEffect(() => {
    console.log(`GetTodosStore: ${GetTodosStore}`);
    console.log(`load: ${load}`);
    console.log(`data: ${data}`);
    console.log(`error: ${error}`);
    console.log(`fail: ${fail}`);
    console.log(`reset: ${reset}`);
  }, [GetTodosStore]);

  function getData() {
    dispatch(GetTodosAction());
  }

  function resetData() {
    dispatch({ type: TODOS_RESET });
  }
  return (
    <div>
      <h1>Todos</h1>
      {load && <div>Загрузка идёт</div>}
      {error && <div>Ошибка сервера</div>}
      {fail && <div>Ошибка клиента</div>}
      {data && (
        <ul>
          {data["result"].map((item) => (
            <li key={item.id}>{item.title}</li>
          ))}
        </ul>
      )}
      <div>
        <button onClick={getData}>click</button>
        <button onClick={resetData}>reset</button>
      </div>
    </div>
  );
}
