import React, {useState} from 'react';
import ThemeContext from './ThemeComponent';

function ThemeContext() {
    const { theme, toggleTheme} = useContext(ThemeContext);

    return (
        <div 
        style={{
            backgroundColor: theme === "light" ? "white" : "black",
            color: theme === "light" ? "black" : "white",
            padding: "20px",
        }}>

            <h2>Theme: {theme}</h2>
            <button onClick={toggleTheme}>Toggle Theme</button>
        </div>

    );
}

export default ThemeContext;