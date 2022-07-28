import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";


export const LOAD_TODOS = "LOAD_TODOS";
export const RESULT_TODOS = "RESULT_TODOS";
export const ERROR_TODOS = "ERROR_TODOS";


export function TodosReducer(state = {}, action = null) {
    switch (action.type) {
        case LOAD_TODOS:
          return { load: true, data: undefined, error: undefined };
        case RESULT_TODOS:
          return { load: false, data: action.payload, error: undefined };
        case ERROR_TODOS:
          return { load: false, data: undefined, error: "произошла ошибка" };
        default:
          return state
    }
}

const  Home = () => {
    const dispatch = useDispatch();

    const todos = useSelector((state) => state.todos)
    //let todos = [];
    const getData = () => {
      axios.get("https://jsonplaceholder.typicode.com/todos")
        .then(res => {
          const result = res.data;
          // this.setState({ persons });
          console.log(result)
        //   setTodos(result)
            //todos = result
            dispatch({ type: RESULT_TODOS, payload: result })

        })
    }



    return (
      <div className="App">
        { todos && todos.length > 0 ? ('данные пришли'): ('данных нет') }
        <button onClick={ getData }>click</button>
        <ul>
          { todos && todos.length > 0 ? todos.map(todo => <li key={ todo['id'] }>{todo['title']}</li>): ('данных нет') } 
        </ul>
      </div>
    );
}

export default Home