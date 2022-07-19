import React from 'react';
import {Navbar, Footer} from './ui';


function Base({children}) {
  return (
    <div>
      <main className="custom_main_1">
        <Navbar />
        <div>{children}</div>
      </main>
      <Footer/>
    </div>
  )
}

export default Base