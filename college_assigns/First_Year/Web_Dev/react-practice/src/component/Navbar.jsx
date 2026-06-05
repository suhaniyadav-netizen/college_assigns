import React from 'react'
import { Link, NavLink, useNavigate } from 'react-router-dom'
import User from './User'
function Navbar(props) {
  // props.list="Cricket"
  // console.log(props.list)

  const navigate=useNavigate()

  const handleRoute=()=>{
    console.log("REdirecting to the homepage")
    navigate("/sample")
  }
  return (
    <div>
      <h2> This is a NavBar</h2>
      <ul>
        <li>{props.list}</li>
        <li><Link to="/contact">Contact</Link></li>
        <li><Link to='/sample'>Sample</Link></li>
        <li><NavLink to='/sample' className="hover:bg-blue-800 text-white" style={({isActive})=>({color:isActive?'red':'blue'})}>Sample</NavLink></li>
        <button onClick={handleRoute}>Homepage</button>
      </ul>
      <h3> Logo</h3>
      <User />
      
    </div>
  )
}

export default Navbar