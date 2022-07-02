import React from 'react';
import axios from 'axios';
import LOGIN_LOAD from './constants';
import LOGIN_DATA from './constants';
import LOGIN_ERROR from './constants';
import LOGIN_FAIL from './constants';

export function getAllTexts(){
  return async function getAllTexts(dispatch, getState) {
    try{
      dispatch({
        type: LOGIN_LOAD
      });
      const config = {
        method: "GET",
        timeout: 5000,
        url: `/api/chat/read/`,
        data: null,
      };
      // axios(config)
      // .then(res => {
      //   const {result} = res.data;
      //   console.log(result);
      //   setTexts(result);
      // });
      const {result} = await axios(config);
      console.log(3);
      console.log(result);
      if (result){
        dispatch({
          type: LOGIN_DATA,
          payload: result
        });
      } else {
        dispatch({
          type: LOGIN_ERROR,
          payload: result
        });
      }
    } catch (error){
      console.log(error);
      dispatch({
        type: LOGIN_FAIL,
        payload: error
      });
    }
  };
}





