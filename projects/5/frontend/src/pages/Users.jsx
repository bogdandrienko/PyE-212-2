import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import axios from "axios";

export const DEBUG = true;

export const USERS_LOAD = "USERS_LOAD_CONSTANT";
export const USERS_DATA = "USERS_DATA_CONSTANT";
export const USERS_ERROR = "USERS_ERROR_CONSTANT";
export const USERS_FAIL = "USERS_FAIL_CONSTANT";
export const USERS_RESET = "USERS_RESET_CONSTANT";

export function GetUsersReducer (state = {}, action = null) {
  switch (action.type) {
    case USERS_LOAD:
      return { load: true };
    case USERS_DATA:
      return { load: false, data: action.payload };
    case USERS_ERROR:
      return { error: "ошибка на сервере" };
    case USERS_FAIL:
      return { fail: "ошибка на клиенте" };
    case USERS_RESET:
      return {};
    default:
      return state;
  }
}

export const GetUsersAction = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: USERS_LOAD,
    });

    // const { ReduxExampleStore: ReduxExampleStore } = getState();

    const config = {
      "method": "GET",
      timeout: 5000,
      url: `/api/get_users/`,
      data: null,
    };
    const response = await axios(config);

    const { data } = response;
    if (data) {
      dispatch({
        type: USERS_DATA,
        payload: data,
      });
    } else {
      dispatch({
        type: USERS_ERROR,
        payload: data,
      });
    }
  } catch (error) {
    if(DEBUG){
      console.log(error);
    }
    dispatch({
      type: USERS_FAIL,
      payload: error,
    });
  }
};

export function Users() {
  const dispatch = useDispatch();

  function getUsers1() {
    if (!load) {
      dispatch(GetUsersAction());
    } else {
        console.log("Предыдущий запрос ещё в обработке!")
    }
  }

  const getUsers2 = () => {
    //
  };

  function resetUsers() {
    dispatch({
      type: USERS_RESET,
    });
  }

  const GetUsersStore = useSelector((state) => state.GetUsersStore);
  const {
    load: load,
    data: data,
    error: error,
    fail: fail,
    reset: reset,
  } = GetUsersStore;

  useEffect(() => {
    console.log(`load: ${load}`);
    console.log(`data: ${data}`);
    console.log(`error: ${error}`);
    console.log(`fail: ${fail}`);
    console.log(`reset: ${reset}`);

    const config1 = {
      "method": "GET",
    };
    
    console.log(config1);
    const config2 = {
      method: "GET",
    };
    console.log(config2);

    console.log(config1.method);
    console.log(config1["method"]);
  
  }, [GetUsersStore]);

  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        {load ? <div>Идёт загрузка...</div> : <div></div>}
        {error ? <div>Ошибка 1</div> : <div></div>}
        {fail ? <div>Ошибка 2</div> : <div></div>}
        {data ? (
          <ul>
            {data["users"].map((user) => (
              <li>{user.username}</li>
            ))}
          </ul>
        ) : (
          <div></div>
        )}
        <div className="btn-group">
          <button
            onClick={getUsers1}
            className="btn btn-lg btn-outline-primary m-1 p-1"
          >
            get
          </button>
          <button
            onClick={resetUsers}
            className="btn btn-lg btn-outline-secondary m-1 p-1"
          >
            reset
          </button>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default Users;
