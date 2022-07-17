import './auto-text-complete.css';
import React, { useState } from 'react';
import { DATA } from './Constants.js'

const AutoTextComplete = () => {
  const [inputText, setInputText] = useState('')

  const onChange = (event) => {
    setInputText(event.target.value)
  };

  const renderList = (option, index) => {
    return (
      <li className={'dropdown-item'} name={option.label} value={option.label} key={index}>
          <label className='dropdown-item-label'>{option.label}</label>
      </li>
    )
}

  return (
    <div>
      <div className='header'>
        <h2>Auto text complete input</h2>
      </div>
      <div className='auto-text-dropdown-container'>
        <div className='auto-text-field'>
          <input type="text" id="auto-text" name="auto-text" onChange={(e)=> onChange(e)}></input>
          {inputText && <div className='auto-text-field-dropdown'>
            <ul className='dropdown-items'>
              {DATA.map((option, index)=> {
                      return (
                        renderList(option, index)
                      )
                    })}
            </ul>
          </div>}
        </div>
      </div>
    </div>
  );

}

export default AutoTextComplete;
