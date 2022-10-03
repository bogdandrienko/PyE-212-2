import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import { combineReducers } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';
import counterReducer from '../features/counter/counterSlice';
import * as reducers from "../components/Reducers";

const globalReducers = combineReducers(
  {
    counterRedux: reducers.CounterReducer,
    token: reducers.TokenReducer,
    counter: counterReducer, // имя переменной (ключ) : редюсер
    //counter1: counterReducer,
  }
)

const preloadedState = {
  //counter: 10,
  //counter1: 19,
  //token: localStorage.getItem("token") ? localStorage.getItem("token") : null,
}

export const store = configureStore({
  reducer: globalReducers,
  devTools: true,
  // @ts-ignore
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  // @ts-ignore
  preloadedState: preloadedState
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
