import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import Navbar from "../components/navbar";
import Footer from "../components/footer";

export const LOGIN_LOAD = "LOGIN_LOAD_CONSTANT";
export const LOGIN_DATA = "LOGIN_DATA_CONSTANT";
export const LOGIN_ERROR = "LOGIN_ERROR_CONSTANT";
export const LOGIN_FAIL = "LOGIN_FAIL_CONSTANT";
export const LOGIN_RESET = "LOGIN_RESET_CONSTANT";

export const ReduxExampleAction = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: LOGIN_LOAD,
    });

    // const { ReduxExampleStore: ReduxExampleStore } = getState();

    const config = {
      method: "GET",
      timeout: 10000,
      url: `/api/chat/read/`,
      data: null,
    };
    const response = await axios(config);
    // console.log(response);

    const { data } = response;
    if (data) {
      dispatch({
        type: LOGIN_DATA,
        payload: data,
      });
    } else {
      dispatch({
        type: LOGIN_ERROR,
        payload: data,
      });
    }
  } catch (error) {
    console.log(error);
    dispatch({
      type: LOGIN_FAIL,
      payload: error,
    });
  }
};

export const ReduxExampleReducer = (state = {}, action = null) => {
  switch (action.type) {
    case LOGIN_LOAD:
      return { load: true };
    case LOGIN_DATA:
      return { load: false, data: action.payload };
    case LOGIN_ERROR:
      return { error: "ошибка на сервере" };
    case LOGIN_FAIL:
      return { fail: "ошибка на клиенте" };
    case LOGIN_RESET:
      return {};
    default:
      return state;
  }
};

export function ReduxExamplePage() {
  const dispatch = useDispatch();

  const ReduxExampleStore = useSelector((state) => state.ReduxExampleStore);
  const {
    load: load,
    data: data,
    error: error,
    fail: fail,
  } = ReduxExampleStore;

  const checkReducer = () => {
    dispatch(ReduxExampleAction());
  };

  const resetReducer = () => {
    dispatch({ type: LOGIN_RESET });
  };

  useEffect(() => {
    console.log(`load: ${load}`);
    console.log(`data: ${data}`);
    console.log(`error: ${error}`);
    console.log(`fail: ${fail}`);
  }, [ReduxExampleStore]);

  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        <div style={{ margin: "50px" }}>
          <h1>Redux Example Component</h1>

          <div className="btn-group">
            <button
              className="btn btn-lg btn-outline-primary"
              onClick={checkReducer}
            >
              check
            </button>
            <button
              className="btn btn-lg btn-outline-secondary"
              onClick={resetReducer}
            >
              reset
            </button>
          </div>

          <div className="card m-1 p-1">
            {load && <div className="text-primary">Идёт загрузка...</div>}
            {data && data.result && (
              <ul className="list-group mb-3">
                {data.result.map((x) => (
                  <li
                    key={x.id}
                    className="list-group-item d-flex justify-content-between lh-sm"
                  >
                    <div>
                      <h6 className="my-0">{x.text}</h6>
                    </div>
                    <span className="text-muted">#{x.id}</span>
                  </li>
                ))}
              </ul>
            )}
            {error && <div className="text-danger">{error}</div>}
            {fail && <div className="text-warning">{fail}</div>}
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
