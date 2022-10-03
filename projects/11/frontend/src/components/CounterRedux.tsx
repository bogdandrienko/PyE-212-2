import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import * as constants from "../components/Constants";




// @ts-ignore
export default function CounterRedux(props={defaultValue: 0, multiply: 1}) {
  const dispatch = useDispatch();

  // @ts-ignore
  const counterRedux = useSelector((state) => state.counterRedux); // {load, data, eror}
  // @ts-ignore
  const tokenRedux = useSelector((state) => state.token);

  useEffect(()=> {
    console.log(counterRedux)
    console.log(tokenRedux)
    dispatch({type: constants.SUCCESS, payload: props.defaultValue })
  }, [])

  useEffect(()=> {
    console.log(tokenRedux)
  }, [tokenRedux])

  function Increase (){
    dispatch({type: constants.SUCCESS, payload: counterRedux.data + props.multiply})
  }

  function Decrease (){
    dispatch({type: constants.SUCCESS, payload: counterRedux.data - props.multiply})
  }

  return (
    <div>counter: {counterRedux.data}
      <div>
        <button onClick={()=> Increase()}>+</button>
        <button onClick={()=> Decrease()}>-</button>
      </div>
        {/* <button onClick={()=> Increase()}>update</button> */}
      
        {tokenRedux && tokenRedux.load && "....Идёт загрузка токена.....    "}
        {tokenRedux && tokenRedux.error && tokenRedux.error}
        token: {tokenRedux && tokenRedux.data && `${tokenRedux.data.access}\n\n\n |||| ${tokenRedux.data.refresh}`}
    </div>
  )
}
