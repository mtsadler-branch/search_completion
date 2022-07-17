import './auto-text-complete.css';
import React, { useState } from 'react';

const AutoTextComplete = () => {
  const [inputText, setInputText] = useState('')

  const onChange = (event) => {
    setInputText(event.target.value)
  };

  return (
    <div>
      <h2>Auto text complete input</h2>
      <div className='auto-text-field'>
        <input type="text" id="auto-text" name="auto-text" onChange={(e)=> onChange(e)}></input>
      </div>
    </div>
  );

}

export default AutoTextComplete;
