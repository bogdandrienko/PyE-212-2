import React from 'react';
import { Footer2 } from './footers';
import {Navbar1, Navbar2, Navbar4} from './navbars';


export default function Base({children}) {
  return (
    <div className='p-0'>
      <main className="custom_main_1">
        <Navbar1 />
        <div className='p-0'>{children}</div>
      </main>
      <Navbar1/>
    </div>
  )
}

export function Base1({children}) {
  return (
    <div className='m-0 p-0'>
      <Navbar4/>
      <main>{children}</main>
      <Footer2/>
    </div>
  )
}
