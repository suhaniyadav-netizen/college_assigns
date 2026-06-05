import React from 'react'
import Navbar from './Navbar';

function HomePage({menu}) {
  const loggedin=false;
//   if(loggedin){
//     return (
//         <button>Logout</button>
//     )
//   }else{
//     return (
//         <button>Login</button>
//     )
//   }

return(
    <>
      <Navbar list={menu} />
      {loggedin?<button>Logout</button>: <button>Login</button>}
    </>
)
}

export default HomePage