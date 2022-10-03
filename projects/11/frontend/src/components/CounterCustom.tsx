import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';

// @ts-ignore
export default function CounterCustom(props={defaultValue: 0, multiply: 1, callbackGetData: any}) {

  const [value1, setValue1] = useState(props.defaultValue);
  // @ts-ignore
  const counterRedux = useSelector((state) => state.counterRedux); // {load, data, eror}

  return (
    <div>counter: {value1} {counterRedux.data}
      <div>
        <button onClick={()=> setValue1(value1 + props.multiply)}>+</button>
        <button onClick={()=> setValue1(value1 - props.multiply)}>-</button>
      </div>
        <button onClick={()=> props.callbackGetData(value1)}>update</button>
    </div>
  )
}
