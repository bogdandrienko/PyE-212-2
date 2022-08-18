import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import { combineReducers } from "redux";
import thunk from "redux-thunk";
import * as reducers from '../components/Reducers'
import * as utils from '../components/utils'
import * as bases from '../components/Base'


// const reducers = {
//   // newsBooks: reducers.getAllNewsBooks,
//   // topBooks: getAllTopBooks,
//   "topBooks": Reducer_TopBooks,
//   "deleteBook": Reducer_DeleteBook,
//   "token": bases.getUserToken,
// }

// export function ConnectToCombine(name: string, reducer: object){
//   // @ts-ignore
//   reducers[name] = reducer;
// }



const globalReducer = combineReducers({
  // newsBooks: reducers.getAllNewsBooks,
  // topBooks: getAllTopBooks,
  categories: reducers.R_Categories,
  topBooks: reducers.R_TopBooks,
  "deleteBook": reducers.R_DeleteBook,
  "token": bases.getUserToken,
});

const initialState = {
};

export const store = configureStore({
  reducer: globalReducer,
  devTools: true,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  preloadedState: initialState,
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
