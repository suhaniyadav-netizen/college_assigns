import React, { createContext, useState} from "react";
export const themecontext = createContext();

const ThemeContext = ({children}) => {
    const [darkTheme, setDarkTheme] = useState(false);

    function changeTheme() {
        setDarkTheme(!darkTheme) 
    }

    const value = {darkTheme,setDarkTheme,changeTheme};

    return (
        <themecontext.Provider value = {value}>{children}</themecontext.Provider>
    )
}

export default ThemeContext;