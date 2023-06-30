import { useState } from "react";
import axios from "axios";

export default function Form() {
  const [enteredKeyword, setEnteredKeyword] = useState("");
  const keywordChangeHandler = (event) => {
    setEnteredKeyword(event.target.value);
  };

  const formSubmitHandler = async (e) => {
    e.preventDefault();

    const response = await axios.post("/search", {
      keyword: enteredKeyword,
    });

    if (response.data) {
      console.log(response.data);
    }
  };

  return (
    <form onSubmit={formSubmitHandler} method="post">
      <label htmlFor="keyword">Search keyword: </label>
      <input
        id="keyword"
        name="keyword"
        onChange={keywordChangeHandler}
        value={enteredKeyword}
      />
      <button>Submit</button>
    </form>
  );
}
