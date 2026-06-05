import React, { useContext } from "react";
import Counter from "./components/Counter";
import ThemeContext, { themecontext } from "./components/ThemeComponent";

function AppContent() {
  const { darkTheme, changeTheme } = useContext(themecontext);

  return (
    <div>
      <button onClick={changeTheme}>Change Theme</button>
      <p>Theme: {darkTheme ? "Dark" : "Light"}</p>
    </div>
  );
}

function App() {
  return (
    <ThemeContext>
      <div>
        <h1>Context API Implementation Ques 2</h1>
        <Counter />
        <hr />
        <AppContent />
      </div>
    </ThemeContext>
  );
}

export default App;